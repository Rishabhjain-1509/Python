Ar = list()


num = int(input("Enter the number upto which you want to print = "))

Ar.append(int(0))
Ar.append(int(1))


#for i in range(2,num):
	Ar[i] = Ar[i-1] + Ar[i-2]
	
print(Ar)