class Solution:
    def isPalindrome(self, x: int) -> bool:
        num: int = x
        rev: int = 0
        while num > 0:
            remainder: int = num%10
            rev: int = rev * 10 + remainder
            num = num//10
        return rev == x
            
            
        