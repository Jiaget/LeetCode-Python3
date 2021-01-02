# @staticmethod:静态方法，静态方法是不可以访问实例变量或类变量的,这个类方法实际上跟类没有什么关系，它只是类下面的一个函数，跟类本身没关系，只是名义上归类管。
# 它与类唯一的关联就是需要通过类名来调用这个方法
# 如果非要传参数，只有传自己
# @classmethod:类方法只能访问类变量，不能访问实例变量
#
# @property :属性方法,属性方法的作用就是通过@property把一个方法变成一个静态属性

# 使用数组来模拟完全二叉树
# n的左子节点： 2 * i + 1
# n的右子节点： 2 * i + 2
# n的父母节点： (n - 1) // 2 '//'->整除
from typing import List


class Heap:
    def __init__(self, isMaxHeap: bool):
        self.isMaxHeap = isMaxHeap
        self.heap = []

    # 将方法变成静态属性
    @property
    def size(self):
        return len(self.heap)

    def top(self):
        if self.heap:
            return self.heap[0]
        return None

    def push(self, item):
        self.heap.append(item)
        self.up(self.size - 1)

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    # 将该节点向上调整
    def up(self, index):
        while index:
            parent = (index - 1) // 2
            if self.notChange(self.heap[parent], self.heap[index]):
                # 無法移動時，退出
                break
            self.swap(parent, index)
            index = parent

    # 判断是否交换（大顶堆父节点小则交换，小顶堆相反）
    def notChange(self, parent, child):
        return parent > child if self.isMaxHeap else parent < child

    # 向下移動時，需要考慮左右子節點
    def down(self, index):
        # 是否存在子節點
        while index * 2 + 1 < self.size:
            l = index * 2 + 1
            r = index * 2 + 2
            toSwap = index
            # 和左右子節點進行比較確定交換位置
            if self.notChange(self.heap[l], self.heap[toSwap]):
                toSwap = l
            if r < self.size and self.notChange(self.heap[r], self.heap[toSwap]):
                toSwap = r
            # 此時無需進行操作
            if toSwap == index:
                break
            self.swap(index, toSwap)
            index = toSwap

    def pop(self):
        toPop = self.heap[0]
        # 將堆頂和堆底調換
        self.swap(0, self.size - 1)
        self.heap.pop()
        # 由於此時堆頂元素較小，向下交換
        self.down(0)
        return toPop


if __name__ == '__main__':
    def lastStoneWeight(stones: List[int]) -> int:
        heap = Heap(isMaxHeap=True)
        for stone in stones:
            heap.push(stone)
        while heap.size > 1:
            x, y = heap.pop(), heap.pop()
            if x != y:
                heap.push(x - y)
        if heap.size: return heap.heap[0]


    print(lastStoneWeight([2, 7, 4, 1, 8, 1]))
