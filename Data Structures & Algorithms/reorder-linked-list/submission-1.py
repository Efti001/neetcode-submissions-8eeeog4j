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
        #find second half of LL
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next #second half of LL starts here
        slow.next = None #cut the list
        second = reverse(second)

        first = head
        while second:
            #need temp nodes to hold pointers
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
