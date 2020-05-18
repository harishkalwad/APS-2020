#!/bin/python3

import os
import sys


def timeConversion(s):
    time=s.split(":")
    hour=int(time[0])
    t=time[2]
    o=t[2:]
    if(hour==12 and o=="AM"):
        hour=0
    elif(hour!=12 and o=="PM"):
        hour=hour+12
    if(hour<10):
        hour="0"+str(hour)
    new_time=str(hour)+":"+str(time[1])+":"+str(t[0:2])
    return new_time 

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
