if __name__ == "__main__" :
    num_test = int(input())

    for i in range(num_test) :
        size_set_a = int(input())
        set_a = set(map(int,input().split()))
        size_set_b = int(input())
        set_b = set(map(int,input().split()))


        print(set_a.difference(set_b))

        if len(set_a.difference(set_b)) == 0 :
            print("True")
        else:
            print("False")
            elseif("i m fucking chuitya")
