import copy
from typing import List


class DisjointSet:
    def __init__(self, n):
        # 初始化屋顶。 rank确定父子关系
        self.father = {n: n}
        self.count = [1] * n + [0]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if x not in self.father:
            self.father[x] = x
        # 查找根节点
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)
        if xRoot != yRoot:
            if self.rank[xRoot] < self.rank[yRoot]:
                self.father[xRoot] = yRoot
                self.count[yRoot] += self.count[xRoot]
            else:
                self.father[yRoot] = xRoot
                self.count[xRoot] += self.count[yRoot]
                if self.rank[xRoot] == self.rank[yRoot]:
                    self.rank[xRoot] += 1


if __name__ == '__main__':
    # 0代表没有砖块，1代表有砖块，2代表位于顶端的,或者两次遍历都有的"稳固砖块"
    STABLE = 2
    BRICK = 1
    NOBRICK = 0

    def isStable(grid, i, j):
        if i == 0:
            # 位于顶端必然稳定
            return True
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == STABLE:
                return True
        return False


    def hitBricks(grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # DFS.遍历到该节点的上下左右。
        def DFS(i, j):
            res = 0
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = STABLE
                res += DFS(i + 1, j) + DFS(i - 1, j) + DFS(i, j - 1) + DFS(i, j + 1) + 1
                return res
            return 0
        # 大致思路和并查集类似。第一步先敲除砖块。第二部逆序Hits补齐砖块
        # 1. 敲除砖块.无需备份，已用1，2区分是否预先敲除
        m, n, res = len(grid), len(grid[0]), []
        for x, y in hits:
            grid[x][y] -= 1

        # 将此时第一层的砖块标记为2(STABLE)
        for j in range(n):
            _ = DFS(0, j)

        for x, y in hits[::-1]:
            # 为1的砖块是代表原本就有的，为0代表原本要敲除的砖块就不存在
            grid[x][y] += 1
            if grid[x][y] == BRICK and isStable(grid, x, y):
                res.append(DFS(x, y) - 1)
            else:
                res.append(0)
        return res[::-1]
    # # 1.并查集
    # def hitBricks(grid: List[List[int]], hits: List[List[int]]) -> List[int]:
    #     m = len(grid)
    #     n = len(grid[0])
    #     temp = copy.deepcopy(grid)
    #     ds = DisjointSet(m * n)
    #     # 预先去除要敲掉的砖块
    #     for x, y in hits:
    #         temp[x][y] = 0
    #     # 添加 与屋顶连接的元素（i = 0）i
    #     for j in range(n):
    #         if temp[0][j] == 1:
    #             ds.merge(j, n * m)
    #     # 构建并查集
    #     for i in range(1, m):
    #         for j in range(n):
    #             if temp[i][j] == 1:
    #                 if temp[i - 1][j] == 1:
    #                     ds.merge(i * n + j, (i - 1) * n + j)
    #                 if j > 0 and temp[i][j - 1] == 1:
    #                     ds.merge(i * n + j, i * n + j - 1)
    #     res = []
    #     print(temp)
    #     # 逆序遍历Hits，补齐砖块。逆序补齐为了避免未计算之后的砖块对之前的砖块造成的影响
    #     for i, j in hits[::-1]:
    #         # 原位置本来就没有的砖块敲掉不会掉落任何砖块
    #         if grid[i][j] == 0:
    #             res.append(0)
    #             continue
    #         origin = ds.count[ds.find(n * m)]
    #         # 敲掉的是屋顶元素，则和屋顶相连
    #         if i == 0:
    #             ds.merge(j, n * m)
    #         for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
    #             if 0 <= x < m and 0 <= y < n and temp[x][y] == 1:
    #                 ds.merge(i * n + j, x * n + y)
    #         current = ds.count[ds.find((n * m))]
    #         res.append(max(0, current - origin - 1))
    #         temp[i][j] = 1
    #     return res[::-1]

    grid = [[1], [1], [1], [1], [1]]
    hits = [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]
    print(hitBricks(grid, hits))
