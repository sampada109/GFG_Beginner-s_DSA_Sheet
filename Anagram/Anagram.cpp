sort(a.begin(),a.end());
                sort(b.begin(),b.end());
                int n1=a.size();
                                int n2=b.size();
                                int n=max(n1,n2);
                         
                                int count =0;
                for(int i=0;i<n;i++){
                    if(a[i]==b[i]){
                        count ++;
                    }
                }
                if(count==n)
                return true;
                else return false;
