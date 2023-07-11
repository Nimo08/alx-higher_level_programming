#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = int(str(number)[-1])
print(f"Last digit of {number} is {last_num}", end=" ")
if last_num > 5:
    print(f"and is greater than 5")
elif last_num == 0:
    print(f"and is 0")
elif last_num < 6 and last_num != 0:
    print(f"and is less than 6 and not 0")
else:
    print("Invalid number")
