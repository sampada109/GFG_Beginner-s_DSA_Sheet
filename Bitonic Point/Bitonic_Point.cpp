class Solution{
public:
	
	int findMaximum(int arr[], int n) {
	    // code here
	    sort(arr,arr+n);
	    return arr[n-1];
	}
};
