# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergetwoll(n1, n2):
            dummy = ListNode()
            tail = dummy
            while n1 and n2:
                if n1.val < n2.val:
                    tail.next = n1
                    n1 = n1.next
                else:
                    tail.next = n2
                    n2 = n2.next
                tail = tail.next
                
            if n1:
                tail.next = n1
            if n2:
                tail.next = n2
                
            # FIX 1: Return the head of the newly merged list
            return dummy.next

        if not lists:
            return None
            
        # FIX 2: Divide and Conquer merging instead of sequential
        while len(lists) > 1:
            merged_lists = []
            
            # Jump by 2 to merge pairs (l0+l1, l2+l3...)
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                merged_lists.append(mergetwoll(l1, l2))
                
            # Replace the old list array with our newly merged half-array
            lists = merged_lists
            
        return lists[0]