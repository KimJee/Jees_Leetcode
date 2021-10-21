class Solution {
public:
    int binary_search(vector<int>& nums, int target, int low, int high)
    {
        int index = (low + high) / 2;
        if (low <= high)
        {
            if (nums.at(index) == target)
            {
                return index;
            }
            else if (nums.at(index) < target)
            {
                return binary_search(nums, target, index + 1, high);
            }
            else // (nums.at(index) > target)
            {
                return binary_search(nums, target, low, index - 1);
            }
        }
        return index;
    }

    int searchInsert(vector<int>& nums, int target) {
       	int result = 0;
		int index = binary_search(nums, target, 0, nums.size() - 1);
		target > nums.at(index) ? index = index + 1 : index;
        return index;
    }
};