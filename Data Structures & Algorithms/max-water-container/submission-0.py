class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        ans=0
        while l<r:
            base = r-l
            if heights[l]>heights[r]:
                h=heights[r]
                r-=1
            else:
                h=heights[l]
                l+=1
            ans=max(ans,base*h)
            
        return ans
        