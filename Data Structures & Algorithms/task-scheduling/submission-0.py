from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #create array of space 3 times most  
        counts = Counter(tasks)
        max_count = max(counts.values())
        num_max = sum(1 for c in counts.values() if c == max_count) # ties at the top

        frame = (max_count - 1) * (n + 1) + num_max
        return max(len(tasks), frame)