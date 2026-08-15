# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        index = length-n
        current=head
        prev = None
        while index>0:
            index-=1
            prev = current
            current = current.next
        if prev==None:
            head=head.next
        else:
            prev.next=current.next
        return head