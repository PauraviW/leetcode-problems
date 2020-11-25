text = 'bcdbab'
pat = 'abcdbab'
def commonPrefixSum(s):
    pa = [0] * len(s)
    left, right = 0, 0

    for i in range(0, len(s)):
        if i<=right:
            if pa[i-left] < right - i +1:
                pa[i] = pa[i-left]
            else:
                left=i
                while right < len(s) and s[right-left] == s[right]:
                    right = right+1
                pa[i] = right-left
                right = right - 1
        else:
            left = i
            right = i
            while right<len(s) and s[right-left] == s[right]:
                right = right + 1
            pa[i] = right-left
            right = right - 1
    total_sum = len(s)
    for i in range (1, len(s)):
        total_sum = total_sum + pa[i]
    return total_sum

print(commonPrefixSum('aaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))


def computeLPS(pat, m):

    leng = 0
    i = 1

    lps = [0]*m

    while i < m:
        if pat[i] == pat[leng]:
            lps[i] = leng + 1
            i += 1
            leng += 1
        else:
            if leng != 0:
                leng = lps[leng - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


text = 'aaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
pat = 'aaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

n = len(text)
m = len(pat)

lps = [0] * m
lps = computeLPS(pat, m)


i = 0
j = 0
total = 0
while i < n:
    if text[i] == pat[j] and i != 0:
        i += 1
        j += 1
    else:
        if j != 0:
            # find common_prefix here
            total += j
            j = lps[j-1]
        else:
            i += 1
print(total + j + len(pat))
    # if j == m:
    #     print(i-j)
    #     j = lps[j - 1]
