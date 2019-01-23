class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist :
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    
    
    def insert_at_end(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
            
        temp.next=node
    
    # remove duplicates with hashing 
    def removeDup_with_hash(self):
        temp=self.head
        s=set()
        s.add(temp.data)
        while temp.next:
            if temp.next.data in s :
                temp.next=temp.next.next
            else:
                s.add(temp.data)
                temp=temp.next


    def print_ll(self):
        ll=self.head
        while ll!=None :
            print(ll.data,end=" ")
            ll=ll.next
            
    #remove Duplicates without extra space
    def removeDup_without_hash(self):
        if not self.head.next :
            return
        
        temp1,temp2=self.head,self.head.next
        while temp1 :
            temp2=temp1.next
            while temp2 :
                if temp2.data == temp1.data :
                    temp2=temp2.next
                else :
                    temp1.next=temp2
                    temp2=temp2.next
                    break
            if  temp2==None :
                break
            temp1=temp2
        
if __name__ == '__main__' :
    llist=linkedlist()
    llist.insert_at_begin(10)
    llist.insert_at_begin(14)
    llist.insert_at_begin(10)
    llist.insert_at_begin(10)
    llist.insert_at_begin(10)
    llist.insert_at_end(11)
    llist.print_ll()
    llist.removeDup_with_hash()
    #llist.removeDup_without_hash()
    
    print("")
    llist.print_ll()
