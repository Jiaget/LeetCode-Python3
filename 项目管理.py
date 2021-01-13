from typing import List

if __name__ == '__main__':
    # 拓扑排序的学习与应用
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # 初始化图
        gItems = {i: i for i in range(n)}
        gGroup = group
        res = list()



    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
    print(sortItems(n, m, group, beforeItems))
