class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        length: int = len(s) - 1
        word_length:int = 0
        while s[length] == " ":
            length -= 1
        
        while s[length] != " " and length >= 0:
            word_length += 1
            length -= 1
        
        return word_length