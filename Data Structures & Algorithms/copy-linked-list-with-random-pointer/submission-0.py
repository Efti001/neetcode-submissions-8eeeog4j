"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hMap = {}
        curr = head
        if not head:
            return None
        while curr:
            hMap[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                hMap[curr].next = hMap[curr.next]
            if curr.random:
                hMap[curr].random = hMap[curr.random]
            curr= curr.next
        return hMap[head]