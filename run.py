
print('Welcome to the ultimate pub quiz!')
player_ready = input('do you want to play? ')

if player_ready != 'yes':
    quit()

print('Okay! Lets play :)')

answer = input('What is the answer to everything? ') 
if answer == '42':
    print('Correct!')
else:
    print('Incorrect!')

answer = input('How many numbers are there on a roulette wheel? ') 
if answer == '37':
    print('Correct!')
else:
    print('Incorrect!')

    answer = input('What is the value of the letter Q in Scrabble? ') 
if answer == '10':
    print('Correct!')
else:
    print('Incorrect!')

    answer = input('Nostradamus was famous for making what? ') 
if answer == 'predictions':
    print('Correct!')
else:
    print('Incorrect!')

    answer = input('What was the middle name of Wolfgang Mozart? ') 
if answer == 'Amadeuss':
    print('Correct!')
else:
    print('Incorrect!')