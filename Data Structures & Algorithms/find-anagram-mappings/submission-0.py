class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        res = []


        for i, num in enumerate(nums2):
            seen[num] = i
        
        for num in nums1:
            res.append(seen[num])

        return res