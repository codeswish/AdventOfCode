#!/usr/bin/env python3
<<<<<<< HEAD

from collections import Counter

=======
>>>>>>> day_03
left_right = [[], []]

with open("input.txt", "r") as f:
    for line in f:
        left_right[int(line[0])].append(line.rstrip())


# Generate range on code length starting at index 1
r = range(1, len(left_right[0][0]))

# How to find the filter left_right
# int(len(l[1]) >= len(l[0]))
codes = left_right[int(not len(left_right[1]) >= len(left_right[0]))]

# reinitialize left_right
left_right = [[], []]


for idx in r:
    for code in codes:
        left_right[int(code[idx])].append(code)

    codes = left_right[int(not len(left_right[1]) >= len(left_right[0]))]
    if len(codes) == 1:
        rating = codes[0]
        break
    left_right = [[], []]


print("CO2 Scrubber Rating: " + str(int(rating, 2)))
