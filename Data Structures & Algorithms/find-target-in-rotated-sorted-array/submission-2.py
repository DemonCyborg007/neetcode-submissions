class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # CONDITION 1: The LEFT half is sorted
            if nums[l] <= nums[mid]:
                # Does the target fall strictly inside this sorted left half?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Target is here, go left
                else:
                    l = mid + 1  # Target is NOT here, go right
            
            # CONDITION 2: The RIGHT half is sorted
            else:
                # Does the target fall strictly inside this sorted right half?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Target is here, go right
                else:
                    r = mid - 1  # Target is NOT here, go left
                    
        return -1