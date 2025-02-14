# n = int(input())
# x = int(input())
# number = x
# frac = 1
# step = x
# sign = -1
# for i in range(1,n+1):
#     step *= x * x
#     frac *= (2 * i) * (2 * i + 1)
#     number += sign * (step / frac)
#     sign *= -1
# print(number)

# n = int(input())
# x = int(input())
# number = x
# step = x
# p = 1
# sign = -1
# for i in  range(1,n+1):
#     step *= x * x
#     p += 2
#     number += sign * (step / p)
#     sign *= -1
# print(number)

# x = int(input())
# a = 1
# for i in range(1,x+1):
# 	a= (a+1)/i
# 	print(a)
#
# x = int(input())
# f1 =0
# f2 = 1
# f3 = 2
# print(1)
# print(2)
# for i in range(x-2):
# 	f1= f2
# 	f2=f3
# 	f3=f2+ f1
# 	print(f3)

# n = int(input())
# degree = 3
# coun = 1
# while degree - n < 0:
#     degree *= 3
#     coun += 1
# print(coun)

# summa = 0
# k = 1
# n = int(input())
# while summa < n:
#     summa+=k
#     print(k)
#     k+=1
# print(summa)

# n = int(input())
# inverted = 0
# while n > 0:
#     k = n % 10
#     n //= 10
#     inverted = inverted * 10 + k
# print(inverted)

# n = int(input())
# if n < 2:
#     print(False)
# else:
#     i = 2
#     is_prime = True
#     while i * i <= n:
#         if n % i == 0:
#             is_prime = False
#             break
#         i += 1
#     print(is_prime)

a = int(input())
b = int(input())
while b > 0:
    a, b = b, a % b
print(a)
