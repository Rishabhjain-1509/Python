import math

Num1 = int(input())
Num2 = int(input())

print(math.gcd(Num1,Num2))

def GCD(Num1,Num2):
    if(Num2 == 0):
        return Num1
    else:
        Rem = Num1%Num2
        return GCD(Num2,Rem)


Num1 = int(input())
Num2 = int(input())

GCD_Num = GCD(Num1,Num2)

print(GCD_Num)
