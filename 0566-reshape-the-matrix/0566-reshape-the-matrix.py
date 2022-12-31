class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        row=len(mat)
        column=len(mat[0])
        
        if row*column != r*c:
            return mat
        
        #outputMatrix=[[0]*c]*r
        outputMatrix=[]

        col=0
        row=0
        temp=[]
        print("C",c)
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                
                temp.append(mat[i][j])
                
                col+=1
                print(temp)
                if col == c:
                    print(col,c)
                    outputMatrix.insert(row,temp)
                    col=0
                    row+=1
                    temp=[]
                
           
        
        return outputMatrix