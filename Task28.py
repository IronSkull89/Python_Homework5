# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum_rec(a, b):
    if a and b:
        return sum_rec(a-1, b-1) + 1 + 1
    if not a and b:
        return sum_rec(a, b-1) + 1
    if a and not b:
        return sum_rec(a-1, b) + 1 
    return 0

a = int(input("Введите первое слагаемое: "))
b = int(input("Введите второе слагаемое: "))
print(f"{a}+{b}={sum_rec(a, b)}")