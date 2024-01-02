class Solution:
    def missingNumber(self,array,n):
        # code here
        og_sum = sum(list(range(1,n+1)))
        ob_sum = sum(array)
        return og_sum - ob_sum
