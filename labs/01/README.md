# Lab 1: Rock Paper Scissors

## Idea

In this lab, we will create a simple game of Rock Paper Scissors against a computer. The program will ask the user to enter either "rock", "paper", or "scissors". The computer will then randomly choose one of the three options. The program will then print out the result of the game.

## Hints/General Instructions

Here are some hints to get you started:

- Generate a random number between 1 and 3 for the computer's choice, where 1 represents Rock, 2 represents Paper, and 3 represents Scissors
- Store this number in a variable called `cpu`
- Ask the user for their input next, store this value in a variable called `user`
- Check what the user chose
- Given what the user chose, check what the computer chose
- Print out the result of the game
- Use nested conditional statements to check for multiple conditions at the same time.

## Example Outputs
  
```bash
Enter rock, paper, or scissors: rock

You chose rock.

The computer chose scissors.

You win!
```

```bash
Enter rock, paper, or scissors: paper

You chose paper.

The computer chose paper.

It's a tie!
```

```bash
Enter rock, paper, or scissors: scissors

You chose scissors.

The computer chose rock.

You lose!
```

## Running the program

To run the program, type the following command in the terminal:

```bash
python3 rock_paper_scissors.py
```

*Note: If you're using Windows, you may need to use `python` instead of `python3`.*

## Submission

Push your code to GitHub and submit the link to your repository on Canvas. Make sure you push your code to the `main` branch of your repository.
