/*
   Find merge point of two linked lists
   Node is defined as
   struct Node
   {
       int data;
       Node* next;
   }
*/
int FindMergeNode(Node *headA, Node *headB)
{
    Node* temp;
    while(headA!=NULL)
    {
        temp=headB;
        while(temp!=NULL)
        {
            if(headA==temp)
            {
                return headA->data;
            }
            temp=temp->next;
        }
        headA=headA->next;
    }
    return 0;
    // Complete this function
    // Do not write the main method. 
}
