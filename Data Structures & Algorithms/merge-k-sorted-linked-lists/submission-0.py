# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for cur in lists:
            while cur:
                nodes.append(cur.val)
                cur = cur.next
        nodes.sort()

        dummy = ListNode(0)
        h = dummy
        for node in nodes:
            h.next = ListNode(node)
            h = h.next
        return dummy.next
