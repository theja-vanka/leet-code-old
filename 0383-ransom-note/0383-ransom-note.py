class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine_hashmap: dict = {}

        for char in magazine:
            if char not in magazine_hashmap:
                magazine_hashmap[char] = 1
            else:
                magazine_hashmap[char] += 1
        
        for char in ransomNote:
            if char in magazine_hashmap and magazine_hashmap[char] > 0:
                magazine_hashmap[char] -= 1
            else:
                return False
        
        return True
        