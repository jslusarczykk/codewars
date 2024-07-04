#3kyu
#kod dziala ale nie dla duzych liczb
#kod mniej bardziej zoptymalizowany XDXDD
def smaller(arr):
    x=len(arr)
    arr_r=[0 for i in range(x)]
    for i in range(len(arr)-1):
        counter=0
        arr2=[0 for i in range(x-i-1)] #tu juz git ale zmiana w len(arr)-1
        for j in range(x-1-i):
            arr2[j]=arr[i+j+1] #tutaj jest git
        arr2.sort(reverse = True) #tutaj jest git
        print(arr2)
        for k in range(x-1-i):
            if arr[i]>arr2[k]:
                counter+=len(arr2)-k
                break
            if arr[i]<arr2[len(arr2)-1]: #nie musi być
                break 
        arr_r[i]=counter
    return arr_r
print(smaller([1, 2, 0]))
print(smaller([5, 4, 3, 2, 1])) # 4, 3, 2, 1, 0

#for j in range(i,len(arr)):
 #           if(arr[i]>arr[j]):
  #              counter+=1
#
'''
arr3=[0 for i in range(len(arr)-i)] #git
        for j in range(len(arr)-i-1): #tutaj cos
            arr3[j]=arr[i+1]
        arr3.sort()
        for j in range(len(arr)-i-1):
            if arr[i]>arr3[j]:
                counter+=len(arr)-i
'''