# 3 - Дан массив размера N. После каждого 
# отрицательного элемента массива вставьте элемент с 
# нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => 
# [28, -46, 0, 14, -14, 0]

import random
n = int(input('Введите размер массива : '))
a_list = random.sample(range(-100, 100), n)
def transform(a_list:list)->list:
    result = []
    for element in a_list:
        result.append(element)
        if element < 0:
            result.append(0)
    return result
    
print(transform(a_list))