# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to hold the start of our new list
        curr = dummy         # Pointer to build the new list
        carry = 0
        
        # Loop continues as long as there is a node in l1, l2, or a leftover carry
        while l1 or l2 or carry:
            # Get the values (use 0 if the list has already ended)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum for this column
            total = val1 + val2 + carry
            
            # Update the carry for the next calculation
            carry = total // 10
            
            # Create a new node with the single digit and attach it
            curr.next = ListNode(total % 10)
            
            # Move all pointers forward
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next
         
            
        