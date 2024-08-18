#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2:] == 'AM':
        if s[0:2] == '12':
            s[0:2] == '00'
    elif(s[-2:] == 'PM'):
        if s[0:2] != '12':
            hour = int(s[0:2])
            hour += 12
            hour = str(hour)
            s = hour + s[2:] 
    return s[:-2]

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)

