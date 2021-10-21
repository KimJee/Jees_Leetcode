class Solution {
public:

    int recursive_helper(vector<int>& nums, int target, int low, int high)
    {

        int index = (high + low) / 2; // Should take the lower half

        if (high >= low)
        {
            if (nums[index] == target)
            {
                return index;
            }
            else if (target > nums[index])
            {
                return recursive_helper(nums, target, index+1, high);
            }
            else if (target < nums[index])
            {
                return recursive_helper(nums, target, 0, index-1);
            }
        }
        return -1;
    }

    int search(vector<int>& nums, int target) {

        return recursive_helper(nums, target, 0, nums.size() - 1);
    }
};