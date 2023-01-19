from collections import Counter
from random import randrange


def start_new_game() -> None:
    """Реализует цикл игры до 100 очков с рандомной генирацией начальной колоды"""
    sum_total_score_bot: int = 0
    sum_total_score_player: int = 0
    while (sum_total_score_bot < 100) and (sum_total_score_player < 100):
        base_kit: list = [randrange(1, 7) for x in range(5)]  # Генерация начальной колоды игрока
        bot_kit: list = [randrange(1, 7) for x in range(5)]  # Генерация начальной колоды бота
        draw_dice_kit(base_kit)  # Отрисовываем результат игрока в консоль
        print(f'Ваш стартовый набор')
        change_kit(base_kit, bot_kit)
        player_score: int = score(base_kit)
        bot_score: int = score(bot_kit)
        sum_total_score_player += player_score
        sum_total_score_bot += bot_score
        identifying_the_winner(sum_total_score_bot, sum_total_score_player)  # Подсчет очков по колоде текущего набора кубиков

def change_kit(base_kit: list, bot_kit: list) -> None:
    '''Реализует возможность переброса кубиков игрока, после идет ход бота'''
    print('Хотите перебросить кубики y|n')
    answer: str = str(input())
    if answer == 'y':
        generetes_kit(base_kit)
        print('Ваша измененая колода')
        draw_dice_kit(base_kit)
    print('Ход бота')
    draw_dice_kit(bot_kit)


def draw_dice(number: int) -> None:
    """Функция описывает отрисовку точек на кубике"""
    amount_dot_on_dice: int = number
    dot: str = ' o'
    drawing_half_of_dice: str = (
                                 '-----\n|' + dot[amount_dot_on_dice >= 2] +
                                 ' ' + dot[amount_dot_on_dice >= 4] + '|\n|' +
                                 dot[amount_dot_on_dice >= 6]
                                 )
    print(drawing_half_of_dice + dot[amount_dot_on_dice & 1] + drawing_half_of_dice[::-1])


def draw_dice_kit(base_kit: list) -> list:
    """Отрисовывает кубики в терминале"""
    for dice in base_kit:
        draw_dice(dice)
    return base_kit


def generetes_kit(base_kit: list) -> None:
    """Изменяет значение на кубиках по запросу"""
    print('введите 1 если меняем кубик и 0 если нет.\nОжидаемый ввод 5 чисел, по одному за раз')
    input_number: list = [int(input()) for i in range(5)]  # Принимает заявку на переброс кубиков
    index: int = 0  # Счетчик прохода по колоде
    for x in input_number:
        if x == 1:
            base_kit[index] = randrange(1, 7)  # Изменяем конкретный бросок через рандом
        index += 1


def score(kit: list) -> int:
    """Подсчитывает балы за выпавшие комбинации"""
    combination_score: list = [0]  # Список для возможных комбинаций
    sort_result: list[tuple[int, int]] = Counter(kit).most_common()  # Сортируем одинаковые кости по убыванию числа совпадений
    most_common_dice: tuple[int, int] = sort_result[0]
    second_most_common_dice: tuple[int, int] = sort_result[1]
    most_common_count: int = most_common_dice[1]
    second_most_common_count: int = second_most_common_dice[1]
    if len(sort_result) == 5:  # Выпал стрит
        combination_score.append(20)
    if most_common_count == 4:  # Выпало каре
        combination_score.append(40)
    elif most_common_count == 3 and second_most_common_count == 2:  # Выпал фул-хаус
        combination_score.append(30)
    elif most_common_count == 3:  # Выпал сет
        combination_score.append(10)
    elif most_common_count == 2 and second_most_common_count == 2:  # Выпали 2 пары
        combination_score.append(4)
    elif most_common_count == 2:  # Выпала пара
        combination_score.append(2)
    final_score: int = max(combination_score)
    return final_score


def identifying_the_winner( sum_total_score_bot: int, sum_total_score_player: int) -> None:
    """Сравнивает результаты игроков и определяет победителя"""
    if (sum_total_score_player >= 100) or (sum_total_score_bot >= 100):
        if sum_total_score_player >= 100:
            print('Вы победили')
        elif sum_total_score_bot >= 100:
            print('Бот победил')
        else:
            print('Ничья')
    print(
          f'Ваш итоговый счет {sum_total_score_player}',
          f'Счет бота {sum_total_score_bot}', sep='\n'
          )

def print_game_rule() -> None:
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