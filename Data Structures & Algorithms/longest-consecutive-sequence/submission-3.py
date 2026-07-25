class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bag = set()
        if len(nums)==1:
            return 1
        for i in nums:
            bag.add(i)
        max_l = 0
        curr_l = 0
        for i in nums:
            if i-1 not in bag:
                curr_l+=1
                for j in range(len(nums)):
                    if i+j+1 in bag:
                        curr_l+=1
                    else:
                        break
            max_l=max(max_l,curr_l)
            curr_l=0      
        return max_l
        