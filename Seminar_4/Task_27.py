"""Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore. The shells that she sells are sea shells. I'm sure. So if she sells sea shells on the sea shore. I'm sure that the shells are sea shore shells.
Output: 13
"""
print("Введите текст: ")
text = str(input())
text = text.lower()
word = ''
words = []

for i in text:
    if i == '.':
        words.append(word)
    elif i != ' ':
        word = word + i    
    else:
        words.append(word)
        word = ''

print(words)
words_number = {'0'}

for temp in words:
    words_number.add(temp)
words_number.remove('0')

print(len(words_number))