class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        ans = 0
        
        for i in tokens:
            stack.append(i)
            if i in operators:
                oper = stack.pop()
                a = int(stack.pop())
                b = int(stack.pop())
                
                if oper == "+":
                    ans = a + b
                elif oper == "-":
                    ans = b - a
                elif oper == "*":
                    ans = b* a
                else:
                    ans = int(b/a)
                stack.append(ans)
            ans = int(stack[-1])
        
        return ans
                
            

                    
