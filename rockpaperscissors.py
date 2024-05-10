import random
user=int(input("rock=0\npaper=-1\nscissors=1\nChoose a Valid Input :"))

def check(comp,user):
    if(comp==user):
        return 0
    if(comp==1 and user==-1) or (comp==0 and user==1) or (comp==-1 and user==0):
        return -1
    if(user>2):
        return 2
    return 1

comp = random.randint(-1,1)

print("You chose", user)

print("comp chose", comp)

score= check(comp,user)
if (score==2):
    print("Invalid Input")
elif (score==0):
    print("draw")
elif(score==1):
    print("you won")
elif(score==-1):
    print("You Lost")