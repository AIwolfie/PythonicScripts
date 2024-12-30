# Creating Your First Python Program (Hello World)

![Logo](https://imgs.search.brave.com/3qCuZnpr6to5-OovLGHar_44p4yrt4RrXmduQl72AcA/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9jb250/ZW50Lmluc3RydWN0/YWJsZXMuY29tL0ZM/NC83SzBUL0o3UUdM/NjNHL0ZMNDdLMFRK/N1FHTDYzRy5wbmc_/YXV0bz13ZWJwJmZp/dD1ib3VuZHMmZnJh/bWU9MWF1dG89d2Vi/cCZmcmFtZT0xJmhl/aWdodD0zMDA)

## Here's a simple Python program that prints "Hello, World!" to the console:

To deploy this project run

```python
print("Hello, World!")
```
### Explanation:
   - ### 'print':
       This is the Python built-in function used to display output.

   - ### "Hello, World!": 
       This is the text (or string) that we want to print. Strings in Python are enclosed in quotes (either single or double quotes).

### When you run this program, it will output:

```python
Hello, World!
```

## Additional Examples of Using 'print'

### 1.Printing Variables:
```python
name = "Alice"
age = 30
print("Name:", name)
print("Age:", age)
```
- ### 'name = "Alice"':
    This line assigns the string value "Alice" to the variable 'name'. In Python, you can create variables by assigning values to them. Here, 'name' is a variable storing the name "Alice".
- ### 'age = 30':
    This line assigns the integer value 30 to the variable 'age'. Similarly to 'name', 'age' is a variable storing the age 30. Unlike some other programming languages, Python doesn't require you to declare the type of variable explicitly. It dynamically infers the type based on the assigned value.
- ### 'print("Name:", name)': 
    This line uses the 'print' function to display output to the console. The 'print' function takes one or more arguments, separated by commas, and displays them on the console. In this case, it prints the string "Name:" followed by the value of the 'name' variable (which is "Alice").
- ### 'print("Age:", age)': 
    Similarly to the previous 'print' statement, this line prints the string "Age:" followed by the value of the 'age' variable (which is 30).

### When you run this code, it will output:
```python
Name: Alice
Age: 30
```
# 

### 2.Printing Formatted Text:
```python
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}.")
```
- ### 'x = 10':
    This line assigns the integer value 10 to the variable 'x'.
- ### 'y = 20':
    Similarly, this line assigns the integer value 20 to the variable 'y'.
- ### 'print(f"The sum of {x} and {y} is {x + y}.")':
    Here, we use an f-string, denoted by the f prefix before the string. F-strings allow us to embed Python expressions directly inside string literals. Let's break down the f-string:
    - ### "The sum of {x} and {y} is {x + y}.": 
        This is the f-string template. The curly braces '{}' are used to insert variables or expressions within the string.
    - ### '{x} and {y}': 
        These are placeholders for the values of variables 'x' and 'y' in the f-string. When the f-string is evaluated, these placeholders will be replaced by the actual values of 'x' and 'y'.
    - ### '{x + y}':
        This part calculates the sum of 'x' and 'y'. Inside the f-string, you can directly include expressions like '{x + y}' to compute values. 
    
So, when the print statement is executed, it will substitute {x}, {y}, and {x + y} with their respective values and display the result:
```python
The sum of 10 and 20 is 30.
```
This code demonstrates how f-strings can be used to create formatted output that includes variables and expressions within a string. It's a convenient and readable way to generate dynamic content in Python strings.

### 3.Printing Multiple Items:
```python
print("Item 1", "Item 2", "Item 3")
```
This line of code uses the 'print' function to display output to the console. The 'print' function takes one or more arguments, separated by commas, and displays them on the console. In this case, it prints three strings: "Item 1", "Item 2", and "Item 3".
- ### "Item 1":
    This is the first argument to the 'print' function. It is a string literal containing the text "Item 1".
- ### "Item 2":
    Similarly, this is the second argument to the 'print' function and is a string literal containing the text "Item 2".
- ### "Item 3": 
    This is the third argument to the 'print' function and is a string literal containing the text "Item 3".

### When you run this code, it will output:
```python
Item 1 Item 2 Item 3
```
The 'print' function concatenates the strings and separates them by a space by default. So, the output will display all three items ("Item 1", "Item 2", and "Item 3") separated by spaces.

- You can also customize the separator between items using the 'sep' parameter of the 'print' function. For example, 'print("Item 1", "Item 2", "Item 3", sep=", ")' would output:
   ```python
    Item 1, Item 2, Item 3
   ```  


These examples demonstrate the versatility of the 'print' function in Python for displaying various types of output, including text, variables, formatted strings, and more. Feel free to experiment with different combinations to see how 'print' can be used in your Python programs.
   