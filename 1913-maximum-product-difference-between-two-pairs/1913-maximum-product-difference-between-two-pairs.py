class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        
        maxx1=-inf
        maxx2=-inf

        minn1=inf 
        minn2=inf 
        
        for i in nums:
            
            if i>maxx1:
                temp=maxx1
                maxx1,maxx2=i,temp
             
            elif i>maxx2:
                maxx2=i
                
        
        for i in nums:
            
            if i<minn1:
                temp=minn1
                minn1,minn2=i,temp
             
            elif i<minn2:
                minn2=i
                
        
        return (maxx1*maxx2)-(minn1*minn2)
        