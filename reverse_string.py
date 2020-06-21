from stack import Stack

def reverse_string(word):
    s = Stack()
    reverse_word = ""
    for i in range(len(word)):
        s.push(word[i])
    while not s.is_empty():
        reverse_word += s.pop()
    
    return reverse_word

print(reverse_string("abcde"))

    
