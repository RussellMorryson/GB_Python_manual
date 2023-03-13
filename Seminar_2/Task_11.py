# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

number = int(input("Введите число: "))

# 0 1 1 2 3 5 8 13 21 34
# 1 2 3 4 5 6 7  8  9 10

fibo = 0
fibo_0 = 0
fibo_1 = 1

count = 2

find_number = 0

while fibo <= number:
    if fibo == number:
        find_number += 1
        break
    else:
        fibo = fibo_0 + fibo_1
        fibo_0 = fibo_1
        fibo_1 = fibo
        count += 1
        continue

if find_number == 0:
    print("-1")
else:
    print(count)
