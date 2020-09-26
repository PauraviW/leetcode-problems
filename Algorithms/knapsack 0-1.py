def brute_force(w,p,capacity):
    l = []

    for i in range(len(w)):
        profit,c = 0, capacity
        for j in range(len(w)):
            if i != j and c >=w[j]:
                profit += p[j]
                c = c - w[j]
        l.append(profit)
    print(max(l))

w = [5,3,4,2]
p = [69,50,70,30]
brute_force(w,p,5)