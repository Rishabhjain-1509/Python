

d = int(input())
a = list(map(int,input().split()))

b = []
b.extend(a[d:len(a)])

b.extend(a[0:d])
print(b)
