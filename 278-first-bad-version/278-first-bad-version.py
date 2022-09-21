# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low: int = 1
        high: int = n
        
        while(low <= high):
            middle: int = low + int((high - low)/2);
            if isBadVersion(middle):
                correct_version: int = middle
                high = middle - 1
            else:
                low = middle + 1
            
        return correct_version