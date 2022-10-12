# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]

def prime_factors(num):
    if num <= 0:
        print("Wrong number!")
        return []
    else:
        prime_list = []
        for i in range(2, num + 1):
            while num % i == 0:
                prime_list.append(i)
                num //= i
                
    return prime_list

num = int(input("Enter an integer: "))
print(prime_factors(num))