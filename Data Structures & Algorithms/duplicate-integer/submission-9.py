class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDuplicates = set()

        for num in nums:
            if num in noDuplicates:
                return True
            noDuplicates.add(num)
        return False
