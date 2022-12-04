# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print(' ')
print('Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')
print(' ')
data = '2 3 5 9 3'.split()
data = list(map(int, data))
even=[(data[i]) for i in range(0, len(data)) if i%2 != 0]
print('Для списка - ', data, '\nЭлементы стоящие на нечётной позиции - ',even,'\nСумма которых равна - ',sum(even))



# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

print(' ')
print('Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.')
print(' ')
data = '2 3 4 5 6'.split()
data = list(map(int, data))
product_pairs=[(data[i]* data[len(data) - i-1]) for i in range(0, len(data)//2+1)]
print('Для списка - ', data, '\nПроизведение указаных пар чисел списка - ',product_pairs)



# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print(' ')
print('Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов')
print(' ')
data = '1.1 1.2 3.1 5 10.01'.split()
data = list(map(float, data))
fractional_values=[round((data[i] - int(data[i])),5) for i in range(0, len(data))]
# print(fractional_values)
min=fractional_values[0]
max=fractional_values[0]
for i in range(1,len(fractional_values)):
    if max<fractional_values[i]:
        max=fractional_values[i]
    if min>fractional_values[i] and fractional_values[i] != 0.0:
        min=fractional_values[i]
# print(min,max)
print('Для списка - ', data, '\nРазница между максимальным и минимальным значением дробной части элементов - ',max - min)



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print(' ')
print('Напишите программу, которая будет преобразовывать десятичное число в двоичное')
print(' ')
n=int(input('Введите целое десятичное число: '))
print('Число - ',n,' в двоичном формате = ', end='')
while (n>0):
    a=int(float(n%2))
    n=(n-a)/2
    print(a, end='')
print()


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

print(' ')
print('Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')
print(' ')
n=int(input())
f1 = 0
f2 = 1
nlist = [0, 1]
list = [0, 1]
for i in range(2, n + 1):
    f1, f2 = f2, f1 + f2
    list.append(f2)
for i in range(2, n + 1):
    nlist.append(((-1)**(i+1))*list[i])
nlist.reverse()
for i in range(1, n + 1):
    nlist.append(list[i])
print(nlist)