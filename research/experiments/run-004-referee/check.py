"""Separate exact coefficient and selected kernel checks for Run 004.

This does not independently sum the entire second derivative certificate.
"""
from fractions import Fraction as F
from math import isqrt, factorial
from pathlib import Path
import hashlib
import json
import sys


def logarithm(x: F) -> tuple[F, F]:
    def small(t: F) -> tuple[F, F]:
        z = (t-1)/(t+1)
        assert 0 <= z <= F(1, 3)
        value = sum((2*z**(2*j+1)/F(2*j+1) for j in range(100)), F(0))
        error = 2*z**201/(201*(1-z*z))
        return value, value+error
    exponent = 0
    while x < 1:
        x *= 2
        exponent -= 1
    while x >= 2:
        x /= 2
        exponent += 1
    lo, hi = small(x)
    l2, h2 = small(F(2))
    return (lo+min(exponent*l2, exponent*h2), hi+max(exponent*l2, exponent*h2))


def pi_bounds() -> tuple[F, F]:
    def arctan(q: int) -> tuple[F, F]:
        s = sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(100)), F(0))
        return s, s+F(1, 201*q**201)
    l5, h5 = arctan(5)
    l239, h239 = arctan(239)
    return 16*l5-4*h239, 16*h5-4*l239


def bernoulli(n: int) -> list[F]:
    out: list[F] = []
    for m in range(n+1):
        out.append(F(1, m+1))
        for j in range(m, 0, -1):
            out[j-1] = j*(out[j-1]-out[j])
        yield_value = out[0]
        if m == 0:
            values = [yield_value]
        else:
            values.append(yield_value)
    return values


def gamma_bounds() -> tuple[F, F]:
    # Euler Maclaurin remainder is bounded by the first omitted term for H_N.
    n, k = 100, 16
    bs = bernoulli(2*k+2)
    correction = sum((bs[2*j]/(2*j*n**(2*j)) for j in range(1, k+1)), F(0))
    loglo, loghi = logarithm(F(n))
    h = sum((F(1, j) for j in range(1, n+1)), F(0))
    remainder = abs(bs[2*k+2]/((2*k+2)*n**(2*k+2)))
    center = h-F(1, 2*n)+correction
    return center-loghi-remainder, center-loglo+remainder


def kernel(x: F, gamma: tuple[F, F], pi: tuple[F, F]) -> tuple[F, F]:
    l, h = logarithm(x)
    l += gamma[0]
    h += gamma[1]
    sl = 0 if l <= 0 <= h else min(l*l, h*h)
    sh = max(l*l, h*h)
    series = sum(((-x)**j/(j*j*factorial(j)) for j in range(1,181)), F(0))
    remainder = x**181/(181**2*factorial(181))
    assert x <= 33
    # Terms decrease after the truncation; the omitted first term is negative.
    return sl/2+pi[0]**2/12+series-remainder, sh/2+pi[1]**2/12+series


def coefficient_array(limit: int) -> tuple[list[int], list[int]]:
    spf = list(range(limit+1))
    for p in range(2,isqrt(limit)+1):
        if spf[p] == p:
            for m in range(p*p,limit+1,p):
                if spf[m] == m:
                    spf[m] = p
    primes = [p for p in range(2,limit+1) if spf[p] == p]
    ap = [0]*(limit+1)
    for a in range(1,isqrt(limit)+1,2):
        for b in range(2,isqrt(limit-a*a)+1,2):
            p = a*a+b*b
            if spf[p] == p:
                sign = 1 if (a+b-1)//2 % 2 == 0 else -1
                chi = pow(7611%p,(p-1)//2,p)
                if chi == p-1:
                    chi = -1
                ap[p] = 2*a*sign*chi
    coeff = [0]*(limit+1)
    coeff[1] = 1
    for m in range(2,limit+1):
        p = spf[m]
        if p in (2,3,43,59):
            continue
        rest, power = m, 1
        while rest % p == 0:
            rest //= p
            power *= p
        if power == p:
            value = ap[p]
        else:
            value = ap[p]*coeff[power//p]-p*coeff[power//(p*p)]
        coeff[m] = value*coeff[rest]
    return coeff, primes


def main() -> None:
    limit = 220000
    coeff, primes = coefficient_array(limit)
    tests = []
    for p in primes:
        if p > 1000:
            break
        if p in (2,3,43,59):
            assert coeff[p] == 0
            continue
        count = 1
        for x in range(p):
            value = (x*x*x-7611**2*x)%p
            count += 1 if value == 0 else (2 if pow(value,(p-1)//2,p) == 1 else 0)
        trace = p+1-count
        assert trace == coeff[p], (p,trace,coeff[p])
        tests.append([p,trace])
    assert 7611 == 3*43*59
    assert 32*7611**2 == 1853674272
    assert all(coeff[m] == 0 for p in (2,3,43,59) for m in range(p,limit+1,p))
    pi, gamma = pi_bounds(), gamma_bounds()
    scale = 10**50
    kernels = []
    for x in (F(1,10000), F(1,10), F(1), F(3), F(10), F(30), F(33)):
        lo, hi = kernel(x,gamma,pi)
        lower = lo.numerator*scale//lo.denominator
        upper = -((-hi.numerator*scale)//hi.denominator)
        assert lower <= upper
        kernels.append({'x':str(x),'scale':str(scale),'lower_numerator':str(lower),'upper_numerator':str(upper)})
    coefficient_bytes = (','.join(map(str,coeff[1:]))+'\n').encode()
    print(json.dumps({'limit':limit,'coefficient_encoding':'comma separated a1 through aM plus newline','coefficient_sha256':hashlib.sha256(coefficient_bytes).hexdigest(),'direct_good_prime_counts':tests,'direct_good_prime_count_total':len(tests),'bad_prime_multiples_zero':True,'kernel_bounds':kernels,'pi_interval_width_lt_1e130':pi[1]-pi[0]<F(1,10**130),'gamma_interval_width_lt_1e50':gamma[1]-gamma[0]<F(1,10**50),'scope':'Independent coefficient implementation and selected exact rational kernel enclosures; not a second full L derivative sum.'},indent=2))


if __name__ == '__main__':
    main()
