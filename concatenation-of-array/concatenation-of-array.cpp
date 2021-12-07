class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> result;
        for (int i = 0; i < 2; ++i)
        {
            for (int j = 0; j < nums.size(); ++j)
            {
                result.push_back(nums.at(j));
            }
        }
        return result;
    }
};