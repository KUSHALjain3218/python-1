import random



random = random.randint(1,9) 
chances = 0
while chances<5:
    
    guess = int(input("guess"))
    
    if (guess == random):
        print("good")
        break
    elif (guess>random):
        print("random is a smaller number")
    
    else:
        print("random is a bigger  number")
    chances = chances+1
   
if(chances==5):
    print("you lost")    
    
   