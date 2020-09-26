import bisect
from collections import defaultdict

testScores = [[1,4],[2,9],[1,5],[2,8],[2,8],[1,6],[1,7],[1,8],[1,9],[1,10],[2,9.5],[2,10], [2,5]]

temp_dic = defaultdict(list)
for i, j in testScores:
    bisect.insort_left(temp_dic[i], j)
print( {i:sum(v[-5:])/5 for i, v in temp_dic.items() })
print(temp_dic)