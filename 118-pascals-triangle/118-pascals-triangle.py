class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ret_matrix: List[int] = []
        _temp: List[int] = []
        
        for row in range(1, numRows+1):
            for col in range(row):
                if col == 0 or col == row - 1:
                    _temp.append(1)
                else:
                    _temp.append(ret_matrix[-1][col-1] + ret_matrix[-1][col])
            ret_matrix.append(_temp)
            _temp = []
        return ret_matrix
                
                