/*
  Remove all duplicate elements from a sorted linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* RemoveDuplicates(Node *head)
{
    Node *temp1,*temp2;
    int x;
    if(head!=NULL)
        x=head->data;
    else
        return head;
    temp1=head->next;
    temp2=head;
    while(temp1!=NULL)
    {
        if(temp1->data==x)
            temp2->next=temp2->next->next;
        else
        {
            x=temp1->data;
            temp2=temp2->next;
        }
        temp1=temp1->next;
    }
    return head;
  // This is a "method-only" submission. 
  // You only need to complete this method. 
}
