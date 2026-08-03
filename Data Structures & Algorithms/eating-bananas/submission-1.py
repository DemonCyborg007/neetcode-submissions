class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans = r
        def check(mink):
            val=0
            print(mink)
            for i in piles:
                val+=-(-i//mink)
            if val<=h:
                return True
            else:
                return False
        while l<=r:
            mid=(l+r)//2
            print("mid",mid,l,r)
            if check(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
        