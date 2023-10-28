class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap: dict = {}
        for index, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target-num], index]
            else:
                hashmap[num] = index
        
        