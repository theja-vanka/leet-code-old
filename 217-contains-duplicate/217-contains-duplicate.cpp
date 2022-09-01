class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::map<int, int> hash_nums;
        int key = 0;
        int value = 0;
 
        for (auto &num: nums)
        {
            // check if key `num` exists in the map or not
            std::map<int, int>::iterator it = hash_nums.find(num);
 
            // key already present on the map
            if (it != hash_nums.end()) {
                return true;
            }
            // key not found
            else {
                hash_nums.insert(std::make_pair(num, 1));
            }
        }
 
    return false;
        
    }
};