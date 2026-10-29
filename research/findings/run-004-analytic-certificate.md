# A rational second derivative enclosure for E_7611

Date: October 29, 2026. Revision 1. Status: candidate mathematical argument with an exact interval computation, submitted for separate review. This is a calibration observation, not a protected benchmark, novelty claim, formal proof receipt or full BSD solution. The author cannot certify this claim.

## Exact claim and mathematical dependencies

Let E/Q be the elliptic curve `y^2=x^3-7611^2*x`, with coefficient vector `[0,0,0,-57927321,0]`. Let L(E,s) use the Hasse Weil normalization with good Euler polynomial `1-a_p*T+p*T^2`, where `T=p^(-s)`. The candidate enclosure is

\[
\frac{1561}{100}<L''(E,1)<\frac{1563}{100}.
\]

The [source dossier](../sources/run-004-analytic-sources.md) fixes the analytic bridges, conventions and source locators. This argument depends on those sourced facts and on the [reviewed run 003 rank and descent record](../sources/run-003-route-a.md), not on a database analytic rank.

The inputs are: 7611=3·43·59 is positive and squarefree; E has conductor `N=32*7611^2=1853674272`; its completed L function

\[
\Lambda(E,s)=\left(\frac{\sqrt N}{2\pi}\right)^s\Gamma(s)L(E,s)
\]

is entire and has functional equation sign +1. The established algebraic rank is two. The classical implication from analytic rank zero or one to equal algebraic rank therefore rules out analytic orders zero and one. This is a contraposition of an existing theorem; it does not assume BSD in rank two. Thus `L(E,1)=L'(E,1)=0` exactly.

Under these inputs the nonzero second derivative proves analytic order exactly two for this single curve. It does not prove analytic rank two throughout the prime qualified family. It does not prove finiteness of full Sha or a leading coefficient identity.

## Formula and coefficient identification

Put `x=2*pi/sqrt(N)` and

\[
G_2(z)=\int_1^\infty e^{-zt}\log(t)\,\frac{dt}{t}\qquad(z>0).
\]

Cremona, *Algorithms for Modular Elliptic Curves*, corrected online Chapter II, Proposition 2.13.1 on printed page 43, gives

\[
L''(E,1)=4\sum_{m=1}^{\infty}\frac{a_m}{m}G_2(mx).
\]

The proposition requires order at least two and Fricke eigenvalue negative one, which corresponds to functional equation sign positive one. It does not assume exact order two. The factor four is `2*2!`; no period division is present. The following page gives the convergent expansion

\[
G_2(z)=\frac{(\log z+\gamma)^2}{2}+\frac{\pi^2}{12}
       +\sum_{k=1}^{\infty}\frac{(-z)^k}{k^2 k!}.
\]

These inspected formulas are the only special function identities used. [Cremona Chapter II](https://johncremona.github.io/book/fulltext/chapter2.pdf)

The exact coefficients are identified through the CM curve E_1:`y^2=x^3-x`. For an odd good prime p congruent to 3 modulo 4, `a_p(E_1)=0`. For a prime p congruent to 1 modulo 4, write `p=a^2+b^2` with a odd, b even, and choose the sign of a so `a+b=1 mod 4`. Then `a_p(E_1)=2*a`. Ribet's *Modular forms and Diophantine questions*, section 6, Theorem 1, printed pages 9 to 11, provides the point count formula; the point at infinity must be included when converting it to trace. [Author paper](https://math.berkeley.edu/~ribet/Articles/icfs.pdf)

For p not dividing 2·7611, the quadratic twist trace is `a_p(E)=Legendre(7611,p)*a_p(E_1)`. At each of 2,3,43,59 the reduction is additive and the local Euler factor is 1, so every coefficient with such a prime factor is zero. At good primes, `a_(p^(j+1))=a_p*a_(p^j)-p*a_(p^(j-1))`, and coefficients at coprime indices multiply. The program implements the equivalent recurrence using the smallest prime divisor. The primitive twist character has discriminant 30444; its odd prime values are the displayed Legendre symbols. No incorrect assumption that the primitive conductor is 7611 enters this construction.

Hasse's bound and the Euler factors imply `|a_m| <= d(m)*sqrt(m) <= 2*m`, exactly as derived in the run 002 certificate. This uniform bound controls the omitted Fourier terms. The CM identity accelerates the finite coefficient computation; it does not replace that tail estimate with a numerical assumption.

## Exact interval construction

Every numerical operation in `compute.py` uses integers or rational fractions. An integer pair `(l,u)` denotes the real interval `[l/Q,u/Q]`, with `Q=10^45`. Addition is exact. Multiplication takes the minimum and maximum of the four endpoint products before outward division by Q. Division by a positive integer uses floor and ceiling. Negative scalar multiplication reverses endpoints. Squaring returns lower endpoint zero whenever the input interval crosses zero. Consequently every interval contains the corresponding exact mathematical value, provided its inputs do.

The constant pi is enclosed using `pi=16*atan(1/5)-4*atan(1/239)` and alternating rational series, with respectively 40 and 12 terms. The identity follows from the tangent addition formula with the angles in the first quadrant. Each omitted alternating tail is bounded by its next term. All operations before conversion to fixed scale use `Fraction`.

Logarithms use exact range reduction `v=2^j*u`, with `1<=u<2`, followed by

\[
\log u=2\sum_{k=0}^{\infty}\frac{z^{2k+1}}{2k+1},
\qquad z=\frac{u-1}{u+1}\in[0,1/3).
\]

After K=55 terms the positive omitted tail is at most

\[
\frac{2z^{2K+1}}{(2K+1)(1-z^2)}.
\]

The same formula at z=1/3 encloses log(2). All range reduction, series powers and remainder evaluations retain outward endpoints. The code checks that the reduced upper endpoint stays below two.

Euler's constant needs no floating approximation or Euler Maclaurin formula. For H_J the Jth harmonic sum, elementary integral comparison gives

\[
H_J-\log J-\frac1J<\gamma<H_J-\log J.
\]

Indeed, `H_J-log(J)-gamma` is the sum over k at least J of `integral_k^(k+1) (1/t-1/(k+1)) dt`, which is positive and less than the telescoping sum of `1/k-1/(k+1)`, namely 1/J. The code takes J=1000000, sums the harmonic terms with outward integer division and uses the logarithm interval above. This deliberately broad interval dominates the final enclosure width and is sufficient to exclude zero.

The integer square root of `N*Q^2` gives an interval for sqrt(N); rational division with the pi interval then encloses x. No unqualified numerical square root appears.

For a kernel argument z, let `t_k=z^k/(k^2*k!)`. The recurrence

\[
t_{k+1}=t_k\,z\,\frac{k^2}{(k+1)^3}
\]

is evaluated with outward intervals. The program sums 200 signed terms in the G2 expansion. Subsequent consecutive term ratios are at most `z/(202)`, less than one throughout the computed range. Thus the absolute omitted series is bounded by `t_201/(1-z/202)`. Both endpoints of z enter this bound and the polynomial part. Alternating signs do not justify treating an uncertain z as exact; the code never does so.

## Fourier tail and exact result

The finite sum stops at M=220000. There are 21493 nonzero coefficients. For z>0, `log(t)<=t-1` and `1/t<=1` on t at least one give

\[
0<G_2(z)\le\int_1^\infty e^{-zt}(t-1)\,dt
=\frac{e^{-z}}{z^2}.
\]

Consequently the absolute omitted Fourier contribution is at most

\[
8\sum_{m>M}\frac{e^{-mx}}{(mx)^2}
\le\frac{8e^{-x(M+1)}}{x^2(M+1)^2(1-e^{-x})}.
\]

No exponential routine is needed to evaluate this bound. Let a be the rational lower bound for x, let t=a(M+1), and let h=floor(t). The inequalities `e>2` and `e^a>=1+a` give the conservative rational bound

\[
\frac{8\,2^{-h}(1+a)}{t^2a}.
\]

Monotonicity permits replacement of x by its lower bound. This rational bound is added to the finite upper endpoint and subtracted from the finite lower endpoint.

The retained exact final interval has common denominator

`1000000000000000000000000000000000000000000000`

and numerators

`15619015896289589868978475381196230103954281066`

and

`15620296589727118662310624636835675868427046363`.

Integer cross multiplication proves that this interval lies strictly between 1561/100 and 1563/100. Thus it excludes zero with a wide margin. These rational endpoints, rather than displayed decimal approximations, are the candidate certificate.

## Execution, limitations and handoff

The [experiment](../experiments/run-004-analytic/README.md) contains the code, deterministic output and actual execution receipt. The frozen program ran under Python 3.14.6, exited 0 and took 4.283782624988817 measured seconds. The complete coefficient array has the recorded SHA256 `c605aced34fcd03ed3d7a54079707f411083819140a15d6c516a8b421e2a8b73` under the documented JSON serialization. This hash binds arithmetic output; it is not a proof of coefficient identification.

An initial implementation run with the same mathematical bounds returned the same enclosure in 3.937913000001572 measured seconds. Before freezing, variable timing was removed from deterministic output and placed in the receipt. No arithmetic execution failed. A contemplated approach using a decimal transcendental library was not implemented. The local environment had no installed flint, mpmath, numpy, scipy or gmpy2; exact fixed point intervals removed that tooling dependency. No package was installed, model changed or external computation service used.

Separate review must audit the exact conductor and sign, lower order vanishing, CM trace convention and bad Euler factors, every interval operation and remainder, a separately generated coefficient array, and independent kernel checks. A successful program exit cannot substitute for those bridges. Python's integer arithmetic and the interpreter are part of the computational trust boundary; no formal theorem prover was run.

If the separate review supports the argument, the conclusion is analytic rank exactly two for this E_7611, under the stated established theorem dependencies. Full Sha finiteness, its odd primary components, saturation of the displayed Mordell Weil points, the full regulator and BSD's leading coefficient identity remain unproved by this run. The coordinator owns state integration and Git checkpoints; author submission does not promote its own status.
