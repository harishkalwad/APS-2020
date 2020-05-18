test_list = ['gfg', 'is', 'best', 'for', 'geeksc'] 
print("The original list is : " + str(test_list)) 
temp =  {idx : len(set(idx)) for idx in test_list} 
res = max(temp, key = temp.get) 
print ("The string with most unique characters is : " + str(res)) 
