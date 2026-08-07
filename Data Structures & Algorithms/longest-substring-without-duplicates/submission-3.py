class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check=set()
        ans=0
        start=0
        for i in range(len(s)):
            # print(ans)
            if s[i] in check:
                for j in range(start,i):
                    if s[j]==s[i]:
                        start=j+1
                        break
                    else:
                        check.remove(s[j])
            else:
                check.add(s[i])
                ans=max(ans,i-start+1)
        return ans
        