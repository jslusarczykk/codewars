def dectobin(number):
    s = ""
    while number != 0:
        s += str(number % 2)
        number = number // 2  # Use integer division to get the floor value
    s = s[::-1]
    return s
        

def count_bits(n):
    if n == 0 :
        return 0
    sum=0
    x=dectobin(n)
    for i in range(len(x)):
        if x[i]=="1":
            sum+=1
    return sum