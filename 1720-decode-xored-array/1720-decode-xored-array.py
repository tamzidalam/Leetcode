class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
       
        result=[first]
        
        for i in encoded:
            
            temp=abs(i^result[-1])
            result.append(temp)
        
        
        return(result)