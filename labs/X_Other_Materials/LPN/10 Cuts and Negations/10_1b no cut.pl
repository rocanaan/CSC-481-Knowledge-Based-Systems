s(X,Y):- q(X,Y).
s(0,0).

q(X,Y):- i(X), j(Y).

i(1).
i(2).

j(1).
j(2).
j(3).

% note: s(2,3) is true, but s(3,2) is false.