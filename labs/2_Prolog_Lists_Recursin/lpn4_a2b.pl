a2b([],[]).
a2b([a|Ta],[b|Tb]) :- a2b(Ta,Tb).

/*
Sample queries:
a2b([],[]).
a2b([a],[b]).
a2b([a,a,a,a],[b,b,b,b]).
a2b([a,a,a,a],[b,b,b]).
a2b([a,a],[b,b,b,b]).
a2b(A,[b,b,b,b]).
a2b([a,a,a,a],B).
a2b(A,B).
*/



