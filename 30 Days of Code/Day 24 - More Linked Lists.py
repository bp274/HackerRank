    def removeDuplicates(self,head):
        temp1 = temp2 = head
        while temp1 :
            temp2 = temp1
            while temp2.next :
                if temp1.data == temp2.next.data :
                    temp2.next = temp2.next.next
                else :
                    temp2 = temp2.next
            temp1 = temp1.next
        return head
