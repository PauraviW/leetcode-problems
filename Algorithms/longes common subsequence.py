filestream = "xlopatmhaoierpt"

i1 = 0
i2 = 12

dic = {}
check = 'pathai'
ind = 0
start = 0
end = 0
subs = filestream[i1:i2+1]
for i in range(len(subs)):
    if subs[i] == check[ind]:
        if subs[i] == 'p':
            start = i
        if subs[i] == 'i':
            end = i
        ind += 1
    if ind == len(check):
        print(end - start + 1)
        break
if ind == len(check):
    print(end-start + 1)
else:
    print(0)