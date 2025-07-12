print("welcome to my computer quiz!")

playing=input("do you to wnat to play?:")
if playing.lower()!="yes":
    quit()
print("Okay! Let's play:)") 
score=0

answer=input("which year is going on?")
if answer.lower()=="2025":
    print('correct!')
    score+=1
else:
    print('incorrect!')    

answer=input("you are a human?")
if answer.lower()=="yes":
    print('correct!')
    score+=1
else:
    print('incorrect!')    

answer=input("What does the PSU stand for?")
if answer.lower()=="power supply unit":
    print('correct!')
    score+=1
else:
    print('incorrect!')    

answer=input("What does the CPU stand for?")
if answer.lower()=="central processing unit":
    print('correct!')
    score+=1
else:
    print('incorrect!')                

print(f"total score is {score}")    