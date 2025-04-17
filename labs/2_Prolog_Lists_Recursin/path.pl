edge(a,b).
edge(b,c).
edge(c,d).
edge(c,e).
edge(d,g).
edge(e,f).
edge(f,g).

neighbor(X,Y):-edge(X,Y).
neighbor(X,Y):-edge(Y,X). 
%note: writing edge(X,Y):-edge(Y,X) would lead to endless loop

%use the predicate below to test if an edge [A,B] has been visited.
%note that [A,B] denotes a list with exactly 2 elements, since we are not using the | operator
newedge([A,B],Edges):-not(member([A,B],Edges)),not(member([B,A],Edges)).


%Write a predicate path(X,Y,E,P) that stores the path from X to Y while not using any edge already in E
%Hint: the base case should be: there is a path from every node to itself, the path is a list with the node as its only element, and the list E does not matter for the base case
