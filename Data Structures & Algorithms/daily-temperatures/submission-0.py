class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        m_stack = []
        
        for i in range(len(temperatures)):
            if not m_stack:
                m_stack.append(i)
                continue
            
            count = 0
            while m_stack and temperatures[i] > temperatures[m_stack[-1]]:
                j = m_stack.pop()
                ans[j] = i-j
                
            m_stack.append(i)
        return ans
            

            