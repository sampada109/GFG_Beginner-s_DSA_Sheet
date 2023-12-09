def getMinMax( a, n):
    
    mn = a[0]
    mx = a[0]
    
    for i in range(len(a)):
        if a[i]>mx:
            mx = a[i]
        else:
            if a[i]<mn:
                mn = a[i]
                
    return(mn,mx)            
    
