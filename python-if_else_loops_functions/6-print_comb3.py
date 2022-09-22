#!/usr/bin/python3
for num1 in range(8):
    num2 = num1 + 1
    while num2 < 10:
        print("{}{}".format(num1, num2), end=', ')
        num2 += 1
print("{}{}".format(num1+1, num2-1))
