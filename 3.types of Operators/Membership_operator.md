# Membership Operators in Python
![Logo](https://imgs.search.brave.com/GaCxltUm3kyAtD5bUnKK3UIA11rKwtCiXPjb6Lnf8gY/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9maWxl/cy5yZWFscHl0aG9u/LmNvbS9tZWRpYS9N/ZW1iZXJzaGlwLU9w/ZXJhdG9ycy1pbi1Q/eXRob24taW4tYW5k/LW5vdC1pbl9XYXRl/cm1hcmtlZC5mMjI2/MzUyNDJlOGQuanBn)
    
- Membership operators in Python are used to test whether a value or variable is present in a sequence (like lists, tuples, or strings) or not. There are two membership operators: 'in' and 'not in'.
    
    ## 1. 'in' Operator
    The 'in' operator checks if a value or variable exists in a sequence. It returns 'True' if the value is present and 'False' otherwise.
    
    ### Syntax:
    ```python
    'value in sequence'
    ```
    
    ### Example:
    ```python
    fruits = ['apple', 'banana', 'cherry']
    
    # Check if 'apple' is in the list
    result_in = 'apple' in fruits  # Result: True
    # Check if 'orange' is in the list
    result_not_in = 'orange' in fruits  # Result: False
    ```
    - In the example above, 'apple' in fruits evaluates to 'True' because 'apple' is present in the 'fruits' list, while 'orange' in fruits evaluates to False because 'orange' is not in the list.
    
    ## 2. 'not in' Operator
    The 'not in' operator checks if a value or variable does not exist in a sequence. It returns 'True' if the value is not present and 'False' otherwise.
    
    ### Syntax:
    ```python
    'value not in sequence'
    ```
    
    ### Example:
    ```python
    # Check if 'orange' is not in the list
    result_not_in = 'orange' not in fruits  # Result: True
    
    # Check if 'apple' is not in the list
    result_in = 'apple' not in fruits  # Result: False
    ```
    - In this case, 'orange' not in fruits evaluates to True because 'orange' is not present in the fruits list, while 'apple' not in fruits evaluates to False because 'apple' is in the list.
    
    Understanding and using membership operators can be very useful when working with collections in Python.
