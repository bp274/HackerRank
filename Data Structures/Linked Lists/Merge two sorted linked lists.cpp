/*
  Merge two sorted lists A and B as one linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* MergeLists(Node *headA, Node* headB)
{
    Node *temp,*head;
    if(headA==NULL&&headB==NULL)
    {
        return NULL;
    }
    head = temp = new Node ;
    while(headA!=NULL&&headB!=NULL)
    {
        if(headA->data<headB->data)
        {
            temp->data=headA->data;
            headA=headA->next;
        }
        else
        {
            temp->data=headB->data;
            headB=headB->next;
        }
        temp->next = new Node ;
        temp = temp->next ;
    }
    if(headB==NULL)
    {
        while(headA!=NULL)
        {
            temp->data=headA->data;
            headA=headA->next;
            if(headA!=NULL)
            {
                temp->next = new Node ;
                temp = temp->next ;
            }
        }
    }
    else
    {
        while(headB!=NULL)
        {
            temp->data=headB->data;
            headB=headB->next;
            if(headB!=NULL)
            {
                temp->next = new Node ;
                temp = temp->next ;
            }
        }
    }
    temp->next = NULL;
    return head;
  // This is a "method-only" submission. 
  // You only need to complete this method 
}
