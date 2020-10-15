s = 'harry said, "What a lovely weather!" , to hermione'

import  re
regex = '\"([^\"]*)\" '
regex = '\"([^\"]*)\" '
x = re.findall(regex, s)

print(x)
