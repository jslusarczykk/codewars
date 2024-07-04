def pipi(n: int) -> int:
    #próbuje wyznaczyc pipi(4)
    #miliardy rekurencji XDXDXD
    wynik=n
    if n == 0:
        return 0
    if n==1:
        return 1
    return pipi(n+1)*pipi(n+1)-pipi(n)
        
print(pipi(3))