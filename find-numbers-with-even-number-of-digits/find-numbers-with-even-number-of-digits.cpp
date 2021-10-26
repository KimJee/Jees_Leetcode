class Solution {
public:

    void swap(char a, char b)
    {
        char temp = a;
        a = b;
        b = temp;
    }

    int abs(int input)
    {
        if (input < 0)
        {
            return -1 * input;
        }
        return input;
    }


    string reverse(string& input)
    {
        for (int i = 0, j = input.size() - 1; i < j; ++i, --j)
        {
            swap(input[i], input[j]);
        }
        return input;
    }

    string int_to_string(int input)
    {
        string result = "";
        do
        {
            result += (input % 10) + '0';
            input /= 10;
        } while (input != 0);

        input < 0 ? result += "-" : result += "";
        return reverse(result);
    }

    int findNumbers(vector<int>& nums) {

        int counter = 0;
        for (auto& num : nums)
        {
            // cout << "i:" << int_to_string(num).size() << endl;
            if (int_to_string(num).size() % 2 == 0)
            {
                counter++;
            }
        }
        return counter;
    }
    

};