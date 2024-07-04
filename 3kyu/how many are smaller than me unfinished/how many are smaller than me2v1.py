#3kyu #kod dziala ale nie dla duzych liczb
def smaller(arr):
    arr2=[0 for i in range(len(arr))]
    for i in range(len(arr)):
        counter=0
        for j in range(i,len(arr)):
            if(arr[i]>arr[j]):
                counter+=1
        arr2[i]=counter
    return arr2

print(smaller([1, 2, 0]))
print(smaller([5, 4, 3, 2, 1])) # 4, 3, 2, 1, 0