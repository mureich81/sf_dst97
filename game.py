import numpy as np
number = np.random.randint(1, 100) # guess number
count = 0
while True:
    count += 1
    predict_number = int(input('Guess number you looser:'))
    if predict_number < number:
        print('You must input a larger number')
    elif predict_number > number:
        print('You must input a smaller number')
    else:
        print(f'You guessed the number {number} right in {count} trials')
        break
    