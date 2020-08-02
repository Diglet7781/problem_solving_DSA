
from stack import Stack

def is_match(stack_top,current_char):
    if stack_top == "(" and current_char == ")":
        return True
    elif stack_top == "{" and current_char == "}":
        return True
    elif stack_top == "[" and current_char == "]":
        return True
    else:
        return False


def balance_paren(paren):
    s = Stack()
    index = 0
    balanced = True
    while index < len(paren) and balanced:
        if paren[index] in "({[":
            s.push(paren[index])
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.peek()
                if is_match(top,paren[index]):
                    s.pop()
                else:
                    balanced = False
        index += 1
    if s.is_empty():
        return True
    else:
        return False



print((balance_paren("((((({[(]})))))")))


