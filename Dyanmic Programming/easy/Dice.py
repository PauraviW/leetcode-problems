from collections import defaultdict

n = 3
count = 0
dic = defaultdict(int)

def calc(sum, count, dic):
    if sum <=0:
        return 0
    # if sum in dic:
    #     return dic[sum]
    for i in range(1,7):
        if sum >=i:
            if sum - i == 0:
                count += 1
                # dic[sum] = count
            else:
                count = calc(sum - i, count, dic)
    return count
    # return count
print(calc(5, count,dic))