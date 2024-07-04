#3kyu #kod dziala ale nie dla duzych liczb
def f(arr,y):
    from bisect import bisect
    arr.sort()
    count = len(arr) - bisect(arr, y)
    return count
def smaller(arr):
    arr2=[0 for i in range(len(arr))]
    for i in range(len(arr)):
        counter=0
        for j in range(i,len(arr)):
            if(arr[i]>arr[j]): #arr[i] - nasza liczba i potrzebujemy jeszcze arrayu2
                counter+=1
        arr2[i]=counter
    return arr2

print(smaller([1, 2, 0]))
print(smaller([5, 4, 3, 2, 1])) # 4, 3, 2, 1, 0