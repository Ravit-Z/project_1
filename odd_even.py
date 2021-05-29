import random

GAME = {'user': None,
        'computer': None}

VALIDATE = {'text' : ['even', 'odd'],
            'number' : [f'{x}' for x in range(1, 101)]}

def check_input(val:str, type:str) -> bool:
    return any([val.lower() in valid for valid in VALIDATE[type]])

def read_text(text:str, input_type:str) -> str:
    val = input(text)
    if val == '-1':
        print("ok, bye bye :)")
        exit()
    if check_input(val, input_type):
        return (val.lower())
    print(f'You entered: {val}')
    return read_text(text, input_type)

def draw() -> int:
    return random.randint(1, 100)

def is_even(num1:int, num2:int) -> bool:
    return (num1 + num2) % 2 == 0

def initial_game() -> dict:
    game = GAME.copy()
    game['user'] = read_text("Please enter if you'd like to be even or odd: ", 'text')
    game['computer'] = 'even' if game['user'] == 'odd' else 'odd'
    return game

def who_won(user_n:int, computer_n:int, game_dict:dict)-> str:
    even = is_even(user_n, computer_n)
    if (game_dict['user'] == 'even' and even) or (game_dict['user'] == 'odd' and not even) :
        return 'You'
    return 'Computer'

def play_game():
    picks = initial_game()
    user_num = int(read_text('Enter a number between 1 - 100: ', 'number'))
    computer_num = draw()
    winner = who_won(user_num, computer_num, picks)
    print(f"{winner} won this game!!!")


if __name__ == '__main__':
    print("To exit enter '-1'")
    while True :
        play_game()
