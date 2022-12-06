class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        flag=0
        if nums[0] == nums[len(nums)-1]:
            flag=0
         
        if nums[0] < nums[len(nums)-1]:
            
            flag=1

        else:
            flag=2
         
        for i in range(0,len(nums)-1):
            
            if flag == 0:
                if nums[i] != nums[i+1]:
                    return False
            
            elif flag == 1 :
                if nums[i] > nums[i+1]:
                    return False
            
            else:
                if nums[i] <nums[i+1]:
                    return False
         
        return True 
                    
                