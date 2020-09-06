def reverse(str, index):
    if index == len(str):
        return ""
    return reverse(str, index + 1) + str[index]

a = 'abcde'
print(reverse(a, 0))