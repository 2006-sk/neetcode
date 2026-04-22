from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        count = 0
        m_stack = []   # stores indices with increasing heights
        maxarea = 0
        n = len(heights)

        while count < n:
            # push while stack is empty OR heights are non-decreasing
            if not m_stack or heights[count] >= heights[m_stack[-1]]:
                m_stack.append(count)
                count += 1
            else:
                # current bar is smaller -> finalize rectangles for taller bars
                top = m_stack.pop()
                height = heights[top]

                # left boundary is the new stack top after pop
                left_smaller = m_stack[-1] if m_stack else -1
                width = count - left_smaller - 1

                maxarea = max(maxarea, height * width)

        # flush remaining bars (right boundary is n)
        while m_stack:
            top = m_stack.pop()
            height = heights[top]
            left_smaller = m_stack[-1] if m_stack else -1
            width = n - left_smaller - 1
            maxarea = max(maxarea, height * width)

        return maxarea