class Heap:
    def __init__(self):
        self.array = []
        self.size = 0

    def insert(self, data):
        self.array.append(data)
        self.size += 1
        cur_indx = self.size - 1

        while(cur_indx != 0):
            parent_indx = (cur_indx - 1)//2
            if(self.array[parent_indx] > self.array[cur_indx]):
                self.array[parent_indx], self.array[cur_indx] = self.array[cur_indx], self.array[parent_indx]
                cur_indx = parent_indx
            else:
                break
    
    def print_heap(self):
        for i in self.array:
            print(i, end=' ')
        print()

    def delete(self):
        self.array[0] = self.array[self.size-1]
        self.array.pop()
        self.size -= 1
        cur_index = 0
        last_index = self.size

        while True:
            left = (cur_index * 2) + 1
            right = (cur_index * 2) + 2

            if(left < last_index and right < last_index):
                if(self.array[left] < self.array[cur_index] and self.array[left] < self.array[right]):
                    self.array[left], self.array[cur_index] = self.array[cur_index], self.array[left]
                    cur_index = left
                elif(self.array[right] < self.array[cur_index] and self.array[right] < self.array[left]):
                    self.array[right], self.array[cur_index] = self.array[cur_index], self.array[right]
                    cur_index = right
                else:
                    break
            elif(left < last_index):
                if(self.array[left] < self.array[cur_index]):
                    self.array[left], self.array[cur_index] = self.array[cur_index], self.array[left]
                    cur_index = left
                else:
                    break
            elif(right < last_index):
                if(self.array[right] < self.array[cur_index]):
                    self.array[right], self.array[cur_index] = self.array[cur_index], self.array[right]
                    cur_index = right
                else:
                    break
            else:
                break

heap = Heap()
heap.insert(100)
heap.insert(200)
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(50)
heap.print_heap()
heap.delete()
heap.print_heap()
