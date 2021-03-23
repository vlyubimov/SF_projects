import numpy as np


def binary_search(number):
    """Самым оптимальным вариантом поиска заганного числа, является бинарный поиск. Он позволяет находить
        Он позволяет сократить число попыток до О(Log n). Сначала устанавливаем число на середину возможных
        значений. И далее делаем проверку, если заганное число больше среднего - переносим поиск в область
        больших значений, если заганное число меньге - соответственно в область меньших значений. И по данномму
        алгоритму пока не будет найдено число.
        Функция принимает заганное число и возвращает число попыток"""
    count = 1
    lower = 1
    upper = 100
    mid = (upper + lower) // 2
    while mid != number:
        if number > mid:
            lower = mid + 1
            count += 1
        else:
            upper = mid - 1
            count += 1
        mid = (upper + lower) // 2
    else:
        return count


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(binary_search)
