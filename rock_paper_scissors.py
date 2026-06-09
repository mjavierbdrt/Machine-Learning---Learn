import random

print("""===================
         Rock Paper Scissors
         ===================
         
         1) ✊
         2) ✋
         3) ✌️
         """)
choose = int(input("Pick Your Number: "))
enemy = random.randint(1, 3)
print(enemy)

if choose == 1 and enemy == 1:
    print("Draw")
elif choose == 1 and enemy == 2:
    print("You Lose")
elif choose == 1 and enemy == 3:
    print("You Won!")
elif choose == 2 and enemy == 2:
    print("Draw!")
elif choose == 2 and enemy == 1:
    print("You Won!")
elif choose == 2 and enemy == 3:
    print("You Lose!")
elif choose == 3 and enemy == 3:
    print("Draw!")
elif choose == 3 and enemy == 1:
    print("You Lose")
elif choose == 3 and enemy == 2:
    print("You Won!")
else:
    print("error")

