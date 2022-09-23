class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        map<int,int> diffTarget;
        vector<int> returnValue = {-1, -1};
        
        for(int i=0; i<numbers.size(); i++){
            
            map<int,int>::iterator it = diffTarget.find(numbers[i]);
            if(it != diffTarget.end())
            {
                returnValue = {it->second+1, i+1};
                return returnValue;
            }
            
            diffTarget[target-numbers[i]] =  i;
        
        }
        return returnValue;
        
        
    }
};