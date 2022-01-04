class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        if len(sentence) == 0:
            
            return False
        
        
        
        mapp={}
        
        for i in sentence:
            
            if i not in mapp:
                
                mapp[i] = i
                
        print(len(mapp))
        if len(mapp) == 26:
            return True
        
        return False
        
        