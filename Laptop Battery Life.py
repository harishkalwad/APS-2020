#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput

if __name__ == '__main__':
    used_time = float(input())
    if (used_time>=4.00):
        print ("8.00")
    else:
        print ("%.2f"%(used_time*2))
