import random

top_of_range = input ("Enter top number for range \n")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print ("Please enter greater than 0 ")
        quit()
else:
    print("Please enter a number")


random_number = random.randint(0,top_of_range)

guess = 0

while True:
    guess += 1
    guess_number = input ("Enter your guess number ")
    
    if guess_number.isdigit():

        guess_number = int (guess_number)
    
    else:
        print ("Please type a number ")
        continue


    if guess_number == random_number:
        print("You got it! ")
        break
        

    elif guess_number < random_number:
            print ("You are low")

    else:
        print("You are high")

        


print ("You had to guess",guess,"times" )

