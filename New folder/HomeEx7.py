A = list()
B = list()

for i in range(0,9):
	A.append(int(input("ENTER THE number in first list ")))
	
for i in range(0,9):
	B.append(int(input("ENTER THE number in Second list ")))

C = list()

C = A + B




for i in range(len(C)):
	for j in range(len(C)-1):
		if C[j] > C[j+1]:
			temp = C[j]
			C[j] = C[j+1]
			C[j+1] = temp


print(C)