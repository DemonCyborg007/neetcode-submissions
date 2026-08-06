class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        # We use l < r instead of l <= r because we know the minimum 
        # is always inside the array. When l == r, we've found it.
        while l < r:
            mid = (l + r) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum MUST be in the right half (excluding mid).
            if nums[mid] > nums[r]:
                l = mid + 1
            
            # Otherwise, the right half is sorted, so the minimum is 
            # in the left half (INCLUDING mid, because mid could be the min).
            else:
                r = mid
                
        # When l and r converge, they point to the minimum element.
        return nums[l]
        