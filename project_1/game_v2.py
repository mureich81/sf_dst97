"""Игра угадай число
Компьютер загадывает целое число от 1 до 100, угадывает его за минимальное кол-во попыток
В качестве результата возвращается среднее по 1000-е повторов кол-во попыток за которые угадывается число 
"""

import numpy as np

random_array = np.random.randint(1, 100, size=(10)) 
# генерируем список из 1000-и случайных чисел
count_ls = []
# создаем список, который будем населять кол-вом попыток для угадывания каждого из тысячи, загаданных чисел

for number in random_array:
# создаем цикл для последовательного сравнения чисел из списка с медианами по диапазону возможных значений и фиксирования попыток
    count = 0
    # выставляем счетчик на 0
    min = 1
    max = 100
    # задаем исходные мин и макс значения для диапазона возможных значений
    predict_number = int((min+max)/2)
    # задаем первую медиану по максимальному диапазону для сравнения
    
    while predict_number != number:
    # цикл сравнивает число из случайного массива с медианой актуального диапазона чисел
        count += 1
        if number > predict_number:
            min = predict_number
            predict_number = int((min+max)/2)
        elif number < predict_number:
            max = predict_number 
            predict_number = int((min+max)/2)
    count_ls.append(count)
score = round(sum(count_ls)/len(count_ls))
# вычисляем среднее
print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
