# Tic Tac Toe

Today, we will create the game of tic tac toe in class applying the concepts of a 2D List. We will implement a number of functions, before combining them into our main function at the bottom. The game will be played between two players running on the same computer. Before each round, the board will be printed again.

## Instructions

1. Start by implementing the `setup` function. This will turn the board as an empty list into a 2D list that contains the following. This will return the board at the end of the function. 
```python
[
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]
```

2. Next, implement the `can_mark` function. This will check if a row and column has already been marked. This can simply check if the value at that row and column is still an "_" or if it has changed. This function should return `True` if the position hasn't been marked yet, or `False` if it has.

3. We will then move onto the `mark_pos` function. This will take the board, a row, a column, and the marker to mark that position. This will also assume that the `can_mark` function has been called before this. We could include it in this function, but our `main` function will include the check first.

4. Next, implement each of the win condition checks. These should return the winner "x" or "o" depending on who won, or `None` if no winners have been found yet. 

5. Check for ties at the end. This should check if no available spots are left and a player hasn't won in any of the other cases yet.

6. Once you've written all of these, start calling these functions in the `main` function. 

