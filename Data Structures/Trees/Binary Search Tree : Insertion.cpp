/*
Node is defined as 

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;

*/

node * insert(node * root, int value) {
    if(root == NULL)
    {
        root->data = value ;
    }
    else
    {
        node* temp = root ;
        if(temp->data > value)
        {
            if(temp->left == NULL)
            {
                temp->left = new node ;
                temp->left->data = value ;
            }
            else
            {
                insert(temp->left, value) ;
            }
        }
        else
        {
            if(temp->right == NULL)
            {
                temp->right = new node ;
                temp->right->data = value ;
            }
            else
            {
                insert(temp->right, value) ;
            }
        }
    }
    return root ;
}
