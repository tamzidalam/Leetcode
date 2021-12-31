class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output=[]
        mapp={}
        
        
        for i in strs:
            res = ''.join(sorted(i))
            
            if res not in mapp:
                mapp[res] = [i]
            
            else:
                mapp[res].append(i)
            
        
        
        for i in mapp.values():
            output.append(i)
        
        return output