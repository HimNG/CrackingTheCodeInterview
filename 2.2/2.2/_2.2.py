class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist :
    #count=0
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    
    # kth last element with recursive method
    def kth_last_element_recursive(self,current,k):
        if current.next==None :
            return 1
        else:
            count=self.kth_last_element_recursive(current.next,k) + 1
            if count==k :
                print(current.data)
            return count
 
    # kth last element with non-recursive method
    def kth_last_element_non_recursive(self,k):
        temp1,temp2,count=self.head,self.head,1
        while count<k :
            temp2=temp2.next
            count=count+1
            
        while temp2.next :
            temp1=temp1.next
            temp2=temp2.next
            print(temp1.data) 
        
    #print all elements        
    def print_ll(self):
        ll=self.head
        while ll!=None :
            print(ll.data,end=" ")
            ll=ll.next
        print("")    
        
if __name__ == '__main__' :
    llist=linkedlist()
    llist.insert_at_begin(10)
    llist.insert_at_begin(14)
    llist.insert_at_begin(15)
    llist.insert_at_begin(1)
    llist.insert_at_begin(6)
    llist.print_ll()
    llist.kth_last_element_recursive(llist.head,3)
    llist.kth_last_element_non_recursive(4)
