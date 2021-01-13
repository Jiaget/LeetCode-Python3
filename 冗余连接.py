from typing import List


class DisjointSet:
    def __init__(self, length):
        self.father = {i: i for i in range(1, length + 1)}
        self.depth = 0

    def add(self, x):
        # 添加一个节点，该节点父节点应该为空
        if x not in self.father:
            self.father[x] = None

    def find(self, x):
        # 查找根节点
        root = x
        while self.father[root] != root:
            root = self.father[root]
        # 路径压缩，将x到root节点之间的所有节点直接和root节点相连
        while x != root:
            origFather = self.father[x]
            self.father[x] = root
            x = origFather
        return root

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)
        if xRoot != yRoot:
            self.father[xRoot] = yRoot


if __name__ == '__main__':
    def findRedundantConnection(edges: List[List[int]]) -> List[int]:
        # len(edges)是边的个数，由题意可知，传入的图必然有且只有一个环，故而，边数即节点个数。
        ds = DisjointSet(len(edges))
        for x, y in edges:
            if ds.isConnected(x, y):
                return [x, y]
            ds.merge(x, y)

    edges = [[1, 2], [1, 3], [2, 3]]
    print(findRedundantConnection(edges))

