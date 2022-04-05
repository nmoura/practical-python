# bounce.py
#
# Exercise 1.5
last_bounce = 100 * 3/5
for drop in range(1, 11):
    print(drop, round(last_bounce, 4))
    last_bounce = last_bounce * 3/5
