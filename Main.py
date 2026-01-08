import random
'''
1 for snake
-1 for water
0 for Gun
'''
computer=random.choice([1,0,-1])
youstr=   "S"             # random.choice(["S","W","G"]) , input("Enyter Your Choise: ")
YouDict={"S":1,"W":-1,"G":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}    
you=YouDict[youstr]

print(f"You chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer==you):
    print("Its Draw")
else:
    if(computer==-1 and you==1):
        print("You Win")
    elif(computer==-1 and you==0):
        print("You Lose")
    elif(computer==1 and you==-1):
        print("You Lose")
    elif(computer==1 and you==0):
        print("You Win")
    elif(computer==0 and you==1):
        print("You Win")
    elif(computer==0 and you==-1):
        print("You Lose")
    else:
        print("Something went wrong")
        


 

      
        