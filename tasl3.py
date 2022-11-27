# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

a = int(input('Введите число: '))

def in_list(a):
    list = []
    for i in range (1, a+1):
        list.append((1+1/i)**i)
    return list

def sum(list):
    sum=0
    for i in range (len(list)):
        sum=sum + list[i]
    return sum


list = in_list(a)
print(list)
result = sum(list)
print(result)