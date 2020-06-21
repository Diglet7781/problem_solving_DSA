from stack import Stack

def decimal_to_binary(decimal_number):
    s = Stack()
    binary_number = ""
    while decimal_number >= 1:
        remainder = decimal_number % 2
        s.push(remainder)
        decimal_number = int(decimal_number / 2)
    
    while s.is_empty() != True:
        binary_number += str(s.pop())
    
    return binary_number

print(decimal_to_binary(1000))    
