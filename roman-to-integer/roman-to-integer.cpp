class Solution {
public:
    int romanToInt(string s)
    {
        int total = 0;
        int letter_index = 0;
        while (letter_index < s.size())
        {
            total += prefix(s[letter_index], s, letter_index);
            letter_index++;
        }
        return total;
    }
    
    /*
        So there's a couple structures
         I,  II,  III,  IV,  V,  VI,  VII,  VIII,  IX,  X
        XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX
        
        (1) If I see an I, it could be the (1), or beginning a prefix for V, X, 
        (2) If I see a X, it could be the (10) or beginning prefix of L, C 
        (3) If I see a C, it could be (100), or beginning prefix D, M
    */
    
    int convert_roman_to_int(char c)
    {
        if (c == 'I')
        {
            return 1;
        }
        else if (c == 'V')
        {
            return 5;
        }
        else if (c == 'X')
        {
            return 10;
        }
        else if (c == 'L')
        {
            return 50;
        }
        else if (c == 'C')
        {
            return 100;
        }
        else if (c == 'D')
        {
            return 500;
        }
        else if (c == 'M')
        {
            return 1000;
        }
        else
        {
            return -1;    
        }
    }

    int examine_further(const char &c, const string &input_string, int & char_index)
    {
        if (c == 'I')
        {
            // Check if the next character is either (null, V, or X) and follow rules accordingly.
            // Otherwise just increment the counter by I

            // As long as this next place we're seeking is within limits of the string
            if (0 <= char_index + 1 <= input_string.size() - 1)
            {
                // This is the next character
                const char next_char = input_string[char_index + 1];
                if (next_char == 'V')
                {
                    char_index++;
                    return convert_roman_to_int('V') - convert_roman_to_int('I');
                }
                if (next_char == 'X')
                {
                    char_index++;
                    return convert_roman_to_int('X') - convert_roman_to_int('I');
                }
            }
            return convert_roman_to_int(c);
        }
        else if (c == 'X')
        {
            // Check if the next character is either (null, V, or X) and follow rules accordingly.
            // Otherwise just increment the counter by I

            // As long as this next place we're seeking is within limits of the string
            if (0 <= char_index + 1 <= input_string.size() - 1)
            {
                // This is the next character
                const char next_char = input_string[char_index + 1];
                if (next_char == 'L')
                {
                    char_index++;
                    return convert_roman_to_int('L') - convert_roman_to_int('X');
                }
                if (next_char == 'C')
                {
                    char_index++;
                    return convert_roman_to_int('C') - convert_roman_to_int('X');
                }
            }
            return convert_roman_to_int(c);
        }
        else if (c == 'C')
        {
            // Check if the next character is either (null, V, or X) and follow rules accordingly.
            // Otherwise just increment the counter by I

            // As long as this next place we're seeking is within limits of the string
            if (0 <= char_index + 1 <= input_string.size() - 1)
            {
                // This is the next character
                const char next_char = input_string[char_index + 1];
                if (next_char == 'D')
                {
                    char_index++;
                    return convert_roman_to_int('D') - convert_roman_to_int('C');
                }
                if (next_char == 'M')
                {
                    char_index++;
                    return convert_roman_to_int('M') - convert_roman_to_int('C');
                }
            }
            return convert_roman_to_int(c);
        }
        else
        {
            return -1;    
        }
    }

    int prefix(const char &c, const string &input_string, int& char_index)
    {
        if (c == 'I' || c == 'X' || c == 'C')
        {
            return examine_further(c, input_string, char_index);
        }
        else
        {
            return convert_roman_to_int(c);
        }
    }



};