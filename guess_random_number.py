import random as rand

def user_guess(x):
  rand_num = rand.randint(1,x)
  guess = 0
  while guess != rand_num:
    guess = int(input(f'Guess a number between 1 and {x}: '))
    if guess < rand_num:
      print('Too low. Guess again.')
    elif guess > rand_num:
      print('Too high. Guess again.')

  print('You\'ve got the right number {rand_num} correctly!')


def computer_guess(x):
  low, high = 1, x
  feedback = ''
  while feedback != 'c':
    if low != high:
      guess = rand.randint(low, high)
    else:
      guess = low
    feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1
      
  print('You\'ve got the right number {rand_num} correctly!')


for i in range(1, 11):
  guess(i)
