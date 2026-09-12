class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {}

        for i, num in enumerate(nums):
            requiredNum = target - num
            
            if requiredNum in seenMap:
                return [seenMap[requiredNum], i]
            seenMap[num] = i
