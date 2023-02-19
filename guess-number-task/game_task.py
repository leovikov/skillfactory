"""Игра угадай число"""

import numpy as np

# Функция, которая угадает number
def game_predict(number):
    """Угадываем число

    Args:
        number: Загаданное компьютером число

    Returns:
        int: Количество попыток
    """
    count = 0

    while True:
        count += 1
        
        if number in range(1, 11):
            predict_number = np.random.randint(1, 11)
            if number == predict_number:
                break  # Угадано
        
        elif number in range(11, 21):
            predict_number = np.random.randint(11, 21)
            if number == predict_number:
                break  # Угадано
        
        elif number in range(21, 31):
            predict_number = np.random.randint(21, 31)
            if number == predict_number:
                break  # Угадано
        
        elif number in range(31, 41):
            predict_number = np.random.randint(31, 41)
            if number == predict_number:
                break  # Угадано
            
        elif number in range(41, 51):
            predict_number = np.random.randint(41, 51)
            if number == predict_number:
                break  # Угадано
        
        elif number in range(51, 61):
            predict_number = np.random.randint(51, 61)
            if number == predict_number:
                break  # Угадано
        
        elif number in range(61, 71):
            predict_number = np.random.randint(61, 71)
            if number == predict_number:
                break  # Угадано
        
        elif number in range(71, 81):
            predict_number = np.random.randint(71, 81)
            if number == predict_number:
                break  # Угадано
        
        elif number in range(81, 91):
            predict_number = np.random.randint(81, 91)
            if number == predict_number:
                break  # Угадано
        
        else:
            predict_number = np.random.randint(91, 101)
            if number == predict_number:
                break  # Угадано   
                
    return count

# Функция, которая показывает среднее количество попыток
def score_game(game_predict) -> int:
    
    count_ls = []
    np.random.seed(1)  # Фиксируем seed для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # Загадываем список чисел

    for number in random_array:
        count_ls.append(game_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

score_game(game_predict)