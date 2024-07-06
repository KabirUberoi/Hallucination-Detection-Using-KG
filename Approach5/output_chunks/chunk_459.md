### Mach–Zehnder
interferometer[[edit](/w/index.php?title=Quantum\_mechanics&action=edit&section=12
"Edit section: Mach–Zehnder interferometer")]

[![](//upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Mach-
Zehnder\_interferometer.svg/290px-Mach-
Zehnder\_interferometer.svg.png)](/wiki/File:Mach-
Zehnder\_interferometer.svg)Schematic of a Mach–Zehnder interferometer

The [Mach–Zehnder interferometer](/wiki/Mach%E2%80%93Zehnder\_interferometer
"Mach–Zehnder interferometer") (MZI) illustrates the concepts of superposition
and interference with linear algebra in dimension 2, rather than differential
equations. It can be seen as a simplified version of the double-slit
experiment, but it is of interest in its own right, for example in the
[delayed choice quantum eraser](/wiki/Delayed\_choice\_quantum\_eraser "Delayed
choice quantum eraser"), the [Elitzur–Vaidman bomb
tester](/wiki/Elitzur%E2%80%93Vaidman\_bomb\_tester "Elitzur–Vaidman bomb
tester"), and in studies of quantum entanglement.[35][36]

We can model a photon going through the interferometer by considering that at each point it can be in a superposition of only two paths: the "lower" path which starts from the left, goes straight through both beam splitters, and ends at the top, and the "upper" path which starts from the bottom, goes straight through both beam splitters, and ends at the right. The quantum state of the photon is therefore a vector ψ ∈ C 2 {\displaystyle \psi \in \mathbb {C} ^{2}} ![{\\displaystyle \\psi \\in \\mathbb {C} ^{2}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/a7a51a8280039fc22cd88d90915a952f8e020f47) that is a superposition of the "lower" path ψ l = ( 1 0 ) {\displaystyle \psi \_{l}={\begin{pmatrix}1\\\0\end{pmatrix}}} ![{\\displaystyle \\psi \_{l}={\\begin{pmatrix}1\\\\0\\end{pmatrix}}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/feca39f1f03b4dc63be6f7a7c2060430b1217e2f) and the "upper" path ψ u = ( 0 1 ) {\displaystyle \psi \_{u}={\begin{pmatrix}0\\\1\end{pmatrix}}} ![{\\displaystyle \\psi \_{u}={\\begin{pmatrix}0\\\\1\\end{pmatrix}}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/400e9751fcd7816718398d3892bec2ad26bb4713), that is, ψ = α ψ l + β ψ u {\displaystyle \psi =\alpha \psi \_{l}+\beta \psi \_{u}} ![{\\displaystyle \\psi =\\alpha \\psi \_{l}+\\beta \\psi \_{u}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/fb88364b79f3c611ca2ca1edb5356139bf4e1085) for complex α , β {\displaystyle \alpha ,\beta } ![{\\displaystyle \\alpha ,\\beta }](https://wikimedia.org/api/rest\_v1/media/math/render/svg/e4b46b57cfa0011b643037751809904d915c1b48). In order to respect the postulate that ⟨ ψ , ψ ⟩ = 1 {\displaystyle \langle \psi ,\psi \rangle =1} ![{\\displaystyle \\langle \\psi ,\\psi \\rangle =1}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/7d5758e7a60b4e54bc46e01b0618919c65b787a0) we require that | α | 2 + | β | 2 = 1 {\displaystyle |\alpha |^{2}+|\beta |^{2}=1} ![{\\displaystyle |\\alpha |^{2}+|\\beta |^{2}=1}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/18cd7473cdb894839d10852890517b1fb687c73b). 

Both [beam splitters](/wiki/Beam\_splitter "Beam splitter") are modelled as the
unitary matrix B = 1 2 ( 1 i i 1 ) {\displaystyle B={\frac {1}{\sqrt
{2}}}{\begin{pmatrix}1&i\\\i&1\end{pmatrix}}} ![{\\displaystyle B={\\frac
{1}{\\sqrt
{2}}}{\\begin{pmatrix}1&i\\\\i&1\\end{pmatrix}}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/ddf502efcb65d0cbac5bb8ef1a6f163ac9cf2145),
which means that when a photon meets the beam splitter it will either stay on
the same path with a probability amplitude of 1 / 2 {\displaystyle 1/{\sqrt
{2}}} ![{\\displaystyle 1/{\\sqrt
{2}}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/75a0bbdb60fcb73ac67d9970a5eb0808b87fd37d),
or be reflected to the other path with a probability amplitude of i / 2
{\displaystyle i/{\sqrt {2}}} ![{\\displaystyle i/{\\sqrt
{2}}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/e846b6a5731f3799960a4968399d85bc0b7fb9fd).
The phase shifter on the upper arm is modelled as the unitary matrix P = ( 1
0 0 e i Δ Φ ) {\displaystyle P={\begin{pmatrix}1&0\\\0&e^{i\Delta \Phi
}\end{pmatrix}}} ![{\\displaystyle P={\\begin{pmatrix}1&0\\\\0&e^{i\\Delta
\\Phi
}\\end{pmatrix}}}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/3df9457946dd8035c51a39e0926be9f07c7f0a3e),
which means that if the photon is on the "upper" path it will gain a relative
phase of Δ Φ {\displaystyle \Delta \Phi } ![{\\displaystyle \\Delta \\Phi
}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/20cedb08e6edea3cad9b2829ef67311bbe518dd2),
and it will stay unchanged if it is in the lower path.

A photon that enters the interferometer from the left will then be acted upon
with a beam splitter B {\displaystyle B} ![{\\displaystyle
B}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/47136aad860d145f75f3eed3022df827cee94d7a),
a phase shifter P {\displaystyle P} ![{\\displaystyle
P}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/b4dc73bf40314945ff376bd363916a738548d40a),
and another beam splitter B {\displaystyle B} ![{\\displaystyle
B}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/47136aad860d145f75f3eed3022df827cee94d7a),
and so end up in the state

 B P B ψ l = i e i Δ Φ / 2 ( − sin ⁡ ( Δ Φ / 2 ) cos ⁡ ( Δ Φ / 2 ) ) , {\displaystyle BPB\psi \_{l}=ie^{i\Delta \Phi /2}{\begin{pmatrix}-\sin(\Delta \Phi /2)\\\\\cos(\Delta \Phi /2)\end{pmatrix}},} ![{\\displaystyle BPB\\psi \_{l}=ie^{i\\Delta \\Phi /2}{\\begin{pmatrix}-\\sin\(\\Delta \\Phi /2\)\\\\\\cos\(\\Delta \\Phi /2\)\\end{pmatrix}},}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/7927a94da54f5d57b8accffdb9ad456a1e3b5033)

and the probabilities that it will be detected at the right or at the top are
given respectively by

 p ( u ) = | ⟨ ψ u , B P B ψ l ⟩ | 2 = cos 2 ⁡ Δ Φ 2 , {\displaystyle p(u)=|\langle \psi \_{u},BPB\psi \_{l}\rangle |^{2}=\cos ^{2}{\frac {\Delta \Phi }{2}},} ![{\\displaystyle p\(u\)=|\\langle \\psi \_{u},BPB\\psi \_{l}\\rangle |^{2}=\\cos ^{2}{\\frac {\\Delta \\Phi }{2}},}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/110acb8ee7dc4e309de846470778f4767fe97f8f)
 p ( l ) = | ⟨ ψ l , B P B ψ l ⟩ | 2 = sin 2 ⁡ Δ Φ 2 . {\displaystyle p(l)=|\langle \psi \_{l},BPB\psi \_{l}\rangle |^{2}=\sin ^{2}{\frac {\Delta \Phi }{2}}.} ![{\\displaystyle p\(l\)=|\\langle \\psi \_{l},BPB\\psi \_{l}\\rangle |^{2}=\\sin ^{2}{\\frac {\\Delta \\Phi }{2}}.}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/86880ce53051688a4f591ebfb5183fbae013deee)

One can therefore use the Mach–Zehnder interferometer to estimate the [phase
shift](/wiki/Phase\_\(waves\) "Phase \(waves\)") by estimating these
probabilities.

It is interesting to consider what would happen if the photon were definitely
in either the "lower" or "upper" paths between the beam splitters. This can be
accomplished by blocking one of the paths, or equivalently by removing the
first beam splitter (and feeding the photon from the left or the bottom, as
desired). In both cases, there will be no interference between the paths
anymore, and the probabilities are given by p ( u ) = p ( l ) = 1 / 2
{\displaystyle p(u)=p(l)=1/2} ![{\\displaystyle
p\(u\)=p\(l\)=1/2}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/d2a9b3426984de1a64c07261c3e14b485320fee4),
independently of the phase Δ Φ {\displaystyle \Delta \Phi } ![{\\displaystyle
\\Delta \\Phi
}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/20cedb08e6edea3cad9b2829ef67311bbe518dd2).
From this we can conclude that the photon does not take one path or another
after the first beam splitter, but rather that it is in a genuine quantum
superposition of the two paths.[37]
