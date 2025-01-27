import random
# 1 for stone 
# 0 for paper
# -1 for scissors
bot= random.choice([-1,0,1])
print("s for stone,sc for scissor,p for paper")
younum=input("enter the your chioce ")
yourDict={"s":1,"p":0,"sc":-1}
revdict={1:"stone",0:"paper",-1:"scissors"}
youstr = yourDict[younum]
print(f"your choice is {revdict[youstr]} \n computer choice is {revdict[bot]}")

if(bot==youstr):
    print("Draw:|")    
else:
    if(bot==-1 and youstr==1):
        print("you win:)")
    elif(bot==-1 and youstr==0):
        print("you lose!")
    elif(bot==0 and youstr==-1):
        print("you lose!")
    elif(bot==0 and youstr==1):
        print("you win:)")
    elif(bot==1 and youstr==-1):
        print("you win:)")
    elif(bot==1 and youstr==0):
        print("you lose!")
    else:
        print("somehting went wrong")