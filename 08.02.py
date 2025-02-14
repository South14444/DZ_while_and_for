# str = input()
# counter = 0
# positive_period = 0
# while str != 'stop':
#     number = float(str)
#     if number >= 0:
#         counter += 1
#         if positive_period < counter:
#             positive_period = counter
#     else:
#         counter = 0
#     str = input()
# print(positive_period)
#
# low = 1
# high = 1000
# counter = 1
# while low <= high:
#     counter += 1
#     number = (low + high) // 2
#     print(int(number))
#     sign = input()
#     if sign == "<":
#         high = (low + high) // 2 + 1
#     elif sign == ">":
#         low = (low + high) // 2 - 1
#     elif sign == "=":
#         break
# print(counter)
import math
from math import factorial

# password = input()
# second_password = input()
# correct_item_counter = 0
# while correct_item_counter != 3:
#     if len(password) < 8:
#         print("Короткий")
#     else:
#         correct_item_counter += 1
#         if "123" in password:
#             print("Простой")
#         elif password != second_password:
#             print("Различаются")
#         else:
#             correct_item_counter += 2
#             print("ОК")

# number = int(input())
# degree = 0
# while number >= 2 ** degree:
#    if number == 2 ** degree:
#        answer = degree
#        break
#    else:
#        answer = "NO"
#        degree += 1
# print(answer)

# n = int(input())
# base = int(input())
# result = ""
# while n > 0:
#     result = str(n % base) + result
#     n //= base
# print(result)

# n = int(input())
# summa = 0
# for i in range(n):
#     summa += 1/(i+1)
# print(summa)

# n = int(input())
# summa = 0
# i = 0
# while summa <= n:
#     summa += 1 / (i + 1)
#     i+=1
# print(i)

# n = int(input())
# summa = 0
# for i in range(n):
#     summa += 1/(i+1)**2
# print(summa)
# print(math.pi ** 2 / 6)

# n = int(input())
# summa = 0
# fact = 1
# for i in range(n):
#     fact *= i + 1
#     summa += fact
# print(summa)

# sign = 1
# for i in range(10):
#     sign *= -1
#     print(sign)

a = float(input())
n = int(input())
summa = 1
numer = 1
for i in range(n):
    numer *= -a
    summa += numer
    print(summa)
print(summa)
