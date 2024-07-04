def wyszukiwanie_binarne(arr, x): #how many are larger than me #przerobić dla tablicy malejącej
    l=0
    r = len(arr) - 1
    mid = (l+r) //2 

    #while l<=r :
    #    mid = (l+r) // 2
    #    if arr[mid] == x :
    #        return mid
    #    elif arr[mid] > x :
    #        r = mid - 1
    #    else :
    #        l=mid+1 #to działa tego nie ruszamy
    if x >= arr[len(arr)-1]:
        return len(arr)
    if x<=arr[0]:
        return 0
    while l<=r :
        mid = (l+r)//2 #3
        if arr[mid] <= x and arr[mid+1] > x: #jezeli 4 jest <= 7 i 5 > 7 : 
            return len(arr)-mid-1
        elif arr[mid] > x :
            r = mid - 1
        else :
            l=mid+1

#print(wyszukiwanie_binarne([1,2,3,4,5,6,8,9],7))
#print(wyszukiwanie_binarne([1,2,3,4,5,6,8,9],6))
#print(wyszukiwanie_binarne([1,2,3,4,5,6,8,9],1))
#print(wyszukiwanie_binarne([1,2,3,4,5,6,8,9],9))
#print(wyszukiwanie_binarne([1,2,3,4,5,6,8,9],3))
#print(wyszukiwanie_binarne([1,2,3,4,5,6,8,9],5))
print(wyszukiwanie_binarne([12,18,27,43,51,82,83,90,93,99],125))
print(wyszukiwanie_binarne([12,18,27,43,51,82,83,90,93,99],5))
print(wyszukiwanie_binarne([12,18,27,43,51,82,83,90,93,99],12))
print(wyszukiwanie_binarne([12,18,27,43,51,82,83,90,93,99],55))
print(wyszukiwanie_binarne([12,18,27,43,51,82,83,90,93,99],35))

#print(wyszukiwanie_binarne([99, 93, 90, 83, 82, 51, 43, 27, 18, 12], 125))
#print(wyszukiwanie_binarne([99, 93, 90, 83, 82, 51, 43, 27, 18, 12], 12))
#print(wyszukiwanie_binarne([99, 93, 90, 83, 82, 51, 43, 27, 18, 12], 12))
#print(wyszukiwanie_binarne([99, 93, 90, 83, 82, 51, 43, 27, 18, 12], 55))
#print(wyszukiwanie_binarne([99, 93, 90, 83, 82, 51, 43, 27, 18, 12], 35))

#smaller([5, 4, 3, 2, 1]) === [4, 3, 2, 1, 0]
#smaller([1, 2, 0]) === [1, 1, 0]