# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

from random import choices

def create_list(num):
    return choices(range(num * 2), k=num)

def unique_num(arr):
    new_list = []
    for i in arr:
        if arr.count(i) < 2:
            new_list.append(i)
    return new_list


num = int(input("n = "))
my_arr = (create_list(num))
print(my_arr)
print(unique_num(my_arr))