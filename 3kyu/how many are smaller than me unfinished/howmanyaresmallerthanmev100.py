def howmanysmallerthanme(arr, x): #przekształcić algorytm tak, aby zamiast tej liczby znajdował dwie liczby między którymi się znajduje 
    l=0                           #how many are smaller than me
    r = len(arr) - 1
    mid = (l+r) //2 

    #while l<=r :
    #    mid = (l+r) // 2
    #    if arr[mid] == x :
    #        return mid
    #    elif arr[mid] > x :
    #        r = mid - 1
    #    else :
    #        l=mid+1
    if x > arr[0]:
       return len(arr)
    if x<=arr[len(arr)-1]:
        return 0
    while l<=r :
        mid = (l+r)//2 #3
        if arr[mid] >= x and arr[mid+1] < x: #jezeli 4 jest <= 7 i 5 > 7 : 
            return len(arr)-mid-1
        elif arr[mid] < x :
            r = mid - 1
        else :
            l=mid+1

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