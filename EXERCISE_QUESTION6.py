#Virtual coin toss program that simulates a coin toss and displays the result.

import random
side=random.randint(0,1)
print(side)
if (side == 1):
    print("Heads")
else:
    print("Tails")