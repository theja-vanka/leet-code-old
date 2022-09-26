class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i: int = 0
        j: int = len(s) - 1
        
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        