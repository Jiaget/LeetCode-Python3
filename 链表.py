class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    # 分割链表
    def partition(head: ListNode, x: int) -> ListNode:
        # 记录< x的链表和 >=x 的链表
        # 注意：链表头部均为0，链表从next开始
        largerHead = larger = ListNode(0)
        smallerHead = smaller = ListNode(0)
        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                larger.next = head
                larger = larger.next
            head = head.next
        # head链表分给larger,smaller两个链表。进行链表拼接
        # smaller 为首， larger 为尾
        larger.next = None
        smallerHead.next = largerHead.next
        return smallerHead.next


