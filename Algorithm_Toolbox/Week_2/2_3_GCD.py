def GCD(Num1,Num2):
    if(Num2 == 0):
        return Num1
    else:
        Rem = Num1 % Num2
        return GCD(Num2,Rem)

Num1,Num2 = input().split()
Num1 = int(Num1)
Num2 = int(Num2)

print(GCD(Num1,Num2))
