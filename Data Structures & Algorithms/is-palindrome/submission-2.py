class Solution:
    def isPalindrome(self, s: str) -> bool:
        f=0
        l=len(s)-1
        while f<l:
            sf=s[f]
            sl=s[l]
            while sf.isalnum() == False:
                f+=1
                if f==len(s):
                    return True
                sf=s[f]
            while sl.isalnum() == False:
                l-=1
                sl=s[l]
            
            if sf.lower()!=sl.lower():
                print(sf,sl)
                return False
            f+=1
            l-=1
        return True
        