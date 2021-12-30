class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r=0,0
        
        mapp={}
        
        maxL=0
        i=0
        while(i<len(s)):
            
            if s[i]  not in mapp:
                r+=1
            
            else:
                l = max(l,mapp[s[i]])
                r = i - l 
             
            mapp[s[i]] = i
            
            maxL= max(r,maxL)
            i+=1
            
         
                
        return maxL    
                