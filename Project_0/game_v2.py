"""Игра угадай число
Компьютер сам загадывает и сам угадывает число используя усовершенствованный алгоритм
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    #Установим начальные границы интервала, внутри которого находится загаданное число
    upper_bound = 101
    lower_bound = 1

    while True:
        count += 1
        predict_number = lower_bound + (upper_bound - lower_bound)//2 # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number<predict_number:
            upper_bound = predict_number - 1 #"Сжимаем" исходный интервал "отрезая" верхнюю часть
        else:
            lower_bound = predict_number + 1  #"Сжимаем" исходный интервал "отрезая" нижнюю часть
            
        
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
