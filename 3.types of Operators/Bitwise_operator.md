# Bitwise Operators in Python
![Logo](https://imgs.search.brave.com/Bi1e0JNhLnupMI7tBZDSfzsagJ46dFmsT6hrk27DZPM/rs:fit:860:0:0/g:ce/aHR0cHM6Ly90ZWNo/dmlkdmFuLmNvbS90/dXRvcmlhbHMvd3At/Y29udGVudC91cGxv/YWRzL3NpdGVzLzIv/MjAxOS8xMi9QeXRo/b24tQml0d2lzZS1P/cGVyYXRvcnMuanBn)

- Bitwise operators are used to perform operations on binary representations of integers. They work by manipulating bits (0s and 1s) at the binary level.
    
    - ## 1.Bitwise AND (&) Operator
       The bitwise AND operator ('&') returns 1 if both corresponding bits are 1; otherwise, it returns 0.
    
        ### Syntax:
          result = operand1 & operand2
    
        ### Example:
         ```bash
         a = 10  # Binary: 1010
         b = 5   # Binary: 0101
         result_and = a & b  # Result: 0
         ```
        - In this example, the bitwise AND operation on 'a' and 'b' results in 0 because their binary representations have no matching 1 bits in the same positions.
    
    - ## 2.Bitwise OR (|) Operator
       The bitwise OR operator ('|') returns 1 if at least one of the corresponding bits is 1; otherwise, it returns 0.
    
        ### Syntax:
          result = operand1 | operand2
    
        ### Example:
         ```bash
         a = 10  # Binary: 1010
         b = 5   # Binary: 0101
         result_or = a | b  # Result: 15
         ```
        - In this example, the bitwise OR operation on 'a' and 'b' results in 15 because their binary representations have matching 1 bits in some positions.
    
    - ## 3.Bitwise XOR (^) Operator
       The bitwise XOR operator ('^') returns 1 if the corresponding bits are different; otherwise, it returns 0.
        ### Syntax:
          result = operand1 ^ operand2
    
        ### Example:
         ```bash
         a = 10  # Binary: 1010
         b = 5   # Binary: 0101
         result_xor = a ^ b  # Result: 15
         ``` 
        - In this example, the bitwise XOR operation on 'a' and 'b' results in 15 because their binary representations have different bits in some positions.
    
    - ## 4.Bitwise NOT (~) Operator
       The bitwise NOT operator ('~') inverts all the bits of an integer, turning 0s into 1s and 1s into 0s.
        ### Syntax:
          result = ~operand
    
        ### Example:
         ```bash
         a = 10  # Binary: 1010
         result_not = ~a  # Result: -11
         ``` 
        - In this example, the bitwise NOT operation on 'a' results in -11 because all the bits in the binary representation of 10 are inverted.
    
    - ## 5.Bitwise Left Shift (<<) Operator
       The bitwise left shift operator ('<<') shifts the bits of a number to the left by a specified number of positions.
        ### Syntax:
          result = operand << n
    
        ### Example:
         ```bash
         num = 5  # Binary: 101
         result_left_shift = num << 2  # Result: 20 (Binary: 10100)
         ``` 
        - In this example, the bitwise left shift operation on 'num' shifts its bits two positions to the left, resulting in the binary number 10100, which is equal to 20 in decimal.
    
    
    - ## 6.Bitwise Right Shift (>>) Operator
       The bitwise right shift operator ('>>') shifts the bits of a number to the right by a specified number of positions.
        ### Syntax:
          result = operand >> n
    
        ### Example:
         ```bash
         num = 20  # Binary: 10100
         result_right_shift = num >> 2  # Result: 5 (Binary: 101)
         ``` 
        - In this example, the bitwise right shift operation on num shifts its bits two positions to the right, resulting in the binary number 101, which is equal to 5 in decimal.n