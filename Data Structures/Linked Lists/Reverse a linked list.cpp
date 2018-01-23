/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element  
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Reverse(Node *head)
{
    Node *temp1,*temp2,*temp3;
    temp1=head;
    temp2=new Node;
    temp3=NULL;
    while(temp1!=NULL)
    {
        temp2=temp1->next;
        temp1->next=temp3;
        temp3=temp1;
        temp1=temp2;
    }
    head=temp3;
    return head;
  // Complete this method
}
