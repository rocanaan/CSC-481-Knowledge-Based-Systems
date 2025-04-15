even_elements([]).
even_elements([_,_|T]):-even_elements(T).