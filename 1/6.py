import random

# a = random.randint(1, 10)
# b = random.randint(1, 10)

# if a > b:
#     print(a)
# else:
#     print(b)
    
    
# # ===================================================================

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))

# num3 = abs(num1 - num2)
# num4 = abs(num2 - num1)
# # print(num3)

# if num3 == 135 or num4 == 135:
#     print('yes')
# else:
#     print('no')
    
    

# # ===================================================================


# num = random.randint(1, 10)

# print ('число', num)

# if num > 100 or num < -100:
#     print('—')
# else:
#     print('+')
    
    
# # ===================================================================

num = int(input('Введите номер месяца: '))


if num in range (3, 6):
    print('Весна')
elif num in range(6, 9):
    print('Лето')
elif num in range(9, 12):
    print('Осень')
elif num == 12:
    print('Зима')
    
    
# # ===================================================================


a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))

if a > 10 and b > 10 and c > 10:
    print('yes')
else:
    print('no')
    
    
# # ===================================================================

a = random.randint(-1000, 1000)
b = random.randint(-1000, 1000)
c = random.randint(-1000, 1000)


count = 0

if a > 0: count += 1
if b > 0: count += 1
if c > 0: count += 1

print('Количество положительных чисел:', count)