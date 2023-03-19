"""Игра угадай число"""

import numpy as np

# Функция, которая угадает number
def game_predict(number):
    """Функция угадывающая число от 1 до 100.
    Функция учитывает информацию о том, больше или меньше случайное число нужного нам числа.

    Args:
        number: Загаданное компьютером число

    Returns:
        count: Количество попыток
    """
    count = 0 # Задаём переменную

    # Сначала пробуем среднее значение, чтобы сократить зону поиска
    predict_number = 50
    count += 1
    if number == predict_number:
        return count
        
    # Если загаданное число меньше 50
    elif number < predict_number:
        # Таким же способом далее сокращаем зону поиска
        predict_number = 25
        count += 1
        if number == predict_number:
            return count # Возвращаем текущее количество попыток если число угадано
            
        elif number < predict_number:
            # Зададим список из оставшихся возможных вариантов чисел и перебираем каждое 
            predict_list = list(range(1, 25))
            for predict_number in predict_list:
                count += 1
                if number == predict_number:
                    return count
            
        else:
            predict_list = list(range(26, 50))
            for predict_number in predict_list:
                count += 1
                if number == predict_number:
                    return count
        
    # Идентично, если загаданное число больше 50
    else:
        predict_number = 75
        count += 1
        if number == predict_number:
            return count
            
        elif number < predict_number:
            predict_list = list(range(51, 75))
            for predict_number in predict_list:
                count += 1
                if number == predict_number:
                    return count
            
        else:
            predict_list = list(range(76, 101))
            for predict_number in predict_list:
                count += 1
                if number == predict_number:
                    return count

# Функция, которая возращает среднее количество попыток
def score_game(game_predict) -> int:
    
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # Загадываем список чисел

    for number in random_array:
        count_ls.append(game_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

score_game(game_predict)