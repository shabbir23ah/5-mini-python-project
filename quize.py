print ("Welcome to Quize")

playing = input ("Do you want to play? \n")

if playing.lower()!="yes":
    quit()


print ("Let's play the quize ")

score = 0

answer = input ("What does CPU stand for? \n ")

if answer.lower() == "central processing unit":
    print ("Correct Answer")

    score += 1


else:
    print ("Wrong Answer")



answer = input ("What does GPU stand for? \n ")

if answer.lower() == " graphics processing unit":
    print ("Correct Answer")
    score += 1

else:
    print ("Wrong Answer")



answer = input ("What does RAM stand for? \n ")

if answer.lower() == "random access memory":
    print ("Correct Answer")
    score += 1

else:
    print ("Wrong Answer")



answer = input ("What does PSU stand for? \n ")

if answer.lower() == "power supply unit":
    print ("Correct Answer")
    score += 1


else:
    print ("Wrong Answer")


print ("Your score is " + str(score) )


