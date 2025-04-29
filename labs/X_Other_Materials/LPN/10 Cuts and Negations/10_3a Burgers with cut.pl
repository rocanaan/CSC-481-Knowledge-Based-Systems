enjoys(vincent,X) :- burger(X), not_big_kahuna_burger(X).

not_big_kahuna_burger(X):-big_kahuna_burger(X),!,fail.
not_big_kahuna_burger(X).

burger(X) :- big_mac(X).
burger(X) :- big_kahuna_burger(X).
burger(X) :- whopper(X).

big_mac(a).
big_kahuna_burger(b).
big_mac(c).
whopper(d).