class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        val = {}
        for i in range(len(numbers)):
            if target-numbers[i] in val:
                return [val[target-numbers[i]],i+1]
            # print(val)
            val[numbers[i]]=i+1
        