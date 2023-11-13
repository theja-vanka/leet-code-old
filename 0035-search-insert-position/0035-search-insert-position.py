class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start: int = 0
        end: int = len(nums) - 1
        return self.binarySearch(nums, start, end, target)

    def binarySearch(self, nums, start, end, target):
        mid: int = (end + start)//2

        while start <= end:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binarySearch(nums, start, mid-1, target)
            else:
                return self.binarySearch(nums, mid+1, end, target)
        
        return start
        
            

        