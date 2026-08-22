class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, it can't be a substring
        if len(s1) > len(s2):
            return False
            
        # Create frequency maps (arrays of size 26 for 'a' to 'z')
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # 1. Initialize the first window
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
            
        # 2. Slide the window across s2
        for i in range(len(s2) - len(s1)):
            # If the frequency maps match, we found a permutation
            if s1_count == window_count:
                return True
                
            # Slide window right: remove the character left behind
            left_char_index = ord(s2[i]) - ord('a')
            window_count[left_char_index] -= 1
            
            # Slide window right: add the new character entering the window
            right_char_index = ord(s2[i + len(s1)]) - ord('a')
            window_count[right_char_index] += 1
            
        # 3. Check the very last window after the loop finishes
        return s1_count == window_count
        
        