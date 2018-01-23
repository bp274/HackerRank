/*
  Get Nth element from the end in a linked list of integers
  Number of elements in the list will always be greater than N.
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int GetNode(Node *head,int positionFromTail)
{
    Node* temp=head;
    int count=0;
    while(temp!=NULL)
    {
        temp=temp->next;
        count++;
    }
    temp=head;
    count = count - positionFromTail - 1 ;
    while(count--)
    {
        temp=temp->next;
    }
    return temp->data;
  // This is a "method-only" submission. 
  // You only need to complete this method. 
}
