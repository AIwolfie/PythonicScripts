# Logical Operators in Python
![Logo](https://imgs.search.brave.com/zkXB_LXn_lrGD5ZQTr_UYW7ct3QMRIlSVyhcRPZS0w4/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9kYXRh/LWZsYWlyLnRyYWlu/aW5nL2Jsb2dzL3dw/LWNvbnRlbnQvdXBs/b2Fkcy9zaXRlcy8y/LzIwMTcvMTIvUHl0/aG9uLUxvZ2ljYWwt/T3BlcmF0b3ItMDEu/anBn)
    
- Logical operators are used to combine multiple conditions and evaluate them to True or False. Python provides three main logical operators: 'and', 'or', and 'not'.
    
    - ## 1. 'and' Operator
       The 'and' operator returns True if both operands are True, otherwise, it returns False.
    
        ### Syntax:
          operand1 and operand2
    
        ### Example:
         ```python
          x = 5
          y = 10
          result = (x < 10) and (y > 5)  # True because both conditions are True
         ```
    
    - ## 2. 'or' Operator
       The 'or' operator returns True if at least one of the operands is True, otherwise, it returns False.
    
        ### Syntax:
          operand1 or operand2
    
        ### Example:
         ```python
          x = 10
          y = 5
          result = x != y  # True
         ```
    
    - ## 3. 'not' Operator
       The 'not' operator returns the opposite of the operand's value. If the operand is True, not returns False, and vice versa.
        ### Syntax:
          not operand
    
        ### Example:
         ```python
          x = True
    
          result = not x  # False because x is True, and not True is False
         ```
    
    These logical operators are fundamental for creating conditional statements and controlling program flow based on different conditions.