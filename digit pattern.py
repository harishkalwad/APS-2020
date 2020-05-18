def pattern(n): 

    for i in n: 
  
        # print | for every line 
        print("|", end = "") 
  
        # print i number of * s in  
        # each line 
        print("*" * int(i))    
n = "41325"
pattern(n) 