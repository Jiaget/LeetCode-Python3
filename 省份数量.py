from typing import List

if __name__ == '__main__':
    # DFS
    def DFS(i, isConnected, isVisited):
        isVisited[i] = 1
        for j in range(len(isConnected)):
            if isConnected[i][j] and not isVisited[j]:
                DFS(j, isConnected, isVisited)
        return


    def findCircleNum(isConnected: List[List[int]]) -> int:
        isVisited = [0] * len(isConnected)
        res = 0
        for i in range(len(isConnected)):
            # 在每次遍历节点前，只要该节点没被访问过，结果即加一
            # 可能的情况：
            # 1  2-3 或者 1-2 3
            if isVisited[i] == 0:
                res += 1
                DFS(i, isConnected, isVisited)
        return res


    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(findCircleNum(isConnected))
