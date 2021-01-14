import collections
from typing import List

if __name__ == '__main__':
    # 拓扑排序的学习与应用
    # 本体除了项目之间的拓扑排序之外，还有分组。对于一个拓扑内的节点，可能存在多组区分。
    # 因此除了简单的拓扑排序之外，还需要进行分组。
    def sortItems(n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # ----初始化----
        indegrees_inGroup = collections.defaultdict(int)  # 组内入度
        indegrees_betweenGroup = collections.defaultdict(int)  # 组间入度
        neighbours_inGroup = collections.defaultdict(list)  # 组内依赖
        neighbours_betweenGroup = collections.defaultdict(list)  # 组间依赖 beforeItem的组号：[其他组Item的组号]
        groups = collections.defaultdict(list)  # group 字典化 组号:[items...]
        res = []

        # 将没分组的元素各自为一组，从m开始编号避免和已分组的发生冲突
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            groups[group[i]].append(i)
        # 维护组内组间的入读与图依赖关系, i为当前节点，pre为前置节点
        for i in range(n):
            for pre in beforeItems[i]:
                if group[i] == group[pre]:
                    indegrees_inGroup[i] += 1
                    neighbours_inGroup[pre].append(i)
                else:
                    indegrees_betweenGroup[group[i]] += 1
                    neighbours_betweenGroup[group[pre]].append(group[i])
        # ----排序----
        # 组间排序
        res_betweenGroup = bfs([group for group in range(m)], indegrees_betweenGroup, neighbours_betweenGroup)
        if len(res_betweenGroup) != m:
            return []  # 检查组间排序，如果排序前后长度不等，说明失败。

        # 根据组间排列的顺序进行组内排序
        for i in res_betweenGroup:
            res_inGroup = bfs(groups[i], indegrees_inGroup, neighbours_inGroup)
            res += res_inGroup

        return res if len(res) == n else []  # 检查排序前后长度

    # BFS排序，使用队列
    def bfs(items, indegrees, neighbours):
        que = collections.deque()
        res = []
        for item in items:
            # 入度为0的（节点或者组）排在前面
            if indegrees[item] == 0:
                que.append(item)
        while que:
            first = que.popleft()
            res.append(first)
            for n in neighbours[first]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    que.append(n)
        return res


    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
    print(sortItems(n, m, group, beforeItems))
