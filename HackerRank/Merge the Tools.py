if __name__ == "__main__":
    Name = input()
    Num = int(input())

    for i in range(0, len(Name), Num):
        s = ""
        for j in Name[i : i + Num]:
            if j in s:
                continue
            else:
                s += j
        print(s)



