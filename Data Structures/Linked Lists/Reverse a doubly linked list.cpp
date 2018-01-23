/*
   Reverse a doubly linked list, input list may also be empty
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* Reverse(Node* head)
{
    Node *temp1, *temp2, *temp3 ;
    temp1 = head ;
    temp3 = NULL ;
    while(temp1 != NULL)
    {
        temp2 = temp1->next ;
        temp1->next = temp3;
        temp1->prev = temp2;
        if(temp1 != head)
        {
            temp3->prev = temp1 ;
        }
        temp3 = temp1 ;
        temp1 = temp2 ;
    }
    head = temp3 ;
    return head ;
    // Complete this function
    // Do not write the main method. 
}
