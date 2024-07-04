def howmanysmallerthanme(arr, x): 
    l=0                         
    r = len(arr) - 1
    mid = (l+r) //2 

    if x > arr[0]:
       return len(arr)
    if x<=arr[len(arr)-1]:
        return 0
    while l<=r :
        mid = (l+r)//2 
        if arr[mid] >= x and arr[mid+1] < x: 
            return len(arr)-mid-1
        elif arr[mid] < x :
            r = mid - 1
        else :
            l=mid+1

def smaller(arr):
    x=len(arr)
    arr_r=[0 for i in range(x)]
    for i in range(len(arr)-1):
        counter=0
        arr2=[0 for i in range(x-i-1)]
        for j in range(x-1-i):
            arr2[j]=arr[i+j+1] 
        arr2.sort(reverse = True) 
        counter=howmanysmallerthanme(arr2,arr[i])
        arr_r[i]=counter
    return arr_r
print(smaller([1, 2, 0])) #1 1 0
print(smaller([5, 4, 3, 2, 1])) # 4, 3, 2, 1, 0

sorted_array = list(range(1, 120001))
print(smaller(sorted_array)) 
