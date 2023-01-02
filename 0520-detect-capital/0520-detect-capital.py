class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        allCap= word.upper()
        allLow=word.lower()
        first=word.capitalize()
        
        
        if word == allCap or word == allLow or word == first:
            return True
        
        return False