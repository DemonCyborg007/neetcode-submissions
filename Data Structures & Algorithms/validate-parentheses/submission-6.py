class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Dictionary mapping closing brackets to opening brackets
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # If stack is empty or top of stack doesn't match, it's invalid
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # It's an opening bracket
                stack.append(char)
                
        # Valid if the stack is completely empty at the end
        return not stack