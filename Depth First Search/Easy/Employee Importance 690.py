from collections import defaultdict
class Solution:
    def getImportance(self, employees: [], id: int) -> int:

        importance = defaultdict(int)
        subbordinates = defaultdict(list)

        for id, imp, subbo in employees:
            importance[id] = imp
            subbordinates[id] = subbordinates[id] + subbo
        print(importance, subbordinates)
















data =  [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
emp_id = 1
print(Solution().getImportance(data, emp_id))
