# Задайте последовательность чисе. Напишите программу которая выведет список неповторяющихся элементов исходной прследовательности.

from random import randint

m = 1
n = 15
list1 = list(set(randint(m, n) for i in range(1, 15)))
list1.sort(reverse = True)
print(list1)
