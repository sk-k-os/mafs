"""Hash bound replay and comparison of the submitted Run 004 certificate."""
from pathlib import Path
from fractions import Fraction as F
import datetime
import hashlib
import importlib.util
import json
import platform
import subprocess
import time

ROOT = Path('research/experiments/run-004-referee')
AUTHOR = Path('research/experiments/run-004-analytic')


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name,path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def main() -> None:
    inputs = [ROOT/'check.py', AUTHOR/'compute.py', AUTHOR/'output.json']
    before = {str(p):digest(p) for p in inputs}
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    tick = time.monotonic()
    own_run = subprocess.run(['python3',str(ROOT/'check.py')],capture_output=True,text=True)
    assert own_run.returncode == 0, own_run.stderr
    (ROOT/'output.json').write_text(own_run.stdout)
    own_data = json.loads(own_run.stdout)
    own = module('referee_004',ROOT/'check.py')
    author = module('author_004',AUTHOR/'compute.py')
    coeff, _ = own.coefficient_array(author.LIMIT)
    assert coeff == author.coefficients()
    agamma, api = author.gamma_interval(), author.pi_interval()
    ogamma, opi = own.gamma_bounds(), own.pi_bounds()
    assert F(agamma[0],author.SCALE) <= ogamma[0] <= ogamma[1] <= F(agamma[1],author.SCALE)
    assert F(api[0],author.SCALE) <= opi[0] <= opi[1] <= F(api[1],author.SCALE)
    kernel_checks = []
    for row in own_data['kernel_bounds']:
        x = F(row['x'])
        ai = author.kernel(author.ratio(x.numerator,x.denominator),agamma,api)
        lo = F(int(row['lower_numerator']),int(row['scale']))
        hi = F(int(row['upper_numerator']),int(row['scale']))
        assert F(ai[0],author.SCALE) <= lo <= hi <= F(ai[1],author.SCALE)
        kernel_checks.append({'x':str(x),'independent_rational_interval_inside_author_interval':True})
    replay = subprocess.run(['python3',str(AUTHOR/'compute.py')],capture_output=True,text=True)
    assert replay.returncode == 0, replay.stderr
    assert replay.stdout == (AUTHOR/'output.json').read_text()
    data = json.loads(replay.stdout)
    scale = int(data['interval_scale'])
    xlo = F(int(data['x_interval']['lower_numerator']),scale)
    tlo = xlo*(data['coefficient_cutoff']+1)
    conservative_tail = 8*F(1,2**(tlo.numerator//tlo.denominator))*(1+xlo)/(tlo*tlo*xlo)
    assert conservative_tail <= F(int(data['absolute_tail_upper_numerator']),scale)
    enclosure = data['second_derivative_enclosure']
    assert F(1561,100) < F(int(enclosure['lower_numerator']),scale)
    assert F(int(enclosure['upper_numerator']),scale) < F(1563,100)
    after = {str(p):digest(p) for p in inputs}
    assert before == after
    receipt = {'started_utc':started,'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'elapsed_seconds_measured':time.monotonic()-tick,'exit_code':0,'python_version':platform.python_version(),
               'input_hashes_before':before,'input_hashes_after':after,'inputs_unchanged':True,
               'referee_output_sha256':digest(ROOT/'output.json'),'replay_script_sha256':digest(ROOT/'replay.py'),
               'all_coefficients_equal_through':author.LIMIT,'direct_good_prime_count_total':own_data['direct_good_prime_count_total'],
               'kernel_comparisons':kernel_checks,'independent_constant_intervals_inside_author_intervals':True,
               'tail_bound_recomputed_as_fraction':True,'author_full_output_replayed_byte_identically':True,
               'strict_coarse_enclosure':['1561/100','1563/100'],
               'limits':'Separate coefficient implementation and selected exact kernel calculations; entire derivative sum replays author code. Shared model family, tools and mathematical dependencies. No formal prover or external human review.'}
    (ROOT/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'exit_code':0,'receipt_sha256':digest(ROOT/'receipt.json'),'referee_output_sha256':digest(ROOT/'output.json'),'all_coefficients_equal_through':author.LIMIT,'kernel_cases':len(kernel_checks),'strict_coarse_enclosure':['1561/100','1563/100']},indent=2))


if __name__ == '__main__':
    main()
