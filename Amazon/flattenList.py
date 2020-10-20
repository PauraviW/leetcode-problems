def dfs(nums, l):

    for i in range(len(nums)):
        if type(nums[i]) == int:
            l.append(nums[i])
        else:
            dfs(nums[i], l)
    return l

l = [1,[2,3],[2,[4,5]]]

ans = dfs(l, [])

print(ans)