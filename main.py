import random

def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None
    
    # Check for all possibilities when computer chose Rock(r)
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
        
    # Check for all possibilities when computer chose Paper(p)
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
        
    # Check for all possibilities when computer chose Scissorp(s)
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False
        

print("Computer Turn: Rock(r) Paper(p) or Scissor(s)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'


you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")