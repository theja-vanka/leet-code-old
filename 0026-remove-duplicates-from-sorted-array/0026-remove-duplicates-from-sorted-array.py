class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pointer: int = 1
        current_value = nums[0]

        for i in range(1,len(nums), 1):
            if current_value == nums[i]:
                continue
            else:
                nums[pointer], current_value = nums[i], nums[i]
                pointer += 1
        
        return pointer
        