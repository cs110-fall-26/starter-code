# Extra Credit 1: Error Reading

In this extra credit assignment, you will read the code, explain the error, and provide a solution. Any code that is suspected of not being your own will automatically be considered an incomplete.

You may write your answers in this README below the question or in separate python files, or separate txt files. You may even write your solutions in a Google doc, then submit the link to your Google doc.

If you're not sure about the problem, make your best assumption about the code. You may also assume all imports have been made before this.

To earn full credit, you must get at least 70 points

## Problems

### Problem 1: 2 pts

```python
x = 1
y == 1
print(x + y)
```

### Problem 2: 2 pts

```python
x = input(int("Enter a number: "))
```

### Problem 3: 4 pts

```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ')
print(first_name - last_name)
```

### Problem 4: 4 pts

```python
num = random.randint(1, 10)
if num % 5:
    print("divisible by 5")
```

### Problem 5: 8 pts

```python
dice = random.randit(1, 6)
coin = random.randit(1, 2)
if dice == 1:
if coin == 1:
    print("Heads and 1 rolled!")
```

### Problem 6: 5 pts

```python
while True:
    if random.randint(1, 6) == 1:
        break
    else:
        print(random.randint(1, 6))
```

### Problem 7: 5 pts

```python
for i in range(-1):
    print(i)
```

### Problem 8: 5 pts

```python
def add(a, b)
return a + b
```

### Problem 9: 10 pts

```python
def sum(list):
    for n in list:
        s += n
    return s
```

### Problem 10: 12 pts

```python
def gen_grid(l, w):
    grid = []
    i = 0
    for row in range(l):
        row = []
        for w in range(w):
            row.append(i)
        grid.append(row)
    return grid
```

### Problem 11: 13 pts

```python
def flip(dict):
    d2 = {}
    for (k,v) in dict:
        d2[v] = k
    return d2 
```

### Problem 12: 15 pts

```python
def read_classes():
    with open("classes.csv", 'r') as f:
        for line in f:
            contents = line
    return contents
```

### Problem 13: 15 pts

```python
try:
   def parse_file(filename):
   with open(filename, 'r') as f:
        return f.load(json)
except FileNotFoundError:
    return "No file found"
```

