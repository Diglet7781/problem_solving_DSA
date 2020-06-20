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