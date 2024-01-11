class Solution:

    def removeKdigits(self, S, K):
        # code here
        stack=[]
        
        for i in S:
            while stack and K>0 and i<stack[-1]:
                stack.pop()
                K -=1
                
            stack.append(i)
            
        while K>0:
            stack.pop()
            K-=1
            
            
        res = ''.join(stack).lstrip('0')
        
        return res if res else '0'
