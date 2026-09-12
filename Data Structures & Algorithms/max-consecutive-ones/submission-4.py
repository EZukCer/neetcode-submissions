class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxRes, tempRes = 0, 0

        for num in nums:
            tempRes = tempRes + 1 if num else 0
            maxRes = max(maxRes, tempRes)
        return maxRes

        