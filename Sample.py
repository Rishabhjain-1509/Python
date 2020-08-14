def Remove(List):
    A = list()

    for i in range(int(len(List) / 2)):
        A.append(List[2 * i])

    return A


def Sum(List, Cost):
    A = list()

    for i in range(0, int(len(List) / 2)):
        List[2 * i] = (List[2 * i] + List[2 * i + 1]) * Cost

    if len(List) % 2 == 0:
        A = Remove(List)
    else:
        A = Remove(List)
        A.append(List[-1])

    return A


if __name__ == "__main__":
    Array = list(map(int, input().split()))
    Num_Array, Cost_Sum = input().split()
    Num_Array = int(Num_Array)
    Cost_Sum = int(Cost_Sum)

    while len(Array) != 1:
        Array.sort()
        Array = Sum(Array, Cost_Sum)

    Str = "".join(list(str(Array[0])))

    print(Str)
