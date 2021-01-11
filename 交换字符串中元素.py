import collections
from typing import List


class DisjointSet:
    def __init__(self, s):
        self.father = {i: i for i in range(len(s))}
        # self.length = 0

    # add 方法添加了父节点为空的独立节点
    def add(self, x):
        # 添加一个节点，该节点父节点应该为空
        if x not in self.parent:
            self.parent[x] = None

    def find(self, x):
        # 查找根节点
        root = x
        # 该判断语句和初始化并查集有关
        # 初始化集合中，节点的父节点是其本身。
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

    # merge方法将两个节点关联在一起
    def merge(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)
        if xRoot != yRoot:
            self.father[xRoot] = yRoot


if __name__ == '__main__':
    # 2. DFS做法
    def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:


    # # 1. 此题中pairs中所有节点对之间联通起来，是连通性问题，使用并查集
    # def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    #     # 创建并查集
    #     ds = DisjointSet(s)
    #     for x, y in pairs:
    #         ds.merge(x, y)
    #     # 使用Key可为空的list字典[(key, value), ...]
    #     connectNode = collections.defaultdict(list)
    #     for node in range(len(s)):
    #         # 记录root节点下所有相关联节点
    #         connectNode[ds.find(node)].append(node)
    #
    #     # 将字符串转换成列表
    #     res = list(s)
    #
    #     # 可以将pairs整理成多个（或者1个）连通图。
    #     # 针对不同的连通图(索引区间)内进行字符串排序
    #     for nodes in connectNode.values():
    #         # index中记录本回参与排序的字符串索引(即构成一个连通图的节点)
    #         index = nodes
    #         # 仅将字符串在index列表中的索引范围内进行排序
    #         string = sorted(res[node] for node in nodes)
    #         # index 和 string 是两个列表，将其压缩成一个元组，并组成新的列表。
    #         for i, ch in zip(index, string):
    #             res[i] = ch
    #     return "".join(res)


    s = "dcab"
    pairs = [[0,3],[1,2],[0,2]]
    print(smallestStringWithSwaps(s, pairs))
