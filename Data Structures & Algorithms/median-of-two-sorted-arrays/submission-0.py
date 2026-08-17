class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
            
        total = len(A) + len(B)
        # Step 2: Target Left Bucket size (Left gets the extra element if odd)
        half = (total + 1) // 2
        
        # Binary search for the number of elements to take from A (0 to len(A))
        l, r = 0, len(A)
        
        while l <= r:
            # Step 3: Make the cuts
            cutA = (l + r) // 2
            cutB = half - cutA
            
            # The 4 values around the cut lines
            L1 = A[cutA - 1] if cutA > 0 else float('-infinity')
            R1 = A[cutA] if cutA < len(A) else float('infinity')
            
            L2 = B[cutB - 1] if cutB > 0 else float('-infinity')
            R2 = B[cutB] if cutB < len(B) else float('infinity')
            
            # Step 4: The "X" Check
            if L1 <= R2 and L2 <= R1:
                # Perfect Cut found!
                
                # Odd total length? Left side has the extra element.
                if total % 2 != 0:
                    return max(L1, L2)
                
                # Even total length? Average of max lefts and min rights.
                return (max(L1, L2) + min(R1, R2)) / 2.0
                
            # Cut in A is too far right, move left
            elif L1 > R2:
                r = cutA - 1
                
            # Cut in A is too far left, move right
            else:
                l = cutA + 1
        