import math;

anime = input()
duration = int(input())
totalTime = int(input())

lunchTime = totalTime / 8
restTime = totalTime / 4
remain = totalTime - lunchTime - restTime

if remain >= duration:
    print(f'You have enough time to watch {anime} and left with {math.ceil(totalTime - remain - lunchTime - restTime)} minutes free time.')
else:
    print(f"You don't have enough time to watch {anime}, you need {math.ceil(duration - remain)} more minutes.")