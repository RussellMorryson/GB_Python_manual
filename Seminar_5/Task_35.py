"""Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes"""

def func(n):
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False
    return result

print("Программа для проверки является ли введенное число простым")
number = int(input("Введите число: "))
if func(number):
    print("yes")
else:
    print("no")