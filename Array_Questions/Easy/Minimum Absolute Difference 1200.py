class Solution:
    def minimumAbsDifference(self, arr: [int]) -> [[int]]:
        arr.sort()
        d = {(arr[i],arr[i+1]): abs(arr[i]-arr[i+1]) for i in range(0, len(arr)-1)}
        min_val = min(d.values())
        l = [list(i)  for i,j in d.items() if j==min_val]
        return l










arr = [4, 2, 1, 3]
arr = [1,3,6,10,15]
arr = [3,8,-10,23,19,-4,-14,27]
print(Solution().minimumAbsDifference(arr))





