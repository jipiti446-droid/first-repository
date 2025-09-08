import random

counters=[0,0,0,0,0,0]

for i in range(500):
    value=random.randint(1,6)
    counters[value-1]=counters[value-1]+1

for x in range(6):
    print(f"주사위 값이 {x+1}인 횟수 : {counters[x]}")