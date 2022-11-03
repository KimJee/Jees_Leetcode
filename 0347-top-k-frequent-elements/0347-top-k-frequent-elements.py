import heapq

class Solution:
    
    def first_solution(self, nums:List[int], k: int):
        
        # Fill in the freq_counter
        freq_counter = {}
        for num in nums:
            freq_counter[num] = freq_counter.setdefault(num, 0) + 1

        # Review this line, (how to sort a dictionary by value)
        freq_counter = dict(sorted(freq_counter.items(), key=lambda item:item[1], reverse=True))
        
        # Turn the freq_list into a list
        result_list = list(freq_counter.keys())
        
        # Filter the list
        result = []
        for i in range(k):
            result.append(result_list[i])
        return result
            
    def second_solution(self, nums:List[int], k:int):
        
        # Fill in the freq_counter
        freq_counter = {}
        for num in nums:
            freq_counter[num] = freq_counter.setdefault(num, 0) + 1
        
        # Create a heap
        item_list = [(v*-1, k) for (k, v) in freq_counter.items()]
        print(item_list)
        heapq.heapify(item_list)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(item_list)[1])
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
            
            return self.second_solution(nums, k)
            
    
            
                
        