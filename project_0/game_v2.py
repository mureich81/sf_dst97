import numpy as np
def random_predict(number:int=1):
    """внутренняя функция которая угадывает значения переданного
    пользователем (либо взятого из случайного массива) аргумента 
    (в функции score_game), через генерацию случайных чисел в теле функц
    random_predict
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return(count) # количество попыток за которые угадывается число  
def score_game(random_predict):
    count_lst = []
    np.random.seed(1) 
    random_array = np.random.randint(1, 100, size=(100))
    """генерируем случайный список из 1000и чисел от 1 до 100"""
    for number in random_array:
        """передаем из по одному в функцию random_predict"""
        count_lst.append(random_predict(number))
    score = int(np.mean(count_lst))
    print(f'your algorythm is guessing the number in average {score} times')
    return score
#print(score_game(random_predict))
if __name__ == '__main__':
    score_game(random_predict)
