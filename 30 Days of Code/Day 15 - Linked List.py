def insert(self,head,data):
    if head == None :
        head = Node(data)
    else :
        temp = head
        while temp.next != None :
            temp = temp.next
        temp.next = Node(data)
    return head
