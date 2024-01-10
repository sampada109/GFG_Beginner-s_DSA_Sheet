class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		#Complete the function
		sum = 0
		ind = 0
		dict = {}
		
		for i in range(n):
		    sum = sum + arr[i]
		    rem = sum % K
		    if(rem<0):
		        rem = rem + K
		    if(rem==0):
		        ind = i+1
		    else:
		        if(rem in dict):
		            ind = max(ind, i+1-dict[rem])
		        else:
		            dict[rem] = i+1
	    return ind           

