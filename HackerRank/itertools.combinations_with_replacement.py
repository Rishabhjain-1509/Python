from itertools import combinations_with_replacement

if __name__ == "__main__":
    Name,Num = input().split()
    Name = list(str(Name))
    Num = int(Num)
    Name.sort()
    print(Name)
    A = list()

    S = list(combinations_with_replacement(Name, Num))
    for i in S:
        A.append("".join(i))

    A.sort()
    for i in A:
        print(i)
