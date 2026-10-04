class Solution:
    def isHappy(self, n: int) -> bool:
        bag = set()
        strn=str(n)
        flag = True
        while flag:
            ans=0
            for i in range(len(strn)):
                ans+=int(strn[i])*int(strn[i])
            if ans==1:
                return True
            if ans in bag:
                return False
            bag.add(ans)
            strn=str(ans)
        