import collections
from typing import List


class DisjointSet:
    def __init__(self):
        # 由于节点数量的不确定性，不在此处进行初始化，每次merge前进行find时，添加进father 字典(i: i)
        self.father = {}
        # cnt 代表连通图的个数，每加一个独立节点 加一，每当节点连通 减一。
        self.cnt = 0

    def add(self, x):
        # 添加一个节点，该节点父节点应该为空
        if x not in self.father:
            self.father[x] = None

    def find(self, x):

        if x not in self.father:
            self.cnt += 1
            self.father[x] = x
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
            self.cnt -= 1


if __name__ == '__main__':
    def removeStones(stones: List[List[int]]) -> int:
        n = len(stones)
        uf = DisjointSet()
        for i in range(n):
            # 加10001映射横坐标，单靠一个坐标来确定不同的点。
            uf.merge(stones[i][0] + 10001, stones[i][1])
        print(uf.father)
        return n - uf.cnt


    stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    print(removeStones(stones))
