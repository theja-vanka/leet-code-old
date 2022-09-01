class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueimg = set(nums)
        if len(nums) > len(uniqueimg):
            return True
        else:
            return False