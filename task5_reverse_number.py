# Задача 5: Обратный порядок чисел
# Напишите программу, которая запрашивает у пользователя трехзначное число и выводит его цифры в обратном порядке.
# Пример:
# Ввод: 123
# Вывод: 321
a = int(input())
c = a//100
b = a%100
d = a%10
k = b//10
print (d*100+k*10+c)