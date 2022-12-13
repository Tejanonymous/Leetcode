class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        l=len(matrix)
        if l==1:
            return min(matrix[0])
        elif l==2:
            return min(matrix[0])+min(matrix[1])
        else:
            row,col=l-2,0
            
            while row>=0:
                
                for col in range(l):
                    if col==0:
                        matrix[row][col]+=min(matrix[row+1][col],matrix[row+1][col+1])
                    elif col==l-1:
                        matrix[row][col]+=min(matrix[row+1][col-1],matrix[row+1][col])
                    else:
                        matrix[row][col]+=min(matrix[row+1][col],matrix[row+1][col+1],matrix[row+1][col-1])
                row-=1
                
            return min(matrix[0])
            
        