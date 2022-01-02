class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        output=0
        
        mapp={}
        
        for i in jewels:
            
            if i not in mapp:
                
                mapp[i] = i
             
        
        for i in stones:
            if i in mapp:
                output+=1
        
        
        print(output)
        return output