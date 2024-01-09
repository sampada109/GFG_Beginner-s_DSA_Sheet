class Solution:
    def search(self, pat, txt):
        # code here
        p = 0
        l = []
        
        while(p<len(txt)):
            if (txt[p]==pat[0]) and (txt[p:p+len(pat)]==pat):
                l.append(p+1)
            p +=1
            
        return l
