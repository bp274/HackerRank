/*
The Node struct is defined as follows:
   struct Node {
      int data;
      Node* left;
      Node* right;
   }
*/

int nodes[10000], k = -1 ;

void inOrder(Node* root)
{
    if(root)
    {
        if(root->left)
        {
            inOrder(root->left) ;
        }
        nodes[++k] = root->data ;
        if(root->right)
        {
            inOrder(root->right) ;
        }
    }
}

bool checkBST(Node* root)
{
    inOrder(root) ;
    for(int i = 1 ; i < k ; i++)
    {
        if(nodes[i] <= nodes[i - 1])
        {
            return false ;
        }
    }
    return true ;
}
