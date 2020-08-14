Num = list(map(int,input().split()))

A = list()

while len(Num) != 0:
    Max = max(Num)
    Num.remove(Max)
    A.append(Max)

print(A)
