"""
@author: Arpit Somani
"""

import random
doors = [0]*3
goatdoor = [0]*2
swap = 0   #no. of swap wins
dont_swap = 0  #no. of don't swap wins
j=0
while(j<10):
    x=random.randint(0,2)   #xth door will comprise of BMW
    doors[x]= "BMW"
    for i in range (0,3):
        if (i==x):
            continue
        else:
            doors[i]= "Goat"
            goatdoor.append(i)
            choice=int(input("Enter your choice:"))
            door_open=random.choice(goatdoor)
            while(door_open==choice):
                door_open=random.choice(goatdoor)
            ch=input("Do you want to swap? (y/n)")
            if(ch=='y'):
                if(doors[choice]=='Goat'):
                    print("WOW! Player wins a BMW")
                    swap=swap+1
                else:
                    print("OOPS! Player lost, you got a Goat")
                    
            else:
                if(doors[choice]=='Goat'):
                    print("OOPS! Player lost, you got a Goat")
                else:
                    print("WOW! Player wins a BMW")
                    dont_swap=dont_swap +1

            j=j+1
print()
print("=> No.of wins after swapping:",swap)
print("=> No.of wins without swapping:",dont_swap)