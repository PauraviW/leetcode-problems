class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = {}
        for idx, num in enumerate(nums):

            if num in positions and (idx - positions[num] <= k):
                return True
            positions[num] = idx
        return False

