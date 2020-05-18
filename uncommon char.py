test_str1 = 'kletech'
test_str2 = 'kletechuniversity'
print ("The original string 1 is : " + test_str1) 
print ("The original string 2 is : " + test_str2) 
res = set(test_str1).symmetric_difference(test_str2) 
print ("The string uncommon elements are : " + str(res)) 
