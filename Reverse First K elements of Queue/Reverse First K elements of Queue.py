class Solution:
    def modifyQueue(self, q, k):
        # code here
        
        return(q[k-1::-1] + q[k:])
