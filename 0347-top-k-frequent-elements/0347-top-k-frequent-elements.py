class Solution:
    def first_solution(self, nums:List[int], k: int):
        freq_counter = {}
        for num in nums:
            freq_counter[num] = freq_counter.setdefault(num, 0) + 1
        freq_counter = dict(sorted(freq_counter.items(), key=lambda item:item[1], reverse=True))
        
        result_list = list(freq_counter.keys())
        
        result = []
        for i in range(k):
            result.append(result_list[i])
        return result
            
            
            
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Inital Thoughts:
            # Let N = # of words in the list
            # Put everything into hash table by count O(N)
            # Then sort the hash table by the count O(NlogN) | O(log(n))
            # Return the first k elements O(Klog(n))
        # Time complexity
            # O(nlogn) => O(klog(n))
        # Another thought is, instead of sorting by the hash table, could we use a heap?
            # That way it can bubble up, or down based on the min-heap property and we can keep taking it
            # I believe the time complexity for a heap was O(log(n))
            
            return self.first_solution(nums, k)
            
    
            
                
        