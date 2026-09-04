class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            new_subsets = [] 
            # Go through every subset we already have
            for subset in res:
                # Add the current number to it and save it to our temporary list
                new_subsets.append(subset + [num])
            # Add all the newly created combinations into our main results list
            res.extend(new_subsets)
        return res
        