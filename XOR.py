test_list = [4, 6, 2, 3, 8, 9] 
print("The original list is : " + str(test_list)) 
res = reduce(lambda x, y: x ^ y, test_list) 
print("The Bitwise XOR of list elements are : " + str(res)) 