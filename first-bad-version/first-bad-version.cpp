// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    unsigned int find_first_bad_version(unsigned int low, unsigned int high)
    {
        unsigned int index = (low + high) / 2;
        if (low  <= high)
        {
            if (isBadVersion(index) == true)
            {
                // Search the partition from [0, index - 1]
                return find_first_bad_version(low, index - 1);
            }
            else
            {
                // Search the rest of the partition [index + 1, size() - 1]
                return find_first_bad_version(index + 1, high);
            }
        }
        return index;
    }
                     
    int firstBadVersion(int n) {
        // Same thing, if I'm given a list, I should really just use binary search as well
        return find_first_bad_version(0, n) + 1;
    }
    

};