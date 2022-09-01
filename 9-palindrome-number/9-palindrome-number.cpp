class Solution {
public:
    bool isPalindrome(int x) {
        
        long reverse = 0;
        int temp = x;
        int reminder;
        
        while(temp > 0){
            reminder = temp%10;
            reverse = reverse*10 + reminder;
            temp = temp/10;
        }
        if(reverse == x){
            return true;
        }
        return false;
        
    }
};