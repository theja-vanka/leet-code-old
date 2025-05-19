class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap: dict = {
        }
        
        for index, value in enumerate(nums):
            if value not in hashmap:
                hashmap[target-value] = index
            else:
                return [hashmap[value], index]
