class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c=[-1]*len(cost)

        def dfs(i):
            if i>=len(cost):
                return 0
            if c[i]!=-1:
                return c[i]
            c[i]=cost[i]+min(dfs(i+1),dfs(i+2))
            return c[i]
        return min(dfs(0),dfs(1))

        