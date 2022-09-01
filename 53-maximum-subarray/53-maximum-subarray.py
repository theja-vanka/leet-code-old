class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_sum: int = -float('inf')
        _sum: int = -float('inf')
        
        for num in nums:
            if _sum < 0:
                _sum = 0
            _sum += num
            maximum_sum = max(_sum, maximum_sum)
        
        return maximum_sum
        
        