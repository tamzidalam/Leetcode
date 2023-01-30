# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        
        start=0
        end=n
        
        while(start<=end):
            
            middle=start+(end-start)//2
            
            if (guess(middle)==-1):
                
                end=middle-1
                
            elif(guess(middle)==1):
                
                start=middle+1
            
            else:
                return middle
            
        
       