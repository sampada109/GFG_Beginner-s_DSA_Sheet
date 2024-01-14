class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        
        l = []
        st = set()
        
        for i in range(m):
            tt = tuple(arr[i])
            if tt in st:
                l.append(i)
            else:
                st.add(tt)
        
        return l        
