
def Sum(List, Cost):
    A = list()

    while len(List) != 0:
        Min1 = min(Array)
        Array.remove(Min1)
        Min2 = min(Array)
        Array.remove(Min2)
        A.append((Min1+Min2)*Cost_Sum)

    return A



if __name__ == "__main__":
    Array = list(map(int, input().split()))
    Num_Array, Cost_Sum = input().split()
    Num_Array = int(Num_Array)
    Cost_Sum = int(Cost_Sum)
    A = list()

    while len(Array) != 1:
        Array = Sum(Array, Cost_Sum)

    print(Array)
