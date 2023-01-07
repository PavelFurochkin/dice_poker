import sys
from collections import Counter
from random import *
from typing import NoReturn


def start_menu_game() -> NoReturn:
    """Меню начала игры"""
    game_rule()
    while True:
        print('Хотите начать новую игру(n) или выйти(q)? \nВведите n|q ...')
        letter: str = str(input())
        if letter == 'n':
            start_new_game()
        elif letter == 'q':
            sys.exit('До новых встреч')


def start_new_game() -> NoReturn:
    """Генерирует начальные колоды, дает выбор по замене кубов"""
    base_kit: list = [randrange(6) for x in range(5)]  # Генерация начальной колоды игрока
    bot_kit: list = [randrange(6) for x in range(5)]  # Генерация начальной колоды бота
    print_kit_dice(base_kit)  # Отрисовываем результат игрока в консоль
    print(f'Ваш стартовый набор')
    print('Хотите перебросить кубики y|n')
    answer: str = str(input())
    if answer == 'y':
        base_kit = change_base_dice(base_kit)
        print('Ход бота')
        print_kit_dice(bot_kit)  # Отрисовываем результат бота в консоль
        player_score: int = scoring(base_kit)  # Подсчет очков игрока
        bot_score: int = scoring(bot_kit)  # Подсчет очков бота
        identifying_the_winner(player_score, bot_score)
    else:
        print('Ход бота')
        print_kit_dice(bot_kit)
        player_score = scoring(base_kit)
        bot_score = scoring(bot_kit)
        identifying_the_winner(player_score, bot_score)


def dice_sketch(number: int) -> NoReturn:
    """Функция описывает отрисовку точек на кубике"""
    amount_dot_on_dice: int = number
    dot: str = 'o '
    drawing_half_of_dice: str = (
                                 '-----\n|' + dot[amount_dot_on_dice < 1] +
                                 ' ' + dot[amount_dot_on_dice < 3] + '|\n|' +
                                 dot[amount_dot_on_dice < 5]
                                 )
    print(drawing_half_of_dice + dot[amount_dot_on_dice & 1] + drawing_half_of_dice[::-1])


def print_kit_dice(base_kit: list) -> list:
    """Отрисовывает кубики в терминале"""
    for dice in base_kit:
        dice_sketch(dice)
    return base_kit


def change_base_dice(base_kit: list) -> list:
    """Изменяет значение на кубиках по запросу"""
    print('введите 1 если меняем кубик и 0 если нет.\nОжидаемый ввод 5 чисел, по одному за раз')
    input_number: list = [int(input()) for i in range(5)]  # Принимает заявку на переброс кубиков
    index: int = 0  # Счетчик прохода по колоде
    while index < len(input_number):
        for x in input_number:
            if x == 1:
                base_kit[index] = randrange(6)  # Изменяем конкретный бросок через рандом
            index += 1
    print('Ваша измененая колода')
    print_kit_dice(base_kit)
    return base_kit


def scoring(player_kit) -> int:
    """Подсчитывает балы за выпавшие комбинации"""
    combination_score: list = []  # Список для возможных комбинаций
    sort_result: list[tuple[int, int]] = Counter(player_kit).most_common()  # Сортируем одинаковые кости по убыванию числа совпадений
    past_i = 0  # Переменная для хранения числа совпадений из предыдущего кортежа
    if len(sort_result) == 5 :  # Выпал стрит
        combination_score.append(20)
    for i in sort_result:
        if i[1] == 4:  # Выпало каре
            combination_score.append(40)
        elif past_i == 3 and i[1] == 2:  # Выпал фул-хаус
            combination_score.append(30)
        elif i[1] == 3:  # Выпал сет
            combination_score.append(10)
        elif past_i == 2 and i[1] == 2:  # Выпали 2 пары
            combination_score.append(4)
        elif i[1] == 2:  # Выпала пара
            combination_score.append(2)
        past_i = i[1]
    final_score = max(combination_score)
    return final_score


def identifying_the_winner(player_score, bot_score):
    """Сравнивает результаты игроков и определяет победителя"""
    total_score_player = []
    total_score_bot = []
    total_score_player.append(player_score)
    total_score_bot.append(bot_score)
    sum_total_score_player = sum(total_score_player)
    sum_total_score_bot = sum(total_score_bot)
    if (sum_total_score_player or sum_total_score_bot) == 100:
        if total_score_player == 100:
            print('Вы победили')
        elif total_score_bot == 100:
            print('Бот победил')
        else:
            print('Ничья')
    print(
          f'Ваш итоговый счет {sum_total_score_player} и серия комбинаций {total_score_player}',
          f'Счет бота {sum_total_score_bot} и серия комбинаций {total_score_bot}', sep='\n'
          )


def game_rule():
    """Объясняет правила игры"""
    print(
        'Правила игры покер на костях:',
        'Каре 4 одинаковые кости - 40 очков',
        'Фул-хаус 3 одинаковые кости и 2 одинаковые кости - 30 очков',
        'Стрит 5 значений подряд, включая переход с 6 на 1 - 20 очков',
        'Сет 3 одинаковые кости - 10 очков',
        'Две пары - 4 очка',
        'Пара - 2 очка', sep='\n'
    )

start_menu_game()
