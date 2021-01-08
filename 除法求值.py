from collections import defaultdict
from typing import List

if __name__ == '__main__':
    # (2)

    # 除法求值。由a/b = 2.0 + b/c = 3.0 => a/c = 6.0 (1) 推算得出使用带权图来解决。
    # 此题转换成有向图中两点之间的最短路径
    # 使用字典(映射)和集合(去重)实现带权图
    # def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    #     n = len(equations)
    #     graph = defaultdict(int)
    #     # 用来存储所有节点.
    #     arr = set()
    #     # 生成有向图
    #     for i in range(n):
    #         a, b = equations[i]
    #         graph[(a, b)] = values[i]
    #         graph[(b, a)] = 1 / values[i]
    #         arr.add(a)
    #         arr.add(b)
    #     # 弗洛伊德(Floyd)算法
    #     for i in arr:
    #         for j in arr:
    #             for k in arr:
    #                 if graph[(j, i)] and graph[(i, k)]:
    #                     graph[(j, k)] = graph[(j, i)] * graph[(i, k)]
    #     res = list()
    #     for p, q in queries:
    #         if graph[p, q]:
    #             res.append(graph[p, q])
    #         else:
    #             res.append(-1)
    #     return res


    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(calcEquation(equations, values, queries))


