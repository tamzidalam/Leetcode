class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        output=""
        
        if len(words)==0:
            return output 
        
        
        
        for i in words:
            
            if i == i[::-1]:
                return i 
            
            
        
        return output