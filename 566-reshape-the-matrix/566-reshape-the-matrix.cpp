class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        
        int row = mat.size();
        int col = mat[0].size();
        
        vector<int> temp;
        vector<vector<int>> reshapedMatrix;
        
        int i = 0;
        int j = 0;
        
        
        if(row*col != r*c) 
            return mat;
        
        
        for(int irow=0; irow<row; irow++)
        {
            for(int icol=0; icol<col; icol++)
            {
                temp.push_back(mat[irow][icol]);
                j += 1;
                if(j == c)
                {
                    reshapedMatrix.push_back(temp);
                    temp.clear();
                    i += 1;
                    j = 0;
                }
            }
        }
        
        return reshapedMatrix;
    }
};