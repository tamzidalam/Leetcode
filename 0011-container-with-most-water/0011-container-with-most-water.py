class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l=0
        r=len(height)-1
        maxx=0
        
        
        while l<r:
            
            if height[l] < height[r]:
                temp=(height[l] * (r-l))
                l+=1
            
            else:
                temp=(height[r] * (r-l))
                r-=1
            
            maxx=max(maxx,temp)

        print(maxx)
        return maxx
        