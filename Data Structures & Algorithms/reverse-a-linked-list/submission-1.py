# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        a=head
        b=head.next
        a.next=None
        while b.next!=None:
            c=b.next
            b.next=a
            a=b
            b=c
        b.next=a
        return b
            
        