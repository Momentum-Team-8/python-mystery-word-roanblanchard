import random

EASY_WORDS = [
    'bang', 'seed', 'sell', 'inch', 'firm', 'meal', 'mess', 'rate', 'fill', 'goal', 'full', 'fade', 'herb', 'body', 'goat', 'disk', 'rich', 'silk', 'plot', 'gene', 'riot', 'zero', 'cast', 'dose', 'stun',
    'throw', 'drift', 'tease', 'sweat', 'siege', 'irony', 'vague', 'spell', 'young', 'brain', 'color', 'spill', 'forge', 'glory', 'torch', 'slant', 'yearn', 'bacon', 'board', 'spine', 'width', 'enjoy', 'drama', 'wound',
]
NORM_WORDS = [
    'stable', 'insure', 'sermon', 'candle', 'suntan', 'rabbit', 'origin', 'cancel', 'waiter', 'stress', 'attack', 'deadly', 'debate', 'reform', 'prayer', 'master', 'safety', 'castle', 'reward', 'linear', 'horror', 'tumble', 'export', 'matter', 'tumour',
    'appoint', 'package', 'brother', 'pudding', 'premium', 'trainer', 'feeling', 'realize', 'balance', 'meaning', 'private', 'account', 'quarrel', 'dribble', 'abandon', 'overeat', 'rainbow', 'concede', 'command', 'silence', 'musical', 'railcar', 'warrant', 'peasant', 'opinion',
]
HARD_WORDS = [
    'correction', 'conviction', 'monopoly', 'patience', 'uncertainty', 'acceptance', 'confusion', 'conception', 'analysis', 'pleasure', 'regulation', 'threshold', 'transmission', 'interface', 'notebook', 'priority', 'neighbour', 'horseshoe', 'vegetable', 'ambition', 'philosophy', 'crosswalk', 'judgment', 'execution', 'transaction', 'comfortable', 'commission', 'elaborate',
    'parameter', 'identity', 'exclusive', 'understand', 'translate', 'chauvinist', 'withdrawl', 'evolution', 'domestic', 'catalogue', 'conversation', 'coalition', 'competence', 'freighter', 'cooperative', 'abundant', 'blackmail', 'isolation', 'communist', 'infinite', 'treasurer', 'governor',
]

level = input("Select difficulty: 1 for easy, 2 for medium, 3 for hard ")
if level == "1":
    word_choice = (random.choice(EASY_WORDS))
if level == "2":
    word_choice = (random.choice(NORM_WORDS))
if level == "3":
    word_choice = (random.choice(HARD_WORDS))


def mystery_word_game():
    tries = 0
    word_list = []
    test = word_choice
    
    for x in test:
        word_list.append(x)

    print("Your word is " + str(len(word_list)) + " characters long.")
    
    correct_guesses = []
    incorrect_guesses = []
    while tries != 8:
        current_progress = []
        player_guess = input("What letter would you like to guess? ")
        if len(player_guess) > 1:
            print("Your guess must be one letter!")
            player_guess = input("What letter would you like to guess? ")
        if player_guess in correct_guesses or player_guess in incorrect_guesses:
            print("You already guessed that, try again.")
            pass
        if player_guess not in word_list:
            tries += 1
        for x in word_list: 
            if player_guess == x:
                current_progress.append(player_guess)
                correct_guesses.append(player_guess)
            elif x in correct_guesses:
                current_progress.append(x)
            else:
                current_progress.append("_")
                incorrect_guesses.append(player_guess)
        if current_progress == word_list:
            print("You win!! Good job.")
            break
        if tries == 8:
            print("You lose!! You get nothing!")
            print("Your word was: " + test)
            break
        print(current_progress)





mystery_word_game()