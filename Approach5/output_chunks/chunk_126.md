### Stochastic outcomes (and relation to other
fields)[[edit](/w/index.php?title=Game\_theory&action=edit&section=17 "Edit
section: Stochastic outcomes \(and relation to other fields\)")]

Individual decision problems with stochastic outcomes are sometimes considered
"one-player games". They may be modeled using similar tools within the related
disciplines of [decision theory](/wiki/Decision\_theory "Decision theory"),
[operations research](/wiki/Operations\_research "Operations research"), and
areas of [artificial intelligence](/wiki/Artificial\_intelligence "Artificial
intelligence"), particularly [AI planning](/wiki/AI\_planning "AI planning")
(with uncertainty) and [multi-agent system](/wiki/Multi-agent\_system "Multi-
agent system"). Although these fields may have different motivators, the
mathematics involved are substantially the same, e.g. using [Markov decision
processes](/wiki/Markov\_decision\_process "Markov decision process") (MDP).[41]

Stochastic outcomes can also be modeled in terms of game theory by adding a
randomly acting player who makes "chance moves" ("[moves by
nature](/wiki/Move\_by\_nature "Move by nature")").[42] This player is not
typically considered a third player in what is otherwise a two-player game,
but merely serves to provide a roll of the dice where required by the game.

For some problems, different approaches to modeling stochastic outcomes may
lead to different solutions. For example, the difference in approach between
MDPs and the [minimax solution](/wiki/Minimax "Minimax") is that the latter
considers the worst-case over a set of adversarial moves, rather than
reasoning in expectation about these moves given a fixed probability
distribution. The minimax approach may be advantageous where stochastic models
of uncertainty are not available, but may also be overestimating extremely
unlikely (but costly) events, dramatically swaying the strategy in such
scenarios if it is assumed that an adversary can force such an event to
happen.[43] (See [Black swan theory](/wiki/Black\_swan\_theory "Black swan
theory") for more discussion on this kind of modeling issue, particularly as
it relates to predicting and limiting losses in investment banking.)

General models that include all elements of stochastic outcomes, adversaries,
and partial or noisy observability (of moves by other players) have also been
studied. The "[gold standard](/wiki/Gold\_standard "Gold standard")" is
considered to be partially observable [stochastic game](/wiki/Stochastic\_game
"Stochastic game") (POSG), but few realistic problems are computationally
feasible in POSG representation.[43]
