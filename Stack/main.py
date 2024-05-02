from stack import Stack

# main function
myStack = Stack()

# input 
while True:
    number = int(input())
    if number == -1:
        break
    else:
        myStack.push(number)

print 
while (myStack.is_empty() == False):
    print(myStack.top(), end= ' ')
    myStack.pop()