N = [_ for _ in range(1,11)]
k = int(input("Введите k:\n"))
result = k % len(N)
print(N[-result:] + N[:-result])