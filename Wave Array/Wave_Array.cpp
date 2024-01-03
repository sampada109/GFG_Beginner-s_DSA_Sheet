void convertToWave(int n, vector<int>& arr){
        
        // Your code here
        for(int i=1;i<n;i+=2){
            swap(arr[i-1],arr[i]);
        }
        
        
    }
