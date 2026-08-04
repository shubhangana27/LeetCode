from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_counts=Counter(ransomNote)
        char_magcounts=Counter(magazine)
        for i in ransomNote:
            if char_counts[i]>char_magcounts[i] :
                return False
        return True