
def Chefs_pawn(P,N):
    Dis = {}
    for i in N:
        if(P%i == 0):
            count = 0
            Sum = 0
            while(Sum != P):
                Sum = Sum + i
                count = count + 1

            Dis[i] = count
        
    if(len(Dis) != 0):
        Max = min(Dis, key=Dis.get)
    else:
        Max = -1
        
    return (Max)

try:
    test_case = input() 
    for i in range(int(test_case)):
        P = list(map(int,input().split()))
        N = list(map(int,input().split()))
    
        print(Chefs_pawn(P[1],N))
        
except EOFError as e:
    print(end="")



    
    