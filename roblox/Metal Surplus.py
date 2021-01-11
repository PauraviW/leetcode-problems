
def get_profit(rods, sz, cpc, sl):
    profit = 0
    for r in rods:
        rodProf = 0

        if r%sz == 0:
            rodProf += ((r/sz) * sz * sl) - (r/sz - 1) * cpc
        else:
            rodProf += ((r/sz) * sz * sl) - (r/sz) * cpc

        if rodProf > 0:
            profit += rodProf

    if profit == 1913:
        return sz


    return profit


n = input()

cpc = input()
sl = input()

v = [0] * n

maxlen = 0
for i in range(n):
    v[i] = input()
    maxlen = max(maxlen, v[i])


ret = 0
for sz in range(maxlen+1):
    prof = get_profit(v, sz, cpc, sl)
    ret = max(prof, ret)
print(ret)
# cout <<ret << endl;
# return 0;
# }