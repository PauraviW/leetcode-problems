S = 'abaaaaa'
B = [10, 15, 56, 233, 12, 123, 2]
i = 0
cost = 0
i = 0
while i < len(S) - 1:
    if S[i] == S[i + 1]:
        if B[i] < B[i + 1]:
            cost += B[i]
            S = S[:i] + S[i + 1:]
            B = B[:i] + B[i + 1:]
        else:
            cost += B[i + 1]
            S = S[:i + 1] + S[i + 2:]
            B = B[:i + 1] + B[i + 2:]

    else:
        i += 1
# return cost
print(cost)