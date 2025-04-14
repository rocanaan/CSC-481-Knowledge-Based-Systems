rich(X):-soldCompany(X).
rich(X):-inherited(X,Y),rich(Y).

soldCompany(alice).
soldCompany(bob).
soldCompany(charlie).

inherited(dave,alice).