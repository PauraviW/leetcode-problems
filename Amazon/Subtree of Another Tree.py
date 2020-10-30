def checkTree(s, t):
    if not s and t or not t and s:
        return False
    if s.val == t.val:
        return checkTree(s.left, t.left) and checkTree(s.right , t.right)
    return True

def traverse(s, ans):
    if not s:
        return
    if s.val == t.val:
        ans = ans or checkTree(s, t)
    else:
        return traverse(s.left, ans) or traverse(s.right, ans)
    return ans
def check(s, t):
    if not s and t or not t and s:
        return False
