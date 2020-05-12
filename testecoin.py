#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    total = 0
    for i in range(len(ar)):
            total += ar[i]
    return total

if __name__ == '__main__':
    #fptr = open(os.environ['c:/teste'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
