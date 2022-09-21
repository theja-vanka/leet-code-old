class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low: int = 0
        high: int = len(nums) - 1
        
        while low <= high:
            middle: int = low + int((high - low)/2)
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle  + 1
            else:
                high = middle - 1
            
        return low