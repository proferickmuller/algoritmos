# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return str(self.val) + " (" + str(self.next) + ")"
        return str(self.val)


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        soma = 0
        if l1:
            soma = l1.val
            pos = 1
            while l1.next:
                l1 = l1.next
                soma = soma + (l1.val * 10**pos)
                pos = pos + 1
        if l2:
            pos = 1
            soma = soma + l2.val
            while l2.next:
                l2 = l2.next
                soma = soma + (l2.val * 10**pos)
                pos = pos + 1

        if soma < 1:
            return ListNode(0)

        a = str(soma)
        r = None
        for c in a:
            r = ListNode(int(c), r)
        print(r)
        return r


s = Solution()

a = ListNode(2, ListNode(4, ListNode(3)))
b = ListNode(5, ListNode(6, ListNode(4)))

assert s.addTwoNumbers(a, b) == ListNode(7, ListNode(0, ListNode(8)))

# a = ListNode(0)
# b = ListNode(0)

# print(s.addTwoNumbers(a, b))

# a = ListNode(
#     9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
# )
# b = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

# print(s.addTwoNumbers(a, b))
