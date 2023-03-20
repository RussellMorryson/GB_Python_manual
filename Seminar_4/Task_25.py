"""Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()"""


array = 'a a a b c a a d c d d'
array = array.split(' ')

letter_arr = {'0'}
letter_array = []
number_arr = []
fatal_array = []
for i in array:
    letter_arr.add(i)
letter_arr.remove('0')
print(letter_arr)

for j in range(len(letter_arr)):
    number_arr.append(0)

for j in letter_arr:
    letter_array.append(j)

fatal = ''
u = 0
for k in array:
    while u < len(letter_array):
        if k == letter_array[u]:
            number_arr[u] = number_arr[u] + 1
            break
        u = u + 1    
    if number_arr[u] == 1:
        fatal = fatal + (f"{k} ")
    else:
        fatal = fatal + (f"{k}_{number_arr[u]-1} ")
    u = 0

print(fatal)