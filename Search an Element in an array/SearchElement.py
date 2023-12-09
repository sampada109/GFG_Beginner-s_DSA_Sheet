class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        #Your code here
        for i in range(len(arr)):
            if arr[i]==X:
                return(i)

        return(-1)
