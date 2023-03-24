"""Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""


def reverse_func(array):
    reverse = []
    max = 0
    min = 1000
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
        if array[i] < min:
            min = array[i]
    
    for j in range(len(array)):
        if array[j] == max:
            reverse.append(min)
        else:
            reverse.append(array[j])
    return reverse

array_1 = [1, 3, 3, 3, 4]
print(reverse_func(array_1))

array_2 = [2, 5, 5, 4, 3]
print(reverse_func(array_2))
