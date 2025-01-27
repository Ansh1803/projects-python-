import random
n=random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    a=int(input("Guess the Number:"))
    if(a>n):
        print("Lower the Number ")
    elif(a<n):
        print("Higher the Number")
    guesses+=1


print(f"you have guessed the number {n} correctly in {guesses} attemps")
