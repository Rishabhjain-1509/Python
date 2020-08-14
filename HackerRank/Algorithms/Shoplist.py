num_of_shose = int(input())

size_of_shose = list(map(int,input().split()))

num_of_constmer = int(input())

Sum = 0

for i in range(num_of_constmer):
    const_price = list(map(int,input().split()))
    
    if(const_price[0] in size_of_shose):
        Sum = Sum + const_price[1]
        size_of_shose.remove(const_price[0])

print(Sum)