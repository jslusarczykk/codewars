#7
def without_last(lst):
    lst2=[]
    for i in range(len(lst)-1):
        lst2+=[lst[i]]
    return lst2