class Solution(object):
    def matrixReshape(self, mat, r, c):
        
        if (len(mat) * len(mat[0])) != (r * c):
            return mat
        
        else:
            res = [[]]
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if len(res[-1]) < c:
                        res[-1].append(mat[i][j])
                    else:
                        res.append([mat[i][j]])
            return res           
        