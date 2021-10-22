#include <algorithm>

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        return better_solution(nums);
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
    
    vector<int> better_solution(vector<int>& nums)
    {
        int begin = 0;
        int end = nums.size() - 1;
        vector<int> result;
        while (begin <= end)
        {
            if (abs(nums.at(begin)) < abs(nums.at(end)))
            {
                result.insert(result.begin(), nums.at(end) * nums.at(end));
                end--;
            }
            else
            {
                result.insert(result.begin(), nums.at(begin) * nums.at(begin));
                begin++;
            }
        }

        return result;
    }

};