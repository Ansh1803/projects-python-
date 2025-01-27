import random
def game():
    print("you playing this game")
    score= random.randint(1,100)
    
    with open("highscore.txt") as f:
        hscore=f.read()
        if(hscore!=""):
            hscore=int(hscore)
        else:
            hscore = 0
    print(f"the score is{score}")
    if(score>hscore):
        with open("highscore.txt","w") as a:
            a.write(str(score))
    return score 

game()


            




