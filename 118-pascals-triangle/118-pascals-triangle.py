class Solution(object):
    def generate(self, numRows):
        ans = [[1]]
        if numRows == 1:
            return ans
        
        for i in range(1, numRows):
            row = [1]
            #start row with 1
            for j in range(1, i):
                row.append(ans[i-1][j-1] + ans[i-1][j])
                #add the 2 elements from previous row, above current element
            
            row.append(1)
            #end row with 1
            ans.append(row)
            #append row to triangle
        
        return ans
        