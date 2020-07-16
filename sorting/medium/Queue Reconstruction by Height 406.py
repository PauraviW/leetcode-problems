from collections import defaultdict


class Solution:
    def reconstructQueue(self, people: [[]]) -> [[]]:
        # root node - the one that has 0 people in front of it who have a height greater than or equal to his/hers and if there are multiple then he/she will have the minumum height amongst them
        sorted_list = sorted(people, key=lambda k:(-k[0], k[1]))
        print(sorted_list)
        result = []
        for i, j in sorted_list:
            result.insert(j, [i,j])

        return result






val = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(Solution().reconstructQueue(val))




