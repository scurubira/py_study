#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

#Sun 10 May 2015 13:54:36 -0700
#Sun 10 May 2015 13:54:36 -0000


# Complete the time_delta function below.
def read_datetime():
    return datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')


# def time_delta(t1, t2):
def main():
    t = int(input())

    for _ in range(t):
        t1 = read_datetime()
        t2 = read_datetime()
        print(int(abs(t1 - t2).total_seconds()))


if __name__ == '__main__':
    main()
