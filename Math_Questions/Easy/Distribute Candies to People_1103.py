candies = 50
num_people = 3
l = [0]* num_people
k = 1

while candies != 0:
    print("iter",candies)
    for j in range(num_people):
        if candies < k:
            print("end", j, l[j], k, candies)
            l[j] +=candies
            candies = 0
            break
        else:
            print("mid", j,l[j],k,candies)
            l[j] += k
            candies -=k
            k = k+1

print(l)



