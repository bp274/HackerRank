/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node* head)
{
    Node *fast, *slow;
    fast = slow = head;
    while(fast != NULL && slow != NULL && fast->next)
    {
        fast = fast->next->next;
        slow = slow->next;
        if(fast == slow)
        {
            return 1;
        }
    }
    // Complete this function
    // Do not write the main method
    return 0;
}
