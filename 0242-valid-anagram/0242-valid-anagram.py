class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_hash: dict = {}
        t_hash: dict = {}

        for char in s:
            if char in s_hash:
                s_hash[char] += 1
            else:
                s_hash[char] = 1
        

        for char in t:
            if char in t_hash:
                t_hash[char] += 1
            else:
                t_hash[char] = 1

        return s_hash == t_hash
        