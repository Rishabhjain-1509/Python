F = [0, 1]
last = [0, 1]
for i in range(2, 60):
    F.append(F[i - 1] + F[i - 2])
    last.append(int(str(F[i])[-1]))

n = int(input())
S = last[n % 60] * last[n % 60] + last[n % 60] * last[(n - 1) % 60]

print(S % 10)
