# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

accept_to_input = True
Numbers_list = []
print("Введите 5 чисел: ")
while accept_to_input:
    i = int(input())
    Numbers_list.append(i)
    if len(Numbers_list) >= 5:
        in_text = str(input("Вы хотите ввести еще число? (y / n)"))
        if in_text == 'y':
            accept_to_input = True
        else:
            accept_to_input = False
            break

K = int(input("Введите размер смещения K: "))
print(f"Последовательность: {Numbers_list}")
print(f"Число на которое производится смещение: {K}")

New_list = []
i = 0
temp = 0
while i < len(Numbers_list):
    temp = i - K+1
    if temp < K:
        New_list.append(Numbers_list[temp])
    else:
        break
    temp = 0
    i += 1
print(f"Результат смещения: {New_list}")