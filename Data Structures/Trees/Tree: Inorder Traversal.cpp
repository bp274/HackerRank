void inOrder(node *root) {
    if(root != NULL)
    {
        if(root->left != NULL)
        {
            inOrder(root->left) ;
        }
        cout << root->data << " " ;
        if(root->right != NULL)
        {
            inOrder(root->right) ;
        }
    }
}
