# s = "abbcccddddeeeeedcba"#
# s = "leetcode"
s = s = "triplepillooooow"
s = "hooraaaaaaaaaaay"
s = "tourist"
count = 0
max  = 0
i = 1
while i < len(s):
    if s[i] == s[i-1]:

        count +=1
        if count > max:
            max = count
    else:
        count = 0

    i = i + 1

print(max+1)