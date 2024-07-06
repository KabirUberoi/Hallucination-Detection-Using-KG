##
Applications[[edit](/w/index.php?title=Implication\_graph&action=edit&section=1
"Edit section: Applications")]

A [2-satisfiability](/wiki/2-satisfiability "2-satisfiability") instance in
[conjunctive normal form](/wiki/Conjunctive\_normal\_form "Conjunctive normal
form") can be transformed into an implication graph by replacing each of its
[disjunctions](/wiki/Disjunction "Disjunction") by a pair of implications. For
example, the statement ( x 0 ∨ x 1 ) {\displaystyle (x\_{0}\lor x\_{1})}
![{\\displaystyle \(x\_{0}\\lor
x\_{1}\)}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/7fd9ba255774770c73022245dc42855f87f1403b)
can be rewritten as the pair ( ¬ x 0 -> x 1 ) , ( ¬ x 1 -> x 0 )
{\displaystyle (\neg x\_{0}\rightarrow x\_{1}),(\neg x\_{1}\rightarrow x\_{0})}
![{\\displaystyle \(\\neg x\_{0}\\rightarrow x\_{1}\),\(\\neg x\_{1}\\rightarrow
x\_{0}\)}](https://wikimedia.org/api/rest\_v1/media/math/render/svg/73525b090007d4ea7908ec4be1974cb72762198b).
An instance is satisfiable [if and only if](/wiki/If\_and\_only\_if "If and only
if") no literal and its [negation](/wiki/Negation "Negation") belong to the
same [strongly connected component](/wiki/Strongly\_connected\_component
"Strongly connected component") of its implication graph; this
characterization can be used to solve 2-satisfiability instances in [linear
time](/wiki/Linear\_time "Linear time").[1]

In [CDCL](/wiki/CDCL "CDCL") [SAT](/wiki/Boolean\_satisfiability\_problem
"Boolean satisfiability problem")-solvers, [unit
propagation](/wiki/Unit\_propagation "Unit propagation") can be naturally
associated with an implication graph that captures all possible ways of
deriving all implied literals from decision literals,[2] which is then used
for clause learning.
