#include <algorithm>

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        return easy_solution(nums);
    }
    
    vector<int> easy_solution(vector<int>& nums)
    {
        for (auto& item : nums)
        {
            item = item * item;
        }
        sort(nums.begin(), nums.end());
        return nums;
    }
};