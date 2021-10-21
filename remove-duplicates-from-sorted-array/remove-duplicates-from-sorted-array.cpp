class Solution {
public:

    void swap(int& num1, int& num2)
    {
        int temp = num1;
        num1 = num2;
        num2 = temp;
    }
    
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0)
        {
            return 0;
        }

        int current_index = 0;
        int next_diff_index = current_index + 1;
        while (next_diff_index <= nums.size() - 1)
        {
            while (nums.at(current_index) >= nums.at(next_diff_index))
            {
                next_diff_index++;
                if (next_diff_index == nums.size())
                {
                    return current_index + 1;
                }
            }
            swap(nums.at(current_index + 1), nums.at(next_diff_index));
            current_index++;
        }

        return current_index + 1;
    }
    

};