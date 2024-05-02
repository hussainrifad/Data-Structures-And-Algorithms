from queue import Queue

# main function

myQueue = Queue()

# input 
while True:
    number = int(input())
    if number == -1:
        break
    else:
        myQueue.push(number)

while (myQueue.is_empty() == False):
    print(myQueue.top(), end= ' ')
    myQueue.pop()