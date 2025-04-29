suspect(a).
suspect(b).
suspect(c).

tall(a).
tall(b).

has_alibi(c).

proven_innocent(X):-has_alibi(X).

potential_killer(X):-suspect(X), \+ proven_innocent(X).

killer_is_tall:- potential_killer(X), \+ tall(X), !, fail.
killer_is_tall:- potential_killer(X).