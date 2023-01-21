class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l=0
        r=len(height)-1
        maxx=0
        
        
        while l<r:
            temp=min(height[l],height[r]) * (r-l)
            maxx=max(maxx,temp)
            if height[l] < height[r]:
                
                l+=1
            
            else:
                r-=1
            
            

        print(maxx)
        return maxx
        