# Identity Operators in Python
![Logo](https://imgs.search.brave.com/nxgQXnMgU5UQfUlJnnZKfCg-u0r0Kj8v6luCXa66NxY/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9saW51/eHdheXMubmV0L3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIyLzAz/L0lkZW50aXR5X09w/ZXJhdG9yc19pbl9Q/eXRob24xLmpwZw)
    
- Identity operators are used to compare the memory location of two objects.
    
    ## 1. 'is' Operator
    The 'is' operator checks if two variables refer to the same object in memory. Returns True if object1 and object2 point to the same object in memory; otherwise, returns False.
    
    ### Syntax:
    \object1 is object2\
    
    ### Example:
    ```python
    x = [1, 2, 3]
    y = [1, 2, 3]
    z = x
    
    print(x is y)  # Output: False
    print(x is z)  # Output: True
    ```
    
    ## 2. 'is not' Operator
    The is not operator checks if two variables do not refer to the same object in memory. Returns True if object1 and object2 do not point to the same object in memory; otherwise, returns False.
    
    ### Syntax:
    \object1 is not object2\
    
    ### Example:
    ```python
    x = [1, 2, 3]
    y = [1, 2, 3]
    z = x
    
    print(x is not y)  # Output: True
    print(x is not z)  # Output: False
    ```
    
    Understanding and using identity operators is essential when dealing with object comparisons and memory management in Python.
