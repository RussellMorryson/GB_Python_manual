# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]

go = True
list_1 = []
print("Введите 7 чисел, оно добавится в массив: ")
while go:    
    i = int(input())
    list_1.append(i)
    if len(list_1) >=7:
        print("Вы хотите ввести еще число? (y / n)")
        in_text = str(input())
        if in_text == 'y':
            go = True
        else:
            go = False
        break

list_2 = [1]
count = 0

for i in list_1:
    for j in list_2:
        if j != i:
            count += 1
            
    if count > 0:
        list_2.append(i)
        count = 0

print(f"Всего {len(list_2)-1} разных чисел")