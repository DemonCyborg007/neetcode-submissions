class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()  # Store indices, not values

        for i, num in enumerate(nums):
            # 1. Remove indices that are out of the current window's left boundary
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # 2. Remove indices of smaller elements from the back of the deque
            # because they are useless now that we found a larger element
            while q and nums[q[-1]] <= num:
                q.pop()
                
            # 3. Add the current element's index to the deque
            q.append(i)
            
            # 4. Once we have processed at least 'k' elements, start adding to the answer
            if i >= k - 1:
                ans.append(nums[q[0]])
                
        return ans
        