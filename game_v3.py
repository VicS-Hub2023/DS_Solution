import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Функция угадывает загаданное число методом бинарного поиска.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = 50  # начинаем угадывать с середины диапазона
    r_start, r_end = 1, 100  # диапазон значений, в котором ищем загаданное число

    while True:
        count += 1
        if predict == number:
            break
        elif predict < number:
            r_start = predict
            predict = np.random.randint(r_start, r_end + 1)
        else:
            r_end = predict
            predict = np.random.randint(r_start, r_end + 1)

    return count



def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


# Run benchmarking to score effectiveness of all algorithms
print('Run benchmarking for random_predict: ', end='')
score_game(game_core_v3)
