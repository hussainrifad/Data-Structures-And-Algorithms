def printFun(arr, i):
    if(i == 0):
        return arr[i]
    
    arr[i] = printFun(arr, i-1)

arr = [10, 30, 40, 50, 60, 40, 200, 500, 400]
printFun(arr, len(arr)-1)
print(arr)