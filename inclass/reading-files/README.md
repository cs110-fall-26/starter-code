# Files Practice

In today's in-class assignment, we will read a number of files and analyze some information from the files. We will start by finding the most common words from Alice in Wonderland, courtesy of Project Gutenberg. We will then move onto reading sample data about students and classes from a CSV, then end by reading a json file containing Pokemon data. We will read this data and find the stats of a given Generation 1 pokemon then!

## Files

- `gutenberg_alice.txt`: The text file containing the entire book of "Alice in Wonderland"
- `classes.csv`: The csv file containing 1000 generated students, taking different lower-division Computer Science classes with their final grades attached.
- `pokemon.json`: The json file containing the pokemon from Generation 1, pulled from PokeAPI.

## Tasks

### Word\_Count

1. In the `word_count.py` file, we will implement the `read_file` function together as a class. This will take a filename as a parameter. It will open the file, read the contents line by line, strip the new lines at the end of each line, and add them into a list, and return the list at the end.
2. You will then go down to the `get_words` function. This will take the contents returned from the `read_file` function, parse out each word from the list. The `file_contents` should contain the list with each line contained. Iterate through the lines, split the line to get each word.
3. Once you have each word, iterate through those words. Check if the word is in the dictionary `words` already. If it isn't, set the word as the key and set the value to 1. If the word is already in the dictionary, update the count connected to the word by adding 1 to it.

### Analyze\_classes

1. In the `analyze_classes.py` file, we will implement the `read_csv` function together as a class. This will take a filename as a parameter. It will open the file, read the contents, strip the any new lines or spaces at the end, split the contents by ",", then add the line to our list of contents. This should create a 2D list in `contents`. The inner lists will contain each value from the line. We will also check if the word "course" is in the line. If the word "course" is in the line, meaning it's a header line, skip this line and go to the next line. We don't want to include the header line as a value. At the end of this, our contents (for the first two values) should look like:

```python
[["1", "Gabriel", "Gilbert", "CS221", "A"], ["2", "Marc", "Howell", "CS111", "B"]]
```

The order of the inner values goes: [`id`, `first_name`, `last_name`, `course`, `grade`]

2. Go down to the `get_course_performance_average` function. You will implement this function. This function will take in the whole list of `courses` and an individual `course_name` as parameters. Iterate through the courses, check if the value at the `3rd` index of the course is the `course_name`. If the course name matches, convert the grade at the `4th` index using the `convert_grade` function, then append the numeric grade equivalent to the `course_performance` list. `convert_grade` will take the letter grade and provide its numeric equivalent. For example, an `A` is converted to a `4.0`.

3. After iterating through the courses, calculate the average of the course\_performances. At the end, return this average.

4. Next, go down to `get_all_course_averages`. You will also implement this function. This function will take in the list of `courses` and a list of `available_courses`. Iterate through the `availabe_courses`, calculate the course performance of each course using the `get_course_performance_average` function you implemented in steps 2 and 3, and add that average to your dictionary `course_averages`. The key of `course_averages` should be the course name itself with the value being the course average. At the end, return the `course_averages`.

### Pokedex

1. In the `pokedex.py` file, we will implement the `load_pokemon` function together as a class. This will take a filename as a parameter. It will open the file, then use the `json.load` function and load the contents of the file into our `pokemon` list. We will then return the list at the end of this function.

2. Next, move down to the `get_pokemon_ids` function. This is the first of two functions you will implement in this file. Iterate through the `pokemon_list` provided as the parameter. For every pokemon, add to the `pokemon_ids` dictionary. Set the key of the dictionary to the `id` of the pokemon and set the value to the `name` of the pokemon. Get the id by: `pokemon['id']` and get the name by: `pokemon['name']`, where `pokemon` is the current pokemon in the loop.

3. Move down to the `print_valid_pokemon` function. This function simply takes the `pokemon_ids` passed in from the `get_pokemon_ids` function, and prints out the ids and names as a list. With the first three, this should look like:

```bash
Pokemon: 
- 1 bulbasaur
- 2 ivysaur
- 3 venusaur
```

You may use any dictionary function to help you here.

