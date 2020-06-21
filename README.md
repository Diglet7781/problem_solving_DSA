# problem_solving_DSA
This repository has been created to track my Data structure and algorithm problem solving skills
```
1. balanced parenthesis
    # In this problem, we need to solve a problem to check if the given set of parenthesis is balanced or not
    This problem can be solved with the use of stack datastructure
    Here, we first create a stack and loop through the given list to be checked if it is balanced or not
    we check the each char in the list 
    if the char is in opening set of char "{([" then we push the current char to stack
    if the char is not in the opening set of char then we check if the stack is empty or not ( we do this for the edge case such as ")}") 
    if the stack is empty we know that the list of paren is not balanced
    if the stack is not empty, we check the top of the stack and the current char from the list and check if they match "(",")" or "{","}" or "[","]"
    if the top of stack and current char matches as a pair , we pop out a char from stack
    if it does not match, we know the list is not balanced
    Once we go through all the char in the list, we check if the stack is empty or not
    if stack is empty , we know the given list was a balanced set of parenthesis
    if not , the given list was not a balanced set of parenthesis
```

```
2. convert decimal to binary number 
    # In this problem, we make the use of Stack data structure to convert a decimal number to binary
    Here, first we create a stack and a empty string to store the binary number
    In this problem, we push the remainder of decimal_number / 2  in the stack
    Therefore, we run a loop until the decimal_number is >=1 
        get the remainder for decimal_number / 2 (decimal_number % 2)  and push it into the stack
        divide the decimal_number by 2 and keep the integer value i.e decimal_number = int(decimal_number / 2)
    once, we finish storing all the remainder into the stack
    we now wil do pop operation on stack and concatenate the top of the stack to string binary number until the stack gets empty
    finally , return the binary number in string

```

```
3. reverse a string
    # In this problem, we make the use of Stack data structure to reverse the string
    Here, first we create a empty stack  and a reverse_string variable 
    we go through the all the charcters in the string and push all of them to stack one at a time
    The next step is to loop through the stack, pop the char from stack and append that char to reverse_string until the stack gets empty
    Finally, return the reverse_string
```