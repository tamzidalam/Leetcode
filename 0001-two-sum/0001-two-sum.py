class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_table={}
        
        
        for i in range(0,len(nums)):
            
            number=target-nums[i] 
            
            if number in check_table:
                
                return [i,check_table[number]]
            
            check_table[nums[i]]=i
            # print(check_table)
        