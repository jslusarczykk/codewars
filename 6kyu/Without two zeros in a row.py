#kata level 6(1) algorytm do numerów, zauwazam fibonacciego, fibonacci +1 i zoptymalizowany algorytm z GPT)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
def zeros(n: int) -> int:
    if n==0:
        return 1
    if n==1:
        return 2
    return fibonacci(n+1)

#print(zeros(7))