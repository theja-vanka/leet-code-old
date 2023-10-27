class Solution:
    def isPalindrome(self, s: str) -> bool:

        condensed_string: str = ""

        for char in s:
            if char.isalnum():
                condensed_string += char.lower()
            
        return condensed_string == condensed_string[::-1]

        