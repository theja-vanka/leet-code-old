class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        votes = 0
        candidate = -1

        for num in nums:
            if votes == 0:
                votes = 1
                candidate = num
            else:
                if candidate == num:
                    votes += 1
                else:
                    votes -= 1
        
        return candidate
        