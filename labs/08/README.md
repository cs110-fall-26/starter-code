# Lab 8: Command Line Arguments Practice

In today's lab, we're going to practice working with Command Line Arguments to read different files, passing in different "flags" into our program, check for these flags, and changing the behavior of our program based on these flags. 

## Count.py

In `count.py`, implement the `main` function to check for command line arguments using `sys.argv`. This will give a list of arguments. It may be good to print out the arguments when you run the code to see how it behaves. The main should check if there are enough arguments (at least 2). If there aren't, print out a message informing the user that there aren't enough arguments. if there are enough, take the filename from the argument and pass it into the `read_file` function. Take the contents returned from `read_file` and pass those into `get_word_count` to get the word count dictionary. Lastly, print out the most common word found from passing the `word_count` returned from `get_word_count` into `most_common_word`.

## Add.py

1. In `add.py`, start by implementing `convert_to_nums`. This will take in the `arguments` from the command line arguments as a parameter. Convert each value into a `float`. If the value cannot be casted into a `float`, ignore that value, and keep going. If the value can be casted into a float, append the value to the list of numbers. Return the list of numbers at the end of this function.

HINT: Use a try-except here, excepting the `ValueError`.

2. Next, go down to the `add` function. This should take in the list of numbers, iterate through it, and return the sum of all of the numbers.

3. Lastly, implement the `main` function. This should get the command line arguments using `sys.argv`, then pass those arguments into `convert_to_nums`, which then takes the numbers and passes the numbers into the `add` function. At the end, print out the sum of all the numbers passed in.

Notes:

- This should work if no numbers were passed in and this should also work for non-numeric values, ignoring those values if need be.

### Example

```bash
python3 add.py 1 1 2 3.0
Sum: 7.0

python3 add.py
Sum: 0.0

python3 add.py 1 2 3 hello 4 5 6
Sum: 21.0
```

## Leet.py

### Context

Flags are one of the major uses for command line arguments. These are often arguments with "-" or "--" before the argument to signify that the value is a flag. These flags usual inform the program that the program should include or exclude certain parts. For example, this can be used to inform a program to use a given file for input and a certain value for output instead of assuming the values based on the index of the argument.

We will use this concept in this file to take in a file, read the contents, then convert each word into Leetspeak. We will check if the user enters a "-i" flag and a corresponding file to read. If the user enters a "-o" flag and a corresponding file, we will write the contents out. If no "-i" flag is given, we will ask the user to enter their words through an input. The reading and writing functions have already been written for you.

The idea of LeetSpeak is to convert each letter into a different character that looks like it. This was popular in 90s and early 2000s. So, let's write some code for this!

### Instructions

1. In `leet.py`, there are a few functions that are already written for you. Go down to `convert_word` and begin implementing this function. The idea of this function is to convert the given word into it's leet equivalent. Iterate through the word, call `get_leet_equivalent` with each character, take that character, and append it into a new word. The end result of `convert_word` should take a word like "hello" into "#3|_|_0".

2. One thing to note is that each character in `get_leet_equivalent` must be uppercase. So, when you convert the letter, make sure the letter is converted to its uppercase equivalent first.

3. Once the function `convert_word` is completed, move down to the `main` function. This will take up most of this lab. Check if there are more than 2 command line arguments. If there are, then there could be an `-i` or `-o` flag. Start by checking if "-i" is in the list of arguments. If the "-i" flag is present, it means the user wants to read in the input from a file. If this is the case, check if the following argument is a file name. If the next argument isn't a file name, or doesn't exist (meaning "-i" is the last argument), then print out to the user that there isn't a valid input file.

HINT: You may use "sys.argv.index(value)" to get the index of a value.

4. If the user inputs a valid input file as the following argument after "-i", take the argument and save it in a variable to use later. Inform the user that the input file will be used.
5. Next, check if an output file is desired by checking if "-o" is in the list of arguments. If it is, make the same checks as you did in step 3. If the output flag is valid with a valid filename after, save that file name in a variable.

6. Next, if no input file was specified, inform the user that the program will default to using user input for the words. Next, call `get_inputs()` and store the returned `contents` from the function into its own `contents` variable in the main. This will allow us to convert the values later.

7. If an input file was specified, get the contents by calling `read_file()` with the input file name as the argument. Store the contents returned from `read_file` into its own `contents` variable in the main.

8. Next, call `convert_contents(contents)` and store that back into `contents`. This calls your `convert_word` function from step 1 and converts all of the words in the list of contents provided.

9. Next, check if the output file was specific. If no output file was speciied, simply print out the converted contents.

10. If an output file was specified, call the `write_file` with the converted contents and the filename given by the output file flag. This will output the contents into the file. End by informing the user that the contents were written to the output file.

