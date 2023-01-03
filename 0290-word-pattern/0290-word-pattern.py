class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        strList= list(s.split(" "))
        
        if len(pattern) != len(strList):
            return False
        
        count=0
        hashMap={}
        for i in pattern:
            if i in hashMap:
                if strList[count] != hashMap[i]:
                    return False
                  
            
            else:
                if strList[count] in hashMap.values():
                    return False
                hashMap[i] = strList[count]
            
            count+=1
                
        
        # Key point: a , b means a and b will contain two different words.

        return True  