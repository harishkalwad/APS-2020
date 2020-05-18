def findMinSum(num): 
    sum = 0
    i = 2
    while(i * i <= num): 
        while(num % i == 0): 
            sum += i 
            num /= i 
        i += 1
    sum += num 
    return sum
num = 12
print findMinSum(num) 
  
