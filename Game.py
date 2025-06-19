import random
while(True):
    choice=int(input("1.Play\n2.Exit\n"))
    if(choice==2):
        break
    else:
        num=random.randint(1,100)
        count=1  
        guess=-1
        while(guess!=num):
            guess = int(input("Enter your guess\n"))
            if(guess>num):
                print("Guess lower")
                count=count+1
            elif(guess<num):
                print("Guess higher")
                count=count+1
        print(f"Wohooo!, You guessed the number {num} correctly in {count} attempts")

            


