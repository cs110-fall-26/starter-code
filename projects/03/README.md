# Project 3

Note Sessions

## Description

In the last project, we added our core functionality, allowing the user to create new notes, read notes, update notes, and delete notes. The user is able to login to the system, courtesy of our functionality from Project 1. We added functions to simplify the code base and make it easier for the user to read the code.

These basic uses are great and all, however, we can't save notes between sessions. When we start our program, all of our notes are gone from the previous session! Let's add some functionality to our system that allows the user to save and load their notes into files.

## New Features

- Read files at the beginning to load users and notes
- Write to files at program exit to save users and notes
- Multiple users can now exist
- A user can create a new account

## Functionality

- The user can create an account now, which will later be stored in a file. If the user chooses to sign up, keep asking the user to enter their password as long as the password is not strong enough. Once the password is strong enough, process the signup.
    - Implement the function to sign the user up.
    - Use the `strong_password` function either here or in the main.
- At the beginning of the program, load in the users into a dictionary
    - Implement the function to load in the users from the `users.json` file.
    - If a JSONDecodeError is thrown, catch it and return an empty dictionary
    - If the file doesn't exist, return an empty dictionary
- After loading in the users, load in the notes into a dictionary
    - Implement the function to load in the notes from the `notes.json` file.
    - If a JSONDecodeError is thrown, catch it and return an empty dictionary
    - Again, if the file doesn't exist, return an empty dictionary
- Once the user chooses to exit the program, save the `users` and `notes` into their respective files.
    - Implement the function to save the users back into `users.json`.
    - Implement the function to save the notes back into `notes.json`.

## Topics

- Data Types
- Variables
- Conditional Statements
- Loops
- Functions
- Lists
- Strings
- Dictionaries
- Exceptions
- Files
- JSON

## General Instructions

1. Implement the `load_users` and `load_notes` functions. These will read the `json` files `users.json` and `notes.json` respectively. They will return the dictionary with the users and notes so that the remainder of the program can use these. You can use `json.load` to help you with these. If the files don't exist, return an empty dictionary. You may have to check for the `FileNotFoundError`. If a `json.JSONDecodeError` is raised, except this and return an empty dictionary too.
2. Next, implement the `save_users` and `save_notes` functions. These will take the users and notes respectively, and write the contents out to a file. Remember, the contents being written into a file must be strings or the program will crash. You can use `json.dumps` to help you with these. If a `json.JSONDecodeError` is raised, except this and return an empty dictionary too.
3. Implement the `signup` function. This function takes in the users, username, and password. It should check if the username is in the dictionary of users already. If it is, return False. If it isn't, it should encrypt the password with a shift of 2, set the username and encrypted password as the key-value pair in the users dictionary. It should then print out a message informing the user that the User was successfully created. Lastly, it should return True.
4. Notice that we now have more login related functions. The login function is the same function from our previous project and we just implemented the signup function. In the main function, ask the user whether they want to signup a new user or login an existing user. The program should keep asking the user until they enter `login` or `signup`. Given the choice from the user, the user should be prompted to input their credentials.
5. If the user chooses to **login**, ask the user for their username and password, then pass those values into the `login` function.
6. If the user chooses to **signup**, ask the user for their username and password. Check if the password is strong enough. If it is not strong enough, ask the user to try again. Once the password is strong enough, pass those values into the `signup` function.
7. Both cases will return True if the signup or login was successful, False otherwise. If they succeeded, set `logged_in` to True.
8. Check if the user failed to log in. If they failed, inform the user that the authentication failed and end the program.
9. If the authentication went smoothly, the program should now run correctly, as it also should be loading data from the `json` files.

## Example Output

```bash

$ python3 main.py # first run

Log in or Create an account? Enter [login] or [signup]: login
Username: edward
Password: password
Successfully logged in!

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 1
Enter the title of the note: Project 3
Enter the description of the note: Work on project 3
Enter the labels; separated by commas: school,cs

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 4
- Hello
- Project 3

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 3
List of notes to view: 
- Hello
- Project 3

Enter the title of the note to view: Project 3

Title: Project 3
Description: Work on project 3
Author: edward
Labels: ['school', 'cs']

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 1
Enter the title of the note: Work on the In class
Enter the description of the note: in class assignment
Enter the labels; separated by commas: school,cs

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 4
- Hello
- Project 3
- Work on the In class

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 2
Possible notes to remove: 
- Hello
- Project 3
- Work on the In class
Enter the title of the note to remove: Work on the In class

Options:
0. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 4
- Hello
- Project 3

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 5

$ python3 main.py # Next run

Log in or Create an account? Enter [login] or [signup]: login
Username: edward
Password: password
Successfully logged in!

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 4
- Hello
- Project 3

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 5
```

| Grade   | Requirements |
|--------------- | --------------- |
| A+ | <ul><li>Everything from A</li><li>Signup protections added; no repeated username</li><li>Signing up a new user requires the user to enter a strong password.</li><li>At least 2 fields added to the note</li></ul> |
| A | <ul><li>Everything from B</li><li>No errors</li><li>Possible errors handled with error handling</li></ul> |
| B | <ul><li>Everything from C</li><li>Save functions implemented correctly</li><li>Minimal errors</li><li>Login and Signup functionality correctly implemented in the main</li></ul> |
| C | <ul><li>Reflection completed</li><li>Signup behaves correctly</li><li>load functions implemented correctly</li><li>Some errors, but code executes with minimal fixes</li></ul> |
| D | <ul><li>Attempt made</li><li>Reflection started</li></ul> |
| F | No attempt made |

