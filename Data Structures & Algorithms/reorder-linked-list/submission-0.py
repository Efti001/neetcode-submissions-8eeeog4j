# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head):
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev 
                prev = curr
                curr = temp
            return prev
        #find middle of LL
        #right half will start from the end and swap
        slow, fast = head, head
        while fast and fast.next:
            #find the middle
            slow = slow.next
            fast = fast.next.next
        #found the middle, cut it, make it into another list    
        second = slow.next
        slow.next = None #new list
        #reverse the second half
        second = reverse(second)

        #now swap the nodes accordingly
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2

        