words = ["Hello", "Alaska", "Dad", "Peace"]

x = []
k = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
for ele in words:
    for i in k:
        if set(ele.lower()).issubset(i):
            x.append(ele)
print(x)