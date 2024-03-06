#This program generates a random number from 1 to 100 and checks if its a prime number
#See if you can find the errors in it

import random

not_prime = False

random_number = random.randint(1,10):
if (random_number > 1):
    for i in range(2,random_number):
        if random_number % i = 0:
            not_prime = True
            break

if not_prime = False:
    print("This number is a prime")
elif:
    print("This number is not a prime")