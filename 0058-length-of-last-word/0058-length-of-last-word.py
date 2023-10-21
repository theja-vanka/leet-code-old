class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = (" ".join(s.split())).split(" ")

        return len(s[-1])