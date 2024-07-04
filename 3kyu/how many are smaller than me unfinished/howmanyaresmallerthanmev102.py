def wyszukiwanie_binarne(arr, x): #przekształcić algorytm tak, aby zamiast tej liczby znajdował dwie liczby między którymi się znajduje 
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

print(wyszukiwanie_binarne([99, 93, 90, 83, 82, 51, 43, 27, 18, 12], 125))
print(wyszukiwanie_binarne([99, 93, 90, 83, 82, 51, 43, 27, 18, 12], 12))
print(wyszukiwanie_binarne([99, 93, 90, 83, 82, 51, 43, 27, 18, 12], 12))
print(wyszukiwanie_binarne([99, 93, 90, 83, 82, 51, 43, 27, 18, 12], 55))
print(wyszukiwanie_binarne([99, 93, 90, 83, 82, 51, 43, 27, 18, 12], 35))
print(wyszukiwanie_binarne([99, 93, 90, 83, 82, 51, 43, 27, 18, 12], 99)) #9 a nie 10 mniejszych
print(wyszukiwanie_binarne([99, 93, 90, 83, 82, 51, 43, 27, 18, 12], 18))


#print len(arr) - wyszukiwanie binarne