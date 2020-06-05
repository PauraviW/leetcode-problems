c = 'AB'
c = "ZY"
c = "AZY"
# c = 'CX'
import string
letters = string.ascii_uppercase
column = 0
for i,data in enumerate(reversed(c)):

    column += pow(26, i) * (letters.index(data)+1)
print(column)
