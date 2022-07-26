
print('Welcome to the ultimate pub quiz!')
player_ready = input('do you want to play? ')

if player_ready != 'yes':
    quit()

print('Okay! Lets play :)')

answer = input('What is the answer to everything? ') 
if answer == '42':
    print('Correct!')
