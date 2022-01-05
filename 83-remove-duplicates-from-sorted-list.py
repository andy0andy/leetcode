"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head





    def lookListNode(self, head: ListNode):

        if not head:
            return

        print(head.val)
        self.lookListNode(head.next)


if __name__ == "__main__":

    h = ListNode(val=1)
    n2 = ListNode(val=1)
    n3 = ListNode(val=2)

    h.next = n2
    n2.next = n3

    # Solution().lookListNode(h)

    head = Solution().deleteDuplicates(h)

    Solution().lookListNode(head)