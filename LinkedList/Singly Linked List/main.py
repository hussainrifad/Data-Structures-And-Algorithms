from singlyList import SinglyList

myList = SinglyList()
run = True

while run:
    print('____________main____________')
    print('1. Insert node')
    print('2. Delete node')
    print('3. Print list')
    print('4. View node data')
    print('5. Exit')

    opt = int(input('Option : '))
    if(opt == 1):
        # if we insert at 0th and nth position time complexity will be O(1)
        # in between time complexity will be O(n)
        pos = int(input('Pos : '))
        data = int(input('Data : '))
        myList.insert_node(pos, data)
    elif(opt == 2):
        # in deletion at 0th index time complexity is O(1)
        # but for rest it would be O(n)
        pos = int(input('Pos : '))
        myList.delete_node(pos)
    elif(opt == 3):
        # time complexity is O(n)
        myList.printList()
    elif(opt == 4):
        # time complexity is O(n)
        pos = int(input('Pos : '))
        myList.print_data_in_pos(pos)
    elif(opt == 5):
        run = False