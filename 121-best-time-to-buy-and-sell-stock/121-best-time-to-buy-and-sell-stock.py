class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum=999999
        maxP=0
        
        for i in prices:
            
            if i < minimum:
                minimum=i
                print(minimum)
            
            else:
                maxP=max(maxP,i-minimum)
                
        
        return maxP
        
        
        
        
        