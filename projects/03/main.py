import json

def strong_password(password):
    if len(password) < 8:
        return False
    hasUpper = False
    hasLower = False
    hasDigit = False
    for char in password:
        if char.isupper():
            hasUpper = True
        elif char.islower():
            hasLower = True
        elif char.isdigit():
            hasDigit = True
    return hasUpper and hasLower and hasDigit

def range_input(prompt, min, max):
    while True:
        try:
            user = int(input(prompt))
            if user < min or user > max:
                    raise TypeError
            return user 
        except ValueError:
            print("Not a number.")
        except TypeError:
            print(f"Out of range, values must be between {min} and {max}")

def encrypt(password, shift):
    encrypted = ""
    for char in password:
        encrypted += chr(ord(char) + shift)
    return encrypted

def load_users():
    # TODO Implement me
    pass

def load_notes():
    # TODO Implement me
    pass

def save_users(users):
    # TODO Implement me 
    pass

def save_notes(notes):
    # TODO Implement me 
    pass

def signup(users, username, password):
    # TODO Implement me
    pass

def login(users, username, password): 
    for stored_user in users:
        stored_username = stored_user
        stored_password = users[stored_user]
        if(stored_username == username):
            if(encrypt(password, 2) == stored_password):
                print("Successfully logged in!")
                return True
    return False

def add_note(notes, title, description, author, labels):
    notes[title] = {
        "title": title,
        "description": description,
        "author": author,
        "labels": labels
    }
    return notes[title]

def remove_note(notes, title):
    if title not in list(notes.keys()):
        return False
    notes.pop(title)
    return True

def view_note(notes, title):
    if title not in list(notes.keys()):
        return None
    note = notes[title]
    note_details = f"Title: {note['title']}\n"
    note_details += f"Description: {note['description']}\n"
    note_details += f"Author: {note['author']}\n"
    note_details += f"Labels: {note['labels']}"
    return note_details

def list_notes(notes):
    for title in list(notes.keys()):
        print(f"- {title}")

def menu():
    print("""
Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program
""")

def main():  
    users = load_users()
    notes = load_notes()
    logged_in = False
    username = ""

    # TODO Implement login or signup logic

    while True:
        menu()
        choice = range_input("Enter your choice: ", 1, 5)
        if(choice == 1):
            title = input("Enter the title of the note: ")
            description = input("Enter the description of the note: ")
            labels = input("Enter the labels; separated by commas: ")
            labels = labels.split(",")
            add_note(notes, title, description, username, labels)
        elif(choice == 2):
            print("Possible notes to remove: ")
            list_notes(notes)
            title = input("Enter the title of the note to remove: ")
            remove_note(notes, title)
        elif(choice == 3):
            print("List of notes to view: ")
            list_notes(notes)
            title = input("Enter the title of the note to view: ")
            print(view_note(notes, title))
        elif(choice == 4):
            list_notes(notes)
        elif(choice == 5):
            save_users(users)
            save_notes(notes)
            return


if __name__ == "__main__":
    main()
