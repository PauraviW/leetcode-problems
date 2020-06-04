from collections import defaultdict
s = "HOW ARE YOU"
s = "CONTEST IS COMING"
# s = "TO BE OR NOT TO BE"
words = s.split(' ')
d = defaultdict(str)
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

for word in words:
    i = 0
    while i < len(longest_word):
        if i > len(word) - 1 :
            d[i]+=" "
        else:
            d[i]+=word[i]
        i += 1


print([i.rstrip() for i in d.values()])