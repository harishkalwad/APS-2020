#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    count = 0
    print(list(str(n)))
    for i in list(str(n)):
        if int(i) != 0 and n % int(i) == 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = f#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e=100
    energy=0
    i=0
    while(i!=len(c)):
        if(c[i]==1):
            energy=e-3
            e=energy
        else:
            energy=e-1
            e=energy
        i+=k
    return energy
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')
#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int p[n+1];
    for(int i=1; i<=n; i++){
        int k;
        cin >> k;
        p[k]=i;
    }
    for(int i=1;i<=n;i++){
        cout << p[p[i]] << endl;
    }
    return 0;
}

indDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
