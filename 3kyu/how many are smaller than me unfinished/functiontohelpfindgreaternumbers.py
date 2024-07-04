from bisect import bisect
def f(arr,y):
    from bisect import bisect
    arr.sort()
    count = len(arr) - bisect(arr, y)
    return count
print(bisect([2,1,3],2))


arr=[2,3,2,1,3,5,6,2,3,6,2,6,4]
y=4
print(f"The numbers greater than {y} : " + str(f(arr,y)))
