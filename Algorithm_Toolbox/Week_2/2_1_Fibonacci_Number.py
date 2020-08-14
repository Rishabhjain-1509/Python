Num = int(input())

Fib = list()

Fib.append(0)
if(Num > 0):
    Fib.append(1)

for i in range(2,Num+1):
    Fib.append(Fib[i-1] + Fib[i-2])

#listToStr = ' '.join([str(elem) for elem in Fib])
if(Num == 0):
    print(Fib[0])
elif Num == 1:
    print(Fib[1])
else:
    print(Fib[Num])


