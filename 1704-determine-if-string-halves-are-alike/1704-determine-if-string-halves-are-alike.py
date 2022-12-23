class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        first=0
        second=0
        
        vowels={'a':'a', 'e':'e', 'i':'i', 'o':'o', 'u':'u', 'A':'A', 'E':'E', 'I':'I', 'O':'O', 'U':'U'}
        
        for i in range(0,len(s)//2):
            if s[i] in vowels:
                print(s[i])
                first+=1
        
        for i in range(len(s)//2,len(s)):
            if s[i] in vowels:
                second+=1
        
        
        if first == second:
            return True
        
        return False
        