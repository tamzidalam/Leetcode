class Solution:
    def reverseWords(self, s: str) -> str:
        
        l,r=0,0
        
        t=' '
        i=0
        hashmap={}
        temp=''
        for i in s:
            if i !=t:
                temp+=i
                hashmap[l]=temp
            else:
                temp=''
                l+=1
                
        temp=''
        for key, value in hashmap.items():
            if (key == len(hashmap) - 1):
                
                value = value [::-1]
                temp=temp+value
            else:
                
                value = value [::-1]
                temp=temp+value+t
            
        
        return temp  