class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        
        s=0
        e=len(nums)-1
        result=[0]*len(nums)
        counter=e

        for i in range(0,e+1):
    
            nums[i]=nums[i]*nums[i]
        
        
        
        
        while(s<=e):
            
            if nums[s]<nums[e]:
                result[counter]=nums[e]
                e=e-1
                
            else:
                result[counter]=nums[s]
                
                s=s+1
          
            counter=counter-1
        
        return result