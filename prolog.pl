% Define addition
add(X, Y, Z) :-
    Z is X + Y.

% Define subtraction
subtract(X, Y, Z) :-
    Z is X - Y.

% Define multiplication
multiply(X, Y, Z) :-
    Z is X * Y.

% Define division
divide(X, Y, Z) :-
    Y =\= 0,
    Z is X / Y.
