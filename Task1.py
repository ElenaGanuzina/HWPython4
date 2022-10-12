# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

from decimal import Decimal

def find_accuracy(num, accuracy):
    num = Decimal(f"{num}")
    num = num.quantize(Decimal(f"{accuracy}"))
    print(num)

num = float(input("Enter a real number: "))
accuracy = float(input("Enter the required accuracy '0.0001': ")) 
find_accuracy(num, accuracy)