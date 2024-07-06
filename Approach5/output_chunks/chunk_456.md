### Free
particle[[edit](/w/index.php?title=Quantum\_mechanics&action=edit&section=9
"Edit section: Free particle")]

Main article: [Free particle](/wiki/Free\_particle "Free particle")

[![](//upload.wikimedia.org/wikipedia/commons/5/56/Guassian\_Dispersion.gif)](/wiki/File:Guassian\_Dispersion.gif)Position
space probability density of a Gaussian [wave packet](/wiki/Wave\_packet "Wave
packet") moving in one dimension in free space

The simplest example of a quantum system with a position degree of freedom is
a free particle in a single spatial dimension. A free particle is one which is
not subject to external influences, so that its Hamiltonian consists only of
its kinetic energy:

 H = 1 2 m P 2 = − ℏ 2 2 m d 2 d x 2 . {\displaystyle H={\frac {1}{2m}}P^{2}=-{\frac {\hbar ^{2}}{2m}}{\frac {d^{2}}{dx^{2}}}.} ![{\\displaystyle H={\\frac {1}{2m}}P^{2}=-{\\frac {\\hbar ^{2}}{2m}}{\\frac {d^{2}}{dx^{2}}}.}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/084f585ee5c6cd8a34e323a6de7943227128afc3)

The general solution of the Schrödinger equation is given by

 ψ ( x , t ) = 1 2 π ∫ − ∞ ∞ ψ ^ ( k , 0 ) e i ( k x − ℏ k 2 2 m t ) d k , {\displaystyle \psi (x,t)={\frac {1}{\sqrt {2\pi }}}\int \_{-\infty }^{\infty }{\hat {\psi }}(k,0)e^{i(kx-{\frac {\hbar k^{2}}{2m}}t)}\mathrm {d} k,} ![{\\displaystyle \\psi \(x,t\)={\\frac {1}{\\sqrt {2\\pi }}}\\int \_{-\\infty }^{\\infty }{\\hat {\\psi }}\(k,0\)e^{i\(kx-{\\frac {\\hbar k^{2}}{2m}}t\)}\\mathrm {d} k,}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/ef4f021ba945856e3676808b11724109a8a74dad)

which is a superposition of all possible [plane waves](/wiki/Plane\_wave "Plane
wave") e i ( k x − ℏ k 2 2 m t ) {\displaystyle e^{i(kx-{\frac {\hbar
k^{2}}{2m}}t)}} ![{\\displaystyle e^{i\(kx-{\\frac {\\hbar
k^{2}}{2m}}t\)}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/fb4cd9a9984c84a493ce547babcf58e31b04f7e7),
which are eigenstates of the momentum operator with momentum p = ℏ k
{\displaystyle p=\hbar k} ![{\\displaystyle p=\\hbar
k}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/24fee69175538303b28ac54e907baf53d0a58dbf).
The coefficients of the superposition are ψ ^ ( k , 0 ) {\displaystyle {\hat
{\psi }}(k,0)} ![{\\displaystyle {\\hat {\\psi
}}\(k,0\)}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/8b8323c08418da8bc376c6d78b578d4729b927ea),
which is the Fourier transform of the initial quantum state ψ ( x , 0 )
{\displaystyle \psi (x,0)} ![{\\displaystyle \\psi
\(x,0\)}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/55ad442e07ca2d7986ef0787f9129fc325cde137).

It is not possible for the solution to be a single momentum eigenstate, or a
single position eigenstate, as these are not normalizable quantum states.[note
1] Instead, we can consider a Gaussian [wave packet](/wiki/Wave\_packet "Wave
packet"):

 ψ ( x , 0 ) = 1 π a 4 e − x 2 2 a {\displaystyle \psi (x,0)={\frac {1}{\sqrt[{4}]{\pi a}}}e^{-{\frac {x^{2}}{2a}}}} ![{\\displaystyle \\psi \(x,0\)={\\frac {1}{\\sqrt\[{4}\]{\\pi a}}}e^{-{\\frac {x^{2}}{2a}}}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/a4c2dae82312897d5fd4c58986c426a6009e6840)

which has Fourier transform, and therefore momentum distribution

 ψ ^ ( k , 0 ) = a π 4 e − a k 2 2 . {\displaystyle {\hat {\psi }}(k,0)={\sqrt[{4}]{\frac {a}{\pi }}}e^{-{\frac {ak^{2}}{2}}}.} ![{\\displaystyle {\\hat {\\psi }}\(k,0\)={\\sqrt\[{4}\]{\\frac {a}{\\pi }}}e^{-{\\frac {ak^{2}}{2}}}.}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/c4991535bba434314af8c27c16fff74f49ce367e)

We see that as we make a {\displaystyle a} ![{\\displaystyle
a}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/ffd2487510aa438433a2579450ab2b3d557e5edc)
smaller the spread in position gets smaller, but the spread in momentum gets
larger. Conversely, by making a {\displaystyle a} ![{\\displaystyle
a}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/ffd2487510aa438433a2579450ab2b3d557e5edc)
larger we make the spread in momentum smaller, but the spread in position gets
larger. This illustrates the uncertainty principle.

As we let the Gaussian wave packet evolve in time, we see that its center
moves through space at a constant velocity (like a classical particle with no
forces acting on it). However, the wave packet will also spread out as time
progresses, which means that the position becomes more and more uncertain. The
uncertainty in momentum, however, stays constant.[34]
