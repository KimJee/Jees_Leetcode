class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # First sort all of the words (with original index)
        # THen collect the words into a hashmap
            # if a match is found, append the word to the group 
            # otherwise if not match is found don't append 
        
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
            
        
        
        
            
        