int height(Node* root)
{
    int x = -1, y = -1 ;
    if(root != NULL)
    {
        x = 1 + height(root->left) ;
        y = 1 + height(root->right) ;
    }
    return x > y ? x : y ;
}
