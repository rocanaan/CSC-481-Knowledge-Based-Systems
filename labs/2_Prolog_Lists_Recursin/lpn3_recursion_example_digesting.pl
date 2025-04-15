is_digesting(X,Y) :- just_ate(X,Y).
is_digesting(X,Y) :-
        just_ate(X,Z),
        is_digesting(Z,Y).

just_ate(mosquito,blood(john)).
just_ate(frog,mosquito).
just_ate(stork,worm).
just_ate(stork,frog).

/*
Example prompts:
is_digesting(stork,mosquito).
is_digesting(X,mosquito).
is_digesting(stork,X).
is_digesting(X,Y).
*/