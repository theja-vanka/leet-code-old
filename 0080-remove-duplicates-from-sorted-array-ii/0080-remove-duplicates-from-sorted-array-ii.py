class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pointer: int = 1
        current_value: int = nums[0]
        counter: int = 1

        for i in range(1, len(nums)):
            if current_value == nums[i] and counter < 2:
                nums[pointer] = nums[i]
                counter += 1
                pointer += 1
            elif current_value != nums[i]:
                nums[pointer], current_value = nums[i], nums[i]
                counter = 1
                pointer += 1
            else:
                counter += 1

        return pointer
                 
        