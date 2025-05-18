import random

answer = random.randint(1, 100)

while True:
    guess = int(input('guess='))
    print('Your guess is', guess)

    if guess == answer:
        print('Good guess! You got it right.')
        break
    elif guess < answer:
        print('Too low')
    else:
        print('Too high')