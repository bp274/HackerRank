void preOrder(node *root) {
    if(root != NULL) {
        cout << root->data << " " ;
        if(root->left != NULL) {
            preOrder(root->left) ;
        }
        if(root->right != NULL) {
            preOrder(root->right) ;
        }
    }
}
