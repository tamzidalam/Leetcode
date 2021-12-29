class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxP,minP=nums[0],nums[0]
        result=maxP
        
        
        for i in range(1,len(nums)):
            
            current = nums[i]
            
            tempMax= max(current,current * maxP,current * minP)
            
            minP= min(current,current * maxP,current * minP)
            
            maxP=tempMax
            
            result=max(result,maxP)
         
        
        return result
     
                
        
        
        