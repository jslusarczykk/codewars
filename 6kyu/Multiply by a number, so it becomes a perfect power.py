#fix the code by modyfying the algorythm
import math
def mul_power(n, k):
    arr=[i**k for i in range(1,1000000)]
    for j in range(1,1000000):
        if j*n in arr :
            return j
    return 0
print(mul_power(27,2)) #0
print(mul_power(100, 3)) #10
print(mul_power(36, 2)) #1
print(mul_power(72, 4)) #18
print(mul_power(1152, 3)) #12
#print(int((1152)**0.5))