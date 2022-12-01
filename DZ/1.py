# num = int (input("Введите число   "))
# res = 1
# for i in range (1, num + 1):
#     # print (res, end = " ")
#     res += num
    
# for res in range (1, num):
#     res += num
#     print (res*res, end = " ")


# 1 - Напишите программу, которая принимает на 
# вход вещественное число и показывает сумму 
# его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# (-0.56) -> 11


number = input('введите число')
def sum_in_number(some_number):
    sum = 0
    for i in some_number:
        if i.isdigit():
            i = int(i)
            sum = sum + i
    print(sum)
sum_in_number(number)