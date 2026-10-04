class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If every digit was 9 (e.g., [9, 9] -> [0, 0]), prepend 1
        return [1] + digits