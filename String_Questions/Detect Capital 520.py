import re
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if re.fullmatch(r'[A-Z]{1}[a-z]*', word) or re.fullmatch(r'[A-Z]*', word) or re.fullmatch(r'[a-z]*', word):
            return True
        return False






word = "33"
print(Solution().detectCapitalUse(word))