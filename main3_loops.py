# Вывести фразу hello world на консоль 10 раз
# for i in range(10):
#     print("hello world")


# сгенерировать 10 случ чисел в диапазоне от 2 до 10, вывести их на консоль и найти сумму
import random

# i = 0
# sum = 0
# while i < 10:
#     val = random.randint(2, 10)
#     sum += val
#     print(val, end=' ')
#     i += 1
# print()
# print('sum =', sum)


# сгенерировать 10 случ чисел в диапазоне от 2 до 10, вывести их на консоль и найти максимальное из них

max = 0 # берем наименьшее из возможынх или еще меньше
for i in range(10):
    x = random.randint(2, 7)
    print(x, end=' ')
    if x > max:
        min = x
print()
print('max =', max)

# сгенерировать 10 случ чисел в диапазоне от 2 до 10, вывести их на консоль и найти минимальное из них

min = 17 #берем наибольшее из возможных или еще больше
for i in range(10):
    x = random.randint(2, 7)
    print(x, end=' ')
    if x < min:
        min = x
print()
print('min =', min)












