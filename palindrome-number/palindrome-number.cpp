class Solution {
public:

    template<typename T>
    void my_swap(T& a, T& b)
    {
        T temp = a;
        a = b;
        b = temp;
    }

    string reverse_string(string & input)
    {

        for (int i = 0, j = input.size() - 1; i < j; ++i, --j)
        {
            my_swap(input[i], input[j]);
        }
        return input;
    }

    string int_to_string(int input)
    {
        string result = "";
        int copy = input;
        do
        {
            result += abs(copy % 10) + '0';
            copy /= 10;
        } while (copy != 0);

        if (input < 0)
        {
            result += "-";
        }
        // cout << "String_to_reverse: " << result << endl;
        return reverse_string(result);
    }

    bool is_palindrome(string input)
    {
        for (int i = 0, j = input.size() - 1; i < j; ++i, --j)
        {
            if (input[i] != input[j])
            {
                return false;
            }
        }
        return true;
    }

    bool isPalindrome(int input)
    {
        string output = int_to_string(input);
        cout << "Output is: " << output << endl;
        return is_palindrome(output);
    }
    

};