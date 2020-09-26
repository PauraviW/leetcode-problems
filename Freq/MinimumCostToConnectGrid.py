import string
class DisjointSet:
    def __init__(self):
        self.parent = []
        self.rank = []


    def make_set(self, node):
        self.parent.append(node)
        self.rank.append(0)


    def find(self, node):
        if self.parent[node] == node:
            return node
        # path compression as we search for node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]


    def union(self, p, q):
        # find root components of each node
        parentp = self.find(p)
        parentq = self.find(q)

        if self.rank[parentp] >= self.rank[parentq]:
            # increment rank iff both have same rank
            self.rank[parentp] += self.rank[parentp] == self.rank[parentq]
            self.parent[parentq] = parentp
        else:
            self.parent[parentp] = parentq

def kruskals(connection, num):
    """
    Kruskal's Algorithm

    Time: O(ElogE) where E is the number of edges
    Space: O(E)
    """
    result = []

    # map characters to indices
    ascii_map = {c: i for i, c in enumerate(string.ascii_uppercase)}

    # sort all the edges from low weight to high
    G = sorted(connection, key=lambda x: x[2])

    # build disjoint set
    djs = DisjointSet()
    for node in range(num):
        djs.make_set(node)

    # Take the edge with the lowest weight and add it to the spanning tree.
    # If adding the edge created a cycle, then reject this edge.
    i, e = 0, 0
    while e < num - 1:
        u, v, w = G[i]
        i += 1

        parentu = djs.find(ascii_map[u])
        parentv = djs.find(ascii_map[v])

        if parentu != parentv:
            e += 1
            result.append([u, v, w])
            djs.union(ascii_map[u], ascii_map[v])

    return result


if __name__ == "__main__":
    for args in (
        (
            [["A", "B", 1],
             ["B", "C", 4], ["B", "D", 6], ["D", "E", 5], ["C", "E", 1]],
            5,
        ),
    ):
        print(kruskals(*args))