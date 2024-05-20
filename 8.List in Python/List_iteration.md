# Lists iteration in Python

- In Python, lists are a versatile and widely used data structure that allow you to store and manipulate a collection of items. Iterating over lists is a fundamental skill, enabling you to access, modify, and utilize each element effectively. This document provides an in-depth look at different methods to iterate over lists in Python.

## Table of Contents
- ### 1.Introduction to List Iteration
- ### 2.Using a For Loop
- ### 3.Using a While Loop

## 1.Introduction to List Iteration
- List iteration refers to the process of going through each element in a list, one by one, to perform operations or extract information. Python provides several ways to iterate over lists, each with its own advantages and use cases.

## 2.Using a For Loop
- The for loop is the most common method to iterate over a list. It allows you to access each element in the list directly.

  ```python
  fruits = ['apple', 'banana', 'cherry']

  for fruit in fruits:
      print(fruit)
  ```
  - ### fruits: 
    A list containing three strings.
  - ### for fruit in fruits: 
    Iterates over each element in the list fruits.
  - ### print(fruit): 
    Prints each element of the list.

    ```python
    numbers = [1, 2, 3, 4, 5]
    total = 0

    for number in numbers:
       total += number

    print("Total:", total)
    ```
    numbers: A list of integers.
   - ### total = 0: 
     Initializes a variable to store the sum.
   - ### for number in numbers: 
     Iterates over each element in the list numbers.
   - ### total += number: 
     Adds the current element to total.
   - ### print("Total:", total): 
     Prints the total sum after the loop completes.

## 3.Using a While Loop
- A while loop can also be used to iterate over a list, typically when you need to keep track of the index.

  ```python
  fruits = ['apple', 'banana', 'cherry']
  index = 0

  while index < len(fruits):
      print(fruits[index])
      index += 1
  ```
  - ### fruits: 
    A list containing three strings.
  - ### index = 0: 
    Initializes an index variable to 0.
  - ### while index < len(fruits): 
    Continues looping as long as index is less than the length of the list.
  - ### print(fruits[index]): 
    Prints the element at the current index.
  - ### index += 1: 
    Increments the index by 1.