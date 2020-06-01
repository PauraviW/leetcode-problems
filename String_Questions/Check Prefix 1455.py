sentence = "hello from the other side"
searchWord = "they"
L = len(searchWord)
for i,data in enumerate(sentence.split(' ')):
    print(data, data[0:L])
    if data[0:L] == searchWord:
        print(i+1)
        break
print(-1)
