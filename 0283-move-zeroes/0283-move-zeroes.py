class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        pointer=0
        fast=0
        
        while fast<len(nums):
            print(nums[fast])
            if nums[fast]!=0:
                nums[pointer],nums[fast]=nums[fast],nums[pointer]
                pointer+=1
            
            fast+=1
            
        
        return nums