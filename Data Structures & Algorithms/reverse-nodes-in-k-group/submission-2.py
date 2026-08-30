# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # groupPrev points to the node immediately preceding the current k-group
        groupPrev = dummy
        
        while True:
            # 1. Find the kth node
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            
            # 2. Reverse the group
            # Initializing prev to groupNext automatically connects the tail 
            # of this reversed group to the start of the next group.
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # 3. Connect the previous group to the new head of this reversed group
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
            
        return dummy.next
        
    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr