class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        result=[]
        

        for i in range(0,len(words)):
            
            temp=set(words[i])
            
            if x in temp:
                result.append(i)
        
        
        return result 
            
        