class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows: int = len(mat)
        cols: int = len(mat[0])
        
        if rows*cols != r*c:
            return mat
        
        ret_list: List[int] = []
        _: List[int] = []
        i = 0
        for lst in mat:
            for num in lst:
                _.append(num)
                i += 1
                if i == c:
                    i = 0
                    ret_list.append(_)
                    _ = []
        return ret_list
                
                    
        
        
            