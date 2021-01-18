import collections
from typing import List


class DisjointSet:
    def __init__(self):
        self.father = {}
        self.depth = 0

    def add(self, x):
        # 添加一个节点，该节点父节点应该为空
        if x not in self.father:
            self.father[x] = None

    def find(self, x):
        if x not in self.father:
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


if __name__ == '__main__':
    def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
        ds = DisjointSet()
        emailToIndex = dict()
        res = list()
        i = 0
        # <--1-->制作[account:eamil]字典
        for account in accounts:
            # 将每个账号（account）用Index表示唯一标识
            # emailToIndex = [i: email]
            emailToIndex[i] = []
            for email in account[1:]:
                emailToIndex[i].append(email)
            i += 1
        # <--2-->加入并查集
        # 将index（account）作为父节点，index（account）和email作为子节点，加入并查集
        # 由于并查集的性质，只要两个account下有相同的email,其中一个account合并到另一个account的子节点下。
        for account in emailToIndex:
            for email in emailToIndex[account]:
                ds.merge(email, account)
        # <--3-->节点合并，并将结果制作成新字典
        mergedDic = collections.defaultdict(list)
        for email in ds.father:
            ds.find(email)
            if type(email) is str:
                mergedDic[ds.father[email]].append(email)
        # <--4-->字典转换列表并输出
        for i, e in mergedDic.items():
            res.append([accounts[i][0]] + sorted(e))

        return res


    # accounts = [["John", "a", "b", "c"], ["John", "d"],
    #             ["John", "a", "e"], ["Mary", "f"]]
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    print(accountsMerge(accounts))
