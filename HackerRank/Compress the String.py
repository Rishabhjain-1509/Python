Name = str(input())

for i in Name:
    print(i)
    Count = 0
    for j in Name:
        if i == j:
            Count = Count + 1
        else:
            break
    print(Count)
