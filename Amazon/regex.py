s = 'aa'
p = 'a'



def dfs(curr, prev, index):
    if index == len(p):
        return True
    if index > len(p):
        return False
    