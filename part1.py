import random

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
moods = ["Happy", "Sad", "Energetic", "Calm"]
time_of_day = ["Morning", "Afternoon", "Evening"]
# random_moods = random.choice(moods)
for i in range(len(week)):
    for time in time_of_day:
        print("On ", week[i] + " " + (time) + " you were feeling ",(random.choice(moods)))

timer = 10
while timer > 0:
    print(timer)
    timer-=2

print("times up")
