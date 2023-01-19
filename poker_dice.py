import sys
import poker_dice_functions


def start_menu_game() -> None:
    """Меню начала игры"""
    poker_dice_functions.print_game_rule()
    while True:
        print('Хотите начать новую игру(n) или выйти(q)? \nВведите n|q ...')
        letter: str = str(input())
        if letter == 'n':
            poker_dice_functions.start_new_game()
        elif letter == 'q':
            sys.exit('До новых встреч')


if __name__ == '__main__':
    start_menu_game()
