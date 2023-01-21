import random
def gamewin(comp , you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True


print("Comp turn: Select Snake(s), Water(w), Gun(g).")
randomno = random.randint(1,3)
# print(randomno)
if randomno == 1:
    comp = "s"
elif randomno == 2:
    comp = "w"
elif randomno == 3:
    comp = "g"
you = input("Your turn: Choose Snake(s), Water(w), Gun(g)\n")
a =gamewin(comp , you)
print(f"Computer chose {comp}")
print(f"You chose {you}")
if a == None:
    print("It's a tie!")
elif a:
    print("You won!") 
else:
    print("You lose!")