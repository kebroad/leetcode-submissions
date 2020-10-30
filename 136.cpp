
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int i = nums.size()-1;
        while(i > 0){
            if(nums[i] == nums[i-1]){
                i -= 2;
            }
            else{
                return nums[i];
            }
        }
        return nums[0];

    }
};