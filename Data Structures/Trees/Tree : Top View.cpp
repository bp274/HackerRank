void left_side(node* root)
{
    if(root->left != NULL)
    {
        left_side(root->left) ;
        cout << root->left->data << " " ;
    }
}

void right_side(node* root)
{
    if(root->right != NULL)
    {
        cout << root->right->data << " " ;
        right_side(root->right) ;
    }
}

void topView(node * root)
{
    if(root != NULL)
    {
        left_side(root) ;
        cout << root->data << " " ;
        right_side(root) ;
    }
}
