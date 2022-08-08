
print('Welcome to the ultimate pub quiz!')
player_ready = input('do you want to play? ')

if player_ready.lower() != 'yes':
    quit()

print('Okay! Lets play :)')
score = 0

answer = input('What is the answer to everything? ') 
if answer.lower() == '42':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input('How many numbers are there on a roulette wheel? ') 
if answer.lower() == '37':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input('What is the value of the letter Q in Scrabble? ') 
if answer.lower() == '10':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input('Nostradamus was famous for making what? ') 
if answer.lower() == 'predictions':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input('What was the middle name of Wolfgang Mozart? ') 
if answer.lower() == 'amadeuss':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input('What was the most downloaded app of 2020? ') 
if answer.lower() == 'tiktok':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input('Which Italian city is Shakespeare’s Romeo and Juliet set? ')
if answer.lower() == 'verona':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
 
 
answer = input('In the Star Wars series of films what is the name of Han Solo’s Wookie co-pilot? ') 
if answer.lower() == 'chewbacca':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input('Which pastry is used to make Baklava? ') 
if answer.lower() == 'filo':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input('The Road to Wigan……what, is a book by George Orwell? ') 
if answer.lower() == 'pier':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


print('You correctly answered ' +  str(score)  + ' questions ')
print('You incorrectly answered ' + str((score/10) * 100) + '%.')