class Solution:
    def twoCitySchedCost(self, costs: [[]]):
        total_cost = 0
        refund = []
        # cost of A
        for i,j in costs:
            total_cost += i
            refund.append(j-i)

        refund.sort()
        print(refund, total_cost)
        for i in refund:
            if i < 0:
                total_cost += i

        return total_cost








costs =  [[10,20],[30,200],[400,50],[30,20]]
print(Solution().twoCitySchedCost(costs))