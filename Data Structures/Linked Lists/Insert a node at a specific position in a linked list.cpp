/*
  Insert Node at a given position in a linked list 
  head can be NULL 
  First element in the linked list is at position 0
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* InsertNth(Node *head, int data, int position)
{
    Node *temp=new Node,*temp1=head,*temp2=head;
    temp->data=data;
    if(position==0)
    {
        temp->next=head;
        head=temp;
    }
    else
    {
        for(int i=0; i<position-1; i++)
        {
            temp1=temp1->next;
        }
        temp2=temp1->next;
        temp1->next=temp;
        temp->next=temp2;
    }
    return head;
  // Complete this method only
  // Do not write main function. 
}
