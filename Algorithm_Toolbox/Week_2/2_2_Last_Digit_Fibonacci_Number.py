Num = int(input())

Fib = list()

Fib.append(0)
if(Num > 0):
    Fib.append(1)

for i in range(2,Num+1):
    Fib.append(Fib[i-1] + Fib[i-2])

Str = list(str(Fib[-1]))

print(int(Str[-1]))
