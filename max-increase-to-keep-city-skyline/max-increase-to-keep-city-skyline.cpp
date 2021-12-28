#include <vector>

class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        return find_skyline(grid);
    }
    
    int find_skyline(const vector<vector<int>>& grid)
    {
        // vertical_skyline();
        vector<int> E_W_skyline = horizontal_skyline(grid);
        vector<int> N_S_skyline = vertical_skyline(grid);
        
        // Prints the correct skyline for each
        print_vector(E_W_skyline);
        print_vector(N_S_skyline);
        
        int accumulator = 0;
        for (int i = 0; i < grid.size(); ++i)
        {
            for (int j = 0; j < grid.at(i).size(); ++j)
            {
                int current_height = grid.at(i).at(j);
                
                // Find the min of the maxes of each skyline
                
                int max_horizontal_height = E_W_skyline.at(i);
                int max_vertical_height = N_S_skyline.at(j);
                
                (max_horizontal_height > max_vertical_height) ? accumulator += (max_vertical_height  - current_height):
                                                                accumulator += (max_horizontal_height - current_height);
            }
        }
        
        return accumulator;
        
    }
    
    void print_vector(const vector<int>& v)
    {
        for (int i = 0; i < v.size(); ++i)
        {
            cout << v.at(i) << "\t";
        }
        cout << endl;
    }
    
    vector<int> vertical_skyline(vector<vector<int>> grid)
    {
        vector<int> result;
        
        for (int j = 0; j < grid.at(0).size(); ++j)
        {
            int max = 0;
            for (int i = 0; i < grid.size(); ++i)
            {
                if (grid.at(i).at(j) > max)
                {
                    max = grid.at(i).at(j);
                }
            }
            result.push_back(max);
        }
        return result;
    }
    vector<int> horizontal_skyline(vector<vector<int>> grid)
    {
        vector<int> result;
        for (auto row: grid)
        {
            int max = 0;
            for (auto building: row)
            {
                if (building > max)
                {
                    max = building;
                }
            }
            result.push_back(max);
        }
        return result;
    }
    
    
};