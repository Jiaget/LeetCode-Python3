class DisjointSet:
    def __init__(self):
        self.father = {}
        self.length = 0

    def add(self, x):
        # 添加一个节点，该节点父节点应该为空
        if x not in self.parent:
            self.parent[x] = None

    def find(self, x):
        # 查找根节点
        root = x
        while self.father[root]:
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
