import random
print('Coin Flip Simulator')

# input
number = int(input('How many coins do you want to flip? '))

# process & output
heads = 0
tails = 0
for n in range(number):
    if random.random() <= .5:
        heads += 1
        print('Flip ' + str(n + 1) + ': heads')
    else:
        tails += 1
        print('Flip ' + str(n + 1) + ': tails')
print('Total number of heads:', heads)
print('Total number of tails:', tails)
