
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
        bool carry_over = 0;
        int index = digits.size()-1;
        digits.at(index) += 1;
        recursive_solve(digits, index, carry_over);
        return digits;
    }
    
    void recursive_solve(vector<int>& digits, int index, bool carry_over)
    {
        if (index == -1)
        {
            if (carry_over == 1)
            {
                digits.insert(digits.begin(), 1);
            }
            return;
        }
        
        int digit = digits.at(index) + carry_over;
        int new_digit = (digit) % 10; // Digit if it carried over
        digits.at(index) = new_digit;
        carry_over = digit / 10;    // If there is a carry over 
        recursive_solve(digits, index - 1, carry_over);
    }
};