from collections import defaultdict

items = [['product1', 'product2'], ['product3', 'product2'], ['product5', 'product6']]

from collections import defaultdict


def findLargestGroup(items: List[List[str]]) -> List[str]:
    adjacencyGraph = defaultdict(list)

    for products in items:
        for i in range(len(products)):
            if i == 0:
                mainProduct = products[i]
            else:
                adjacencyGraph[mainProduct].append(products[i])
                adjacencyGraph[products[i]].append(mainProduct)
    visited = set()

    def dfs(curr, path=[]):

        for nei in adjacencyGraph[curr]:
            if nei not in visited:
                visited.add(nei)
                path = dfs(nei, path + [nei])
        return path

    ans = None
    maxLen = 0
    for product in adjacencyGraph.keys():
        if product not in visited:
            visited.add(product)
            path = dfs(product, [product])

            if len(path) > maxLen:
                ans = path
                maxLen = len(path)
    return ans
print(findLargestGroup(items))