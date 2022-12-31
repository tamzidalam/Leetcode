class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output=[[1]]
        
        rowTrack=1
        
        
        for i in range(numRows-1):
            
            temp=[0] + output[-1] + [0]
            row=[]
            
            for j in range(rowTrack+1):
                           
                row.append(temp[j]+temp[j+1])
            
            output.append(row)
            rowTrack+=1
        
        
        return output
            