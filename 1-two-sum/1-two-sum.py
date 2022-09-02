class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difftarget: Dict = {}
        
        for index, value in enumerate(nums):
            if value in difftarget.keys():
                return [index, difftarget[value]]
            difftarget[target-value] = index
        
            
            