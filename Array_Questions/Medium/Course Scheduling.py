from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        dic = defaultdict(set)
        courses_as_preq = []
        for c, p in prerequisites:
            dic[c].add(p)
            courses_as_preq.append(p)
        if not dic:
            return [i for i in range(numCourses)]

        # course not present
        start = None
        result = []
        if list(set(courses_as_preq) - set(dic.keys())):
            start = list(set(courses_as_preq) - set(dic.keys()))[0]
            result = [start]
        temp = 0
        while dic and temp != len(dic):
            temp = len(dic)
            for c,p in dic.items():

                if len(p - set(result)) == 0:
                    result.append(c)
            for c in result:
                if c in dic:
                    del dic[c]
        return result

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
numCourses = 1
prerequisites = []
numCourses = 2
prerequisites = [[0,1],[1,0]]
print(Solution().findOrder(numCourses, prerequisites))