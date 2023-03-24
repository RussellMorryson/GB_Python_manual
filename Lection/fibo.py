def fibo (n):
    if n in [1,2]:
        return 1
    return fibo(n-1)+fibo(n-2)

list_1 = []
for i in range(1, 10):
    list_1.append((fibo(i)))
print(list_1)