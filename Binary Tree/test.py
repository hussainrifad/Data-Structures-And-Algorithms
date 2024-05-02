queue = []
queue.append(10)
queue.append(20)
queue.append(40)
queue.append(50)

queue.pop(0)
for i in range(0, len(queue)):
    print(i, queue[i])

print()

queue.pop(0)
for i in range(0, len(queue)):
    print(i, queue[i])
    