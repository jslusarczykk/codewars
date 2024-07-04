def sum_array(a):
    sum=0
    if len(a) == 0 :
        return sum
    else:
        for i in range(len(a)):
            sum+=a[i]
        return sum
