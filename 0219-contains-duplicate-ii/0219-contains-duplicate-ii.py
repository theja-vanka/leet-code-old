class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        memory: dict = {}

        for index, value in enumerate(nums):
            if value in memory:
                memory[value].append(index)
                if abs(memory[value][-2]- memory[value][-1]) <= k:
                    return True
            else:
                memory[value] = [index]
        
        return False