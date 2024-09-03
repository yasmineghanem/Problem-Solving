#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def arrayManipulation(n, queries):
    # Write your code here
    values = [0 for _ in range(n)]

    for query in queries:
        a, b, k = query

        values[a-1] += k

        if b < n:
            values[b] -= k

    # cumsum = [0 for _ in range(n)]

    # for i, value in enumerate(values):
    #     if i == 0:
    #         cumsum[i] = value
    #         continue

    #     cumsum[i] = cumsum[i-1] + value

    max_value = -math.inf
    cumsum = 0

    for value in values:
        cumsum += value
        max_value = max(cumsum, max_value)

    return max_value


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
