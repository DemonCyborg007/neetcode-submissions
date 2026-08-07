class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        ans = 0
        start = 0
        
        for i in range(len(s)):
            # If we've seen the character AND it's inside our current window
            if s[i] in char_index_map and char_index_map[s[i]] >= start:
                # Instantly jump the start pointer to avoid an inner loop
                start = char_index_map[s[i]] + 1
            
            # Update the latest index of the character
            char_index_map[s[i]] = i
            ans = max(ans, i - start + 1)
            
        return ans
        