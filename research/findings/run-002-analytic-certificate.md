# A positive rational enclosure for the control derivative

Date: October 28, 2026. Revision 1. Status: candidate mathematical argument submitted for separate review. This author does not certify the argument. No formal checker or qualified human referee has assessed this revision. The result concerns one known control curve and makes no novelty or universal BSD claim.

## Exact statement and dependencies

Let C/Q be the elliptic curve `y^2 + y = x^3 - x`, with coefficients `[0,0,1,-1,0]`. Let L(C,s) denote its Hasse Weil L function with local variable `p^(-s)`, so that at each good prime p the Euler polynomial is `1 - a_p*T + p*T^2` and `a_p = p+1-#C(F_p)`. Write its Dirichlet coefficients as a_n, with a_1=1.

The submitted conclusion is the strict rational enclosure

\[
\frac{73}{2240}<L'(C,1)<\frac{69}{80}.
\]

Together with exact central vanishing, this gives `ord_(s=1) L(C,s)=1`. The argument depends on the following standard mathematical facts and on their applicability to this exact model. Their source audit and local arithmetic are separate coordinator and source specialist artifacts.

1. C has conductor 37 and is modular. There is a normalized weight 2 newform of level 37 whose L function agrees with this Hasse Weil L function, including its bad Euler factor.
2. Its completed L function `Lambda(s) = (sqrt(37)/(2*pi))^s Gamma(s) L(C,s)` is entire and obeys `Lambda(s) = -Lambda(2-s)`. Thus `L(C,1)=0` exactly. The corresponding Fricke eigenvalue is +1; the sign of the functional equation is its negative.
3. Hasse's theorem bounds each good local Frobenius root in complex absolute value by sqrt(p), in fact with equality. The bad local factors have coefficients of absolute value at most one at every prime power.

These are explicit theorem dependencies, not open conjectures. The [source dossier](../sources/run-002-analytic-sources.md) supplies inspected theorem locations and conventions. This finding alone does not establish the conductor or root number. Modularity and Euler coefficient identity identify the form directly; a database name, displayed analytic rank or approximate zero is unnecessary. No algebraic rank, Tate Shafarevich group or leading coefficient conclusion is asserted here.

## Derivative formula and convergence

Set `x = 2*pi/sqrt(37)` and define

\[
E_1(t)=\int_1^\infty e^{-tu}\frac{du}{u}
      =\int_t^\infty e^{-v}\frac{dv}{v}\qquad(t>0).
\]

The formula used is

\[
L'(C,1)=2\sum_{n=1}^\infty\frac{a_n}{n}E_1(nx).
\]

For a direct source, Cremona, *Algorithms for Modular Elliptic Curves*, corrected online second edition, Chapter II, Proposition 2.13.1, equation (2.13.2), printed page 43, applies with r=1 and Fricke eigenvalue +1. Its hypothesis is vanishing of order **at least** one, already supplied by the sign; it does not assume the desired exact analytic rank. [Chapter II](https://johncremona.github.io/book/fulltext/chapter2.pdf)

For clarity the formula can also be derived from the split Mellin integral. If f is the normalized modular form, the functional equation gives

\[
\Lambda(s)=\int_1^\infty f(it/\sqrt{37})
                 \bigl(t^{s-1}-t^{1-s}\bigr)\,dt.
\]

Differentiating at one gives `Lambda'(1)=2 integral_1^infinity f(it/sqrt(37)) log(t) dt`. The coefficient estimate below gives exponential domination on this interval, so termwise differentiation and integration near one are valid. Integration by parts yields

\[
\int_1^\infty e^{-nxt}\log(t)\,dt=\frac{E_1(nx)}{nx}.
\]

Since L(C,1)=0 and Gamma(1)=1, `Lambda'(1)=L'(C,1)/x`. Substitution gives the stated series. This derivation uses no assumption of nonvanishing.

## Uniform coefficient bound

At a good p, factor its Euler polynomial as `(1-alpha*T)(1-beta*T)` with `|alpha|=|beta|=sqrt(p)`. Expanding its inverse gives

\[
a_{p^k}=\sum_{j=0}^k\alpha^j\beta^{k-j},\qquad
|a_{p^k}|\le(k+1)p^{k/2}.
\]

At a bad prime the local inverse is either 1 or `(1-a_p*T)^(-1)` with `a_p` equal to +1 or -1, so the same bound holds. Multiplicativity gives `|a_n| <= d(n)*sqrt(n)`, where d(n) is the number of positive divisors. Pairing a divisor at most sqrt(n) with its complementary divisor proves `d(n) <= 2*sqrt(n)`. Consequently

\[
|a_n|\le2n\quad(n\ge1).
\]

The source for Hasse and the precise local factors is Milne, *Elliptic Curves*, second edition (2021), Chapter IV, Theorem 9.4, printed page 150, and the Euler factors on printed page 164. The subsequent coefficient and divisor estimates are given explicitly above. [Book](https://www.jmilne.org/math/Books/EC2.pdf)

Modulo 2, `x^3-x=0` for both x and `y^2+y=0` for both y. Thus C has four affine points and one point at infinity, so `a_2=2+1-5=-2`. The discriminant is 37, hence 2 is good. No other coefficient needs to be computed.

## Elementary analytic bounds

For t>0,

\[
\frac{e^{-t}}{t+1}\le E_1(t)\le\frac{e^{-t}}t.
\]

The upper bound follows by bounding `1/v` by `1/t` in the defining integral. For the lower bound, write `E_1(t)=e^(-t) integral_0^infinity e^(-u)/(t+u) du`. The pointwise identity

\[
\frac1{t+u}-\left(\frac1{t+1}-\frac{u-1}{(t+1)^2}\right)
=\frac{(u-1)^2}{(t+u)(t+1)^2}\ge0
\]

integrates to the claim, because both `integral e^(-u) du` and `integral u*e^(-u) du` on the positive half line equal one.

All transcendental comparisons needed below have exact rational certificates. The identity `pi/4=integral_0^1 1/(1+t^2) dt` and the finite geometric expansion imply that a partial sum `sum_(k=0)^(m-1) (-1)^k/(2*k+1)` bounds pi/4 from below for even m and above for odd m. With m=26 and m=7, respectively, exact arithmetic yields

\[
\frac{31}{10}<\pi<\frac{33}{10}.
\]

The comparison `(31/5)^2>37` then gives x>1; `sqrt(37)>6` gives `x<11/10`. These bounds are intentionally coarse.

Also `e > sum_(k=0)^4 1/k! =65/24 >8/3`, hence `e^(-1)<3/8`. For z=11/10, the ratios of consecutive exponential terms starting after `z^2/2` are at most z/3, so

\[
e^{11/10}\le 1+\frac{11}{10}
 +\frac{(11/10)^2}{2(1-11/30)}
=\frac{1161}{380}<\frac{10}{3}.
\]

This yields `E_1(x) >= e^(-x)/(x+1)>1/7`.

## Rational enclosure

Put q=3/8 and

\[
S=\frac{L'(C,1)}2=E_1(x)-E_1(2x)+R,
\qquad R=\sum_{n=3}^\infty\frac{a_n}{n}E_1(nx).
\]

Since x>1 and `e^(-1)<q`,

\[
0<E_1(2x)<\frac{q^2}{2}=\frac9{128},
\qquad
|R|\le2\sum_{n=3}^\infty E_1(nx)
 <2\sum_{n=3}^\infty\frac{q^n}{n}
 \le\frac{2q^3}{3(1-q)}=\frac9{160}.
\]

These bounds also establish absolute convergence of the derivative series. Therefore

\[
S>\frac17-\frac9{128}-\frac9{160}=\frac{73}{4480}>0.
\]

For the upper bound, discard the negative second term and use `E_1(x)<q` to obtain

\[
S<\frac38+\frac9{160}=\frac{69}{160}.
\]

Multiplying by two proves the submitted enclosure, under the explicit analytic bridges above. Together with exact central vanishing and holomorphy, strict positivity means the zero at one is simple.

## Evidence, unsuccessful routes and review obligations

The [exact experiment](../experiments/run-002-analytic/README.md) checks the finite pi bounds, exponential comparisons, point count and final fractions with rational arithmetic. It does not formally prove the analytic or modular statements. The public output records strict rational endpoints; there is no precision parameter or floating point value in the proof.

An initial approach bounded every coefficient from n=2 onward by 2n. It gave a tail estimate `q^2/(1-q)=9/40`, greater than the retained first term lower bound 1/7, so it failed to prove positivity. Computing only a_2 removes that obstruction. This failed estimate is not evidence against the conclusion. A more elaborate plan to compute many coefficients and enclose E1 numerically was superseded before implementation, because the elementary two coefficient bound suffices. Database derivative values were discussed by the team only as diagnostics and are absent from every inequality used here.

Separate review must check the conductor, modularity and functional equation sign for this exact model; the Fricke sign convention; every integral and convergence step; Hasse and bad Euler factor applicability; and an independent reconstruction of the decisive rational bounds. The source and root number dossiers must be linked in the coordinator's final record. The initial submission remains a candidate pending that review. Author generated arithmetic output cannot promote its own mathematical status.
