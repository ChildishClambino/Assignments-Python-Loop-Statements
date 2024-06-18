import random
options = ["red", "blue", "yellow", "green"]
answer = random.choice(options)

for attempts in range(3):
    guess = input("guess what color I am thinking about red blue yellow green ")
    if guess == answer:
        print("well played! ")
        break
    else:
        print("try again")
else:
    print("you failed!")