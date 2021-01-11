from collections import defaultdict

def chooseAFlask(numOrders: int, requirements: [], flaskTypes: int, totalMarks: int, edges: [[]]) -> int:

    def binarySearch(value, marks):
        l = 0
        r = len(marks) - 1
        while l < r:
            mid = int((l + r) / 2)
            if marks[mid] == value:
                return value
            elif marks[mid] < value:
                l = mid + 1
            else:
                r = mid - 1
        return marks[l]


    graph = defaultdict(list)

    for flask, marking in edges:
        graph[flask].append(marking)

    maxm = max(requirements)
    minloss = float('inf')
    ans = None
    for k, v in graph.items():
        if v and v[-1] >= maxm:

            loss = 0
            for i in range(len(requirements)):
                mark = binarySearch(requirements[i], v)
                loss += mark - requirements[i]
            if loss < minloss:
                minloss = loss
                ans = k
    return ans

numOrders = 4
requirements = [4,6,6,7]
flaskTypes = 3
totalMarks  = 9
edges = [[0, 3], [0, 5],[0, 7],[1, 6],[1, 8],[1 ,9],[2 ,3],[2 ,5], [2 ,6]]
result = chooseAFlask(numOrders, requirements, flaskTypes, totalMarks, edges)
print(result)