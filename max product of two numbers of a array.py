n=int(input())
a=[int(i) for i in input().split()]
m=max(a)
a.remove(m)
m=m*max(a)
print(m)
