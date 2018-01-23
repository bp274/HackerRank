struct Node
{
    node* data ;
    Node* link ;
};

void levelOrder(node* root)
{
    Node *front, *rear ;
    front = rear = new Node ;
    rear->data = root ;
    rear->link = NULL ;
    while(front)
    {
        if(front->data->left)
        {
            rear = rear->link = new Node ;
            rear->data = front->data->left ;
        }
        if(front->data->right)
        {
            rear = rear->link = new Node ;
            rear->data = front->data->right ;
        }
        rear->link = NULL ;
        cout << front->data->data << " " ;
        front = front->link ;
    }
}
