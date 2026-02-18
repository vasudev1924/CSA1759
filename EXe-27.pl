% -------- Graph --------
edge(a,b).
edge(a,c).
edge(b,d).
edge(c,e).
edge(e,f).

% -------- Heuristic Values (Smaller = Better) --------
h(a,5).
h(b,4).
h(c,2).
h(d,6).
h(e,1).
h(f,0).   % Goal node

% -------- Best First Search --------
best_first(Start, Goal, Path) :-
    bfs(Start, Goal, [Start], RevPath),
    reverse(RevPath, Path).

% If current node is goal
bfs(Goal, Goal, Visited, Visited).

% Otherwise expand best child
bfs(Current, Goal, Visited, Path) :-
    findall(Next,
           (edge(Current,Next),
            \+ member(Next,Visited)),
           Children),
    choose_best(Children, Best),
    bfs(Best, Goal, [Best|Visited], Path).

% Choose node with minimum heuristic value
choose_best([X], X).
choose_best([X,Y|T], Best) :-
    h(X,H1),
    h(Y,H2),
    (H1 =< H2 ->
        choose_best([X|T], Best)
    ;
        choose_best([Y|T], Best)
    ).
