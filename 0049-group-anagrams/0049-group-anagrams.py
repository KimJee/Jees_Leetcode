class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a bitstring representation of the words
        # One for each letter in the alphabet
        
        mapping = {}
        for word in strs:
            encoding = [0] * 26    
            for char in word:
                index = ord(char) - ord('a')
                encoding[index] += 1
            key = tuple(encoding)
            if (mapping.get(key) is None):
                mapping[key] = list() 
                mapping[key].append(word)
            else:
                mapping[key].append(word)
        return mapping.values()
                
        
        
    def approach_1(self, strs):
        # First sort all of the words (with original index)
        # THen collect the words into a hashmap
            # if a match is found, append the word to the group 
            # otherwise if not match is found don't append 
        
        
        
        ''' 
            Time Complexity
            
            word-length = k
            number of words = n
            sorting algo = klog(k)
            
            O(n * klog(k))
            
            Creating Groupings in the dictionary
                Iterating through all of the number of words
                    Theta(n)
            
            Outputting the Result
                Iterating through all the numbers of groups
                Worst-Case O(n)
                    Because in the worst case, we don't have any matching groups
                    
            Time complexity is O(n*klog(k))
                        
            Memory Usage
            
                Sorting each individual word (in-place sort with nlogn exists)
                Dictionary + List
                Let j = the number of groupings
                But we know that j <= N therefore
                    Amortized total would be O(N + j)
                    O(N + N) => O(2N) => O(N)
                O(N) for the result list
                    
                Memory Usage = O(N)
                    
        '''
        sorted_list = []
        for words in strs:
            sorted_list.append(''.join(sorted(words)))
        
        print(sorted_list)
        
        grouping = {}
        for index, values in enumerate(sorted_list):
            if grouping.get(values) is None:
                grouping[values] = list()
                grouping[values].append(strs[index])
            else:
                grouping[values].append(strs[index])
        
        result_list = []
        for values in grouping.values():
            result_list.append(values)
        return result_list
            
        
        
        
            
        