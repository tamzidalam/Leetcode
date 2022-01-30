class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
     
        l=0
        r=len(nums)-1
        
        while(l<r):
            
            mid=l+(r-l)//2
            if nums[l] == nums[r]:
                l+=1
            elif nums[mid]<=nums[r]:
                
                r=mid
             
            else:
                l=mid+1
       
        
        print("INdex",l)
        
        start=l
        end=len(nums)-1
        
        while(start<=end):
            
            mid=start+(end-start)//2
            
            if nums[mid] == target:
                return True
            
            elif nums[mid]<target:
                
                start=mid+1
             
            else:
                end=mid-1
      
        print("2ndd blocck")
        start=0
        end=l-1
        
        while(start<=end):
            
            mid=start+(end-start)//2
            
            if nums[mid] == target:
                return True
            
            elif nums[mid]<target:
                
                start=mid+1
             
            else:
                end=mid-1
        return False