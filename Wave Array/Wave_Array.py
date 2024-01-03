class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        # code here
        for i in range(1,n,2):
            num1 = a[i-1]
            num2 = a[i]
            a[i-1] = num2
            a[i] = num1
            
        return a   
