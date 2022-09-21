class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count: int = 0
        candidate: int = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate