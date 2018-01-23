/*
  Delete Node at a given position in a linked list 
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Delete(Node *head, int position)
{
    Node* temp=head;
    if(position!=0)
    {
        for(int i=1; i<position; i++)
        {
            temp=temp->next;
        }
        temp->next=temp->next->next;
    }
    else
    {
        head=head->next;
    }
    return head;
    // Complete this method
}
