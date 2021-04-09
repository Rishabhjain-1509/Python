n = int(input())
marksheet = [input().split() for _ in range(n)]
Result = {}

for i in range(n):
    avg = (float(marksheet[i][1]) + float(marksheet[i][2]) + float(marksheet[i][3]))/3

    Result[marksheet[i][0]] = "{:.2f}".format(avg)

print(Result)

find = input()

print(Result[find])