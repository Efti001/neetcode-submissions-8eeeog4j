# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for i in (lists):
            cur = i
            while cur:
                nodes.append(cur.val)
                cur = cur.next
        nodes.sort()
        
        dummy = ListNode(0)
        node = dummy

        for i in nodes:
            node.next = ListNode(i)
            node = node.next
        return dummy.next