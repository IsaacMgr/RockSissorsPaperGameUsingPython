import random

def gameWin(comp, you):
    if comp == you:
        return None
    if comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    if comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
    if comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False

randNo = random.randint(1,3)
print(randNo)
print("Comp Turn: Rock(r) Scissors(s) or Paper(p)")
if randNo == 1:
    comp= 'r'
elif randNo == 2:
    comp= 's'
elif randNo == 3:
    comp= 'p'





you = input("Your Turn: Rock(r) Scissors(s) or Paper(p) ")
a = gameWin(comp, you) 

print(f"Computer choose {comp}")
print(f"You choose {you}")
if a == None:
    print("The game is a tie")
elif a:
    print("You win")
else:
    print("You lose")