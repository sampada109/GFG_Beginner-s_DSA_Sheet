class Solution:
    def insertionSort(self, head):
        #code here
        
        if not head or not head.next:
            return head
            
        temp = Node(-1)
        temp.next = head
            
        current = head
        
        while(current.next):
            if current.next.data < current.data:
                insert = current.next
                current.next = current.next.next
                
                pt = temp
                while(pt and pt.next.data) <(insert.data):
                    pt = pt.next
                
                insert.next = pt.next
                pt.next = insert
            
            else:
                current = current.next
                
        return temp.next        
        
        
