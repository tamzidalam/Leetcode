class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        
        n=len(nums)
        
        for i in range(0,len(nums)):
            
            
            
            nums[i] = n* (nums[nums[i]]%n) +nums[i]
            
            
            
        
        

        for i in range(0,len(nums)):
            
            nums[i] = nums[i] // n
        
        
        return nums
        