# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        anshead=list1
        if list1==None:return list2
        if list2==None:return list1
        if list1.val>list2.val:
            anshead=list2
            list2=list2.next
        else:
            list1=list1.next
        current = anshead
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  # Link to the smaller node
                list1 = list1.next    # Move list1 forward
            else:
                current.next = list2  # Link to the smaller node
                list2 = list2.next    # Move list2 forward
            
            # Move the tail pointer forward
            current = current.next
            
        # Once one list is exhausted, attach the remainder of the other list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return anshead
            
        