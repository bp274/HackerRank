/*
    Insert Node in a doubly sorted linked list 
    After each insertion, the list should be sorted
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* SortedInsert(Node *head, int data)
{
    Node *temp1, *temp2, *temp3 ;
    if(head == NULL)
    {
        head = new Node ;
        head->data = data ;
        head->next = NULL ;
        head->prev = NULL ;
    }
    else
    {
        temp1 = head ;
        temp2 = NULL ;
        while(temp1 != NULL && temp1->data < data)  //check for null before data otherwise segmentation fault
        {
            temp2 = temp1 ;
            temp1 = temp1->next ;
        }
        if(temp1 == head)
        {
            head = new Node ;
            head->data = data ;
            head->next = temp1 ;
            temp1->prev = head ;
            head->prev = NULL ;
        }
        else
        {
            temp3 = new Node ;
            temp3->data = data ;
            temp2->next = temp3 ;
            temp3->prev = temp2 ;
            temp3->next = temp1 ;
            if(temp1 != NULL)
            {
                temp1->prev = temp3 ;
            }
        }
    }
    return head ; 
}
