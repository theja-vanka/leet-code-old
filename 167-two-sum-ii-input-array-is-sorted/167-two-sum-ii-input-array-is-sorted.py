class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap: Dict = {}
        
        for index, value in enumerate(numbers):
            if target-value not in hashmap:
                hashmap[value] = index
            else:
                return [hashmap[target-value]+1, index+1]
                
        