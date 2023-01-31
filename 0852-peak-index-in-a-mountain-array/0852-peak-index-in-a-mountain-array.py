class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        start,end=0,len(arr)-1
      
        
        while(start<end):
            
            
            middle= start + (end-start)//2
             
            if arr[middle]>arr[middle+1]:
                
                end=middle
             
            else:
                start=middle+1
        
        return end
                