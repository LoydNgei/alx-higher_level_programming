#!/usr/bin/python3
'''Print the sum of multiples of 3 and 5 in the range 1 to 100'''

Total = 0
for i in list(range(1, 100)):
    if i % 3 == 0 or i % 5 == 0:
        Total += i
print(Total)
