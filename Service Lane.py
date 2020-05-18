N, T = map(int, raw_input().split())
arr = map(int, raw_input().split())
for i in range(T):
    index = map(int, raw_input().split())
    print min(arr[index[0]: index[1]+1])
