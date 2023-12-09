pair<long long, long long> getMinMax(long long a[], int n) {
  
    long long mx=a[0];
    long long mn=a[0];
  
    for(int i=0; i<n;i++){
        if(a[i]>mx){
            mx = a[i];
        }
        else{
            if(a[i]<mn){
                mn = a[i];
            }
        }
    }
    
    return{mn,mx};
    
}
