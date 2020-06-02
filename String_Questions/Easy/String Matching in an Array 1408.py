# words = ["mass","as","hero","superhero"]
# words = ["leetcode","et","code"]
words = ["blue","green","bu", "blue"]
l = []
for i, data1 in enumerate(words):
    for j, data2 in enumerate(words):
        if i != j:
            if data1 in data2:
                l.append(data1)
print(list(set(l)))