class Solution:
    def carFleet(self, target: int, p: List[int], s: List[int]) -> int:
        car = sorted(zip(p,s),reverse=True)
        # print(car)
        t = []
        for i in car:
            t.append((target-i[0])/i[1])
        # print(t)
        first=t[0]
        ans=1
        for j in range(1,len(t)):
            if t[j]<=first:
                continue
            else:
                ans+=1
                first=t[j]
        return ans

