class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int accumulator = 0;
        vector<int> result;
        for (int i = 0; i < nums.size(); ++i)
        {
            accumulator += nums[i];
            result.push_back(accumulator);
        }
        return result;
    }
};