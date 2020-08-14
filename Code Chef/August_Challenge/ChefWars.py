from sys import stdin, stdout 

def Health(h,p):
    while(h > 0):
        if(p != 0):
            h = h - p
            p = p/2
        else:
            return(0)
            break
            
    if(h <= 0):
        return(1)

try:
    test_case = input() 
    for i  in range(int(test_case)):
        h, p = stdin.readline().split(" ")
        h = int(h)
        p = int(p)
        stdout.write(str(Health(h,p))+"\n")
except EOFError as e:
    print(end="")