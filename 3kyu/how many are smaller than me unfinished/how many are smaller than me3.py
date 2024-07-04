def f(arr,y):
    from bisect import bisect
    arr.sort()
    count = len(arr) - bisect(arr, y)
    return count

def howmanyarelargerthanme(arr, x): #przerobić tak aby było how many are smaller than me XD
    l=0
    r = len(arr) - 1
    mid = (l+r) //2 
    if x >= arr[len(arr)-1]:
        return 0
    if x<arr[0]:
        return len(arr)
    while l<=r :
        mid = (l+r)//2 #3
        if arr[mid] <= x and arr[mid+1] > x: #jezeli 4 jest <= 7 i 5 > 7 : 
            return len(arr)-mid-1
        elif arr[mid] > x :
            r = mid - 1
        else :
            l=mid+1

def smaller(arr):
    x=len(arr)
    arr_r=[0 for i in range(x)] #array wynikowy
    for i in range(len(arr)-1): #przechodzimy przez array
        counter=0 #counter resetuje sie dla kadzego arraya
        arr2=[0 for i in range(x-i-1)] #tu juz git ale zmiana w len(arr)-1 #tworzymy tablice pomocniczna arr2(len(arr-1)-i) o dlugosci arrayu wynikowego
        for j in range(x-1-i):
            arr2[j]=arr[i+j+1] #tutaj jest git
        arr2.sort(reverse = True) #tutaj jest git
        print(arr2)
        #w tym miejscu mamy array dla którego sprawdzamy arr[i] czy jest wieksze od arr2[i]
        counter=f(arr,arr[i])
        arr_r[i]=counter
    return arr_r
#print(smaller([1, 2, 0]))
print(smaller([5, 4, 3, 2, 1])) # 4, 3, 2, 1, 0

#for k in range(x-1-i):
#            if arr[i]>arr2[k]:
#                counter+=len(arr2)-k
#                break
#            else if arr[i]>arr2[len(arr2)]: