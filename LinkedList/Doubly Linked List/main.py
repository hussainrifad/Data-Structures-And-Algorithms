from doublyList import DoublyList

myList = DoublyList()
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
        pos = int(input('Pos : '))
        data = int(input('Data : '))
        myList.insert_node(pos, data)
    elif(opt == 2):
        pos = int(input('Pos : '))
        myList.delete_node(pos)
    elif(opt == 3):
        myList.print_list()
    elif(opt == 4):
        pos = int(input('Pos : '))
        myList.print_by_pos(pos)
    elif(opt == 5):
        print('Program closed successfully')
        run = False