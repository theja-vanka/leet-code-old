class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        output: List[str] = []

        if len(nums) == 0: return output

        start: str = str(nums[0])
        end: str = ""
        index: int = 0

        for index in range(1, len(nums), 1):
            if nums[index] - nums[index-1] != 1:
                end = str(nums[index-1])
                if start == end:
                    output.append(start)
                else:
                    output.append(start+"->"+end)
                start = str(nums[index])

        end = str(nums[index])
        if start == end:
            output.append(start)
        else:
            output.append(start+"->"+end)

        return output

