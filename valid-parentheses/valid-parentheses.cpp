#include <stack>

class Solution {
public:
    bool isValid(string s) {

        stack<char> brace_stack;
        for (auto& c : s)
        {
            if (c == '(' || c == '{' || c == '[')
            {
                brace_stack.push(c);
            }
            else if (c == ')')
            {
                if (brace_stack.size() > 0 && brace_stack.top() == '(' )
                {
                    brace_stack.pop();	
                }
                else
                {
                    return false;
                }
            }
            else if (c == ']')
            {
                if (brace_stack.size() > 0 && brace_stack.top() == '[')
                {
                    brace_stack.pop();
                }
                else
                {
                    return false;
                }
            }
            else if (c == '}')
            {
                if (brace_stack.size() > 0 && brace_stack.top() == '{'  )
                {
                    brace_stack.pop();
                }
                else
                {
                    return false;
                }
            }
            else
            {
                cout << "This should not happen" << endl;
            }
        }
        if (brace_stack.size() == 0)
        {
            return true;
        }
        return false;
    }
};