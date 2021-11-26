from typing import Optional

"""
https://leetcode-cn.com/problems/merge-two-sorted-lists/
递归
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


def printNode(node: Optional[ListNode]):

    while node:
        print(node.val)
        node = node.next


if __name__ == "__main__":
    n3 = ListNode(val=4)
    n2 = ListNode(val=2, next=n3)
    n1 = ListNode(val=1, next=n2)

    n6 = ListNode(val=4)
    n5 = ListNode(val=3, next=n6)
    n4 = ListNode(val=1, next=n5)

    res = Solution().mergeTwoLists(n1, n4)

    printNode(res)
