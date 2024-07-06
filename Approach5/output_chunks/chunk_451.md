### Uncertainty
principle[[edit](/w/index.php?title=Quantum\_mechanics&action=edit&section=4
"Edit section: Uncertainty principle")]

One consequence of the basic quantum formalism is the uncertainty principle.
In its most familiar form, this states that no preparation of a quantum
particle can imply simultaneously precise predictions both for a measurement
of its position and for a measurement of its momentum.[25][26] Both position
and momentum are observables, meaning that they are represented by Hermitian
operators. The position operator X ^ {\displaystyle {\hat {X}}}
![{\\displaystyle {\\hat
{X}}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/acc59ad6d9a06d55b96b65beb0fdfc89acc1e40e)
and momentum operator P ^ {\displaystyle {\hat {P}}} ![{\\displaystyle {\\hat
{P}}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/7a46a8cf7bc789e8c4f8de7ca0d9946a46fb8842)
do not commute, but rather satisfy the [canonical commutation
relation](/wiki/Canonical\_commutation\_relation "Canonical commutation
relation"):

 [ X ^ , P ^ ] = i ℏ . {\displaystyle [{\hat {X}},{\hat {P}}]=i\hbar .} ![{\\displaystyle \[{\\hat {X}},{\\hat {P}}\]=i\\hbar .}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/803fe39b0eeaff8d1570df480e738cf5a968cc71)

Given a quantum state, the Born rule lets us compute expectation values for
both X {\displaystyle X} ![{\\displaystyle
X}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/68baa052181f707c662844a465bfeeb135e82bab)
and P {\displaystyle P} ![{\\displaystyle
P}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/b4dc73bf40314945ff376bd363916a738548d40a),
and moreover for powers of them. Defining the uncertainty for an observable by
a [standard deviation](/wiki/Standard\_deviation "Standard deviation"), we have

 σ X = ⟨ X 2 ⟩ − ⟨ X ⟩ 2 , {\displaystyle \sigma \_{X}={\textstyle {\sqrt {\left\langle X^{2}\right\rangle -\left\langle X\right\rangle ^{2}}}},} ![{\\displaystyle \\sigma \_{X}={\\textstyle {\\sqrt {\\left\\langle X^{2}\\right\\rangle -\\left\\langle X\\right\\rangle ^{2}}}},}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/457ec20972d63dfb1ecc9087e18d1f949f908c8f)

and likewise for the momentum:

 σ P = ⟨ P 2 ⟩ − ⟨ P ⟩ 2 . {\displaystyle \sigma \_{P}={\sqrt {\left\langle P^{2}\right\rangle -\left\langle P\right\rangle ^{2}}}.} ![{\\displaystyle \\sigma \_{P}={\\sqrt {\\left\\langle P^{2}\\right\\rangle -\\left\\langle P\\right\\rangle ^{2}}}.}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/63ec8f5f7b9e5957ea6d06c56068b06244acc184)

The uncertainty principle states that

 σ X σ P ≥ ℏ 2 . {\displaystyle \sigma \_{X}\sigma \_{P}\geq {\frac {\hbar }{2}}.} ![{\\displaystyle \\sigma \_{X}\\sigma \_{P}\\geq {\\frac {\\hbar }{2}}.}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/538cada7fa57155ece387e5d53d90ca366e323fe)

Either standard deviation can in principle be made arbitrarily small, but not
both simultaneously.[27] This inequality generalizes to arbitrary pairs of
self-adjoint operators A {\displaystyle A} ![{\\displaystyle
A}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3)
and B {\displaystyle B} ![{\\displaystyle
B}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/47136aad860d145f75f3eed3022df827cee94d7a).
The [commutator](/wiki/Commutator "Commutator") of these two operators is

 [ A , B ] = A B − B A , {\displaystyle [A,B]=AB-BA,} ![{\\displaystyle \[A,B\]=AB-BA,}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/b2a47259b42e63c048c65f67d304404867841951)

and this provides the lower bound on the product of standard deviations:

 σ A σ B ≥ 1 2 | ⟨ [ A , B ] ⟩ | . {\displaystyle \sigma \_{A}\sigma \_{B}\geq {\tfrac {1}{2}}\left|{\bigl \langle }[A,B]{\bigr \rangle }\right|.} ![{\\displaystyle \\sigma \_{A}\\sigma \_{B}\\geq {\\tfrac {1}{2}}\\left|{\\bigl \\langle }\[A,B\]{\\bigr \\rangle }\\right|.}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/d0fd768b447334e150b8b98181f74b475e41ee52)

Another consequence of the canonical commutation relation is that the position
and momentum operators are [Fourier
transforms](/wiki/Fourier\_transform#Uncertainty\_principle "Fourier transform")
of each other, so that a description of an object according to its momentum is
the Fourier transform of its description according to its position. The fact
that dependence in momentum is the Fourier transform of the dependence in
position means that the momentum operator is equivalent (up to an i / ℏ
{\displaystyle i/\hbar } ![{\\displaystyle i/\\hbar
}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/44a04e1f19b5e7bea2bfa8002a841bf8d1b4e66a)
factor) to taking the derivative according to the position, since in Fourier
analysis [differentiation corresponds to multiplication in the dual
space](/wiki/Fourier\_transform#Differentiation "Fourier transform"). This is
why in quantum equations in position space, the momentum p i {\displaystyle
p\_{i}} ![{\\displaystyle
p\_{i}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/5bab39399bf5424f25d957cdc57c84a0622626d2)
is replaced by − i ℏ ∂ ∂ x {\displaystyle -i\hbar {\frac {\partial }{\partial
x}}} ![{\\displaystyle -i\\hbar {\\frac {\\partial }{\\partial
x}}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/ab7fffcee704fc55eb36b137e0cc25132b5dc1bf),
and in particular in the [non-relativistic Schrödinger equation in position
space](/wiki/Schr%C3%B6dinger\_equation#Equation "Schrödinger equation") the
momentum-squared term is replaced with a Laplacian times − ℏ 2 {\displaystyle
-\hbar ^{2}} ![{\\displaystyle -\\hbar
^{2}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/185934c9e69984a0905432abe63d3b41741342b4).[25]
