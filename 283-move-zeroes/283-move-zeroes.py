class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        list_pointer: int = 0;
        zero_counter: int = 0;
        
        for index, value in enumerate(nums):
            if value == 0:
                zero_counter += 1
            else:
                nums[list_pointer] = nums[index]
                list_pointer += 1
        for zero in range(zero_counter):
            nums[list_pointer] = 0
            list_pointer += 1
            