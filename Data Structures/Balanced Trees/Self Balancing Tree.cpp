/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */

int max(int a, int b)
{
    return (a > b) ? a : b;
}

int height(node* ptr)
{
    if (ptr == NULL)
    {
        return -1;
    }
    else
    {
        return ptr->ht;
    }
}

int getBalanceFactor(node* ptr)
{
    if (ptr == NULL)
    {
        return 0;
    }
    else
    {
        return height(ptr->left) - height(ptr->right);
    }
}

node* leftRotate(node* x)
{
    node* y;
    node* t2;

    y = x->right;
    t2 = y->left;

    y->left = x;
    x->right = t2;

    x->ht = 1 + max(height(x->left), height(x->right));
    y->ht = 1 + max(height(y->left), height(y->right));

    return y;
}

node* rightRotate(node* y)
{
    node* x;
    node* t2;

    x = y->left;
    t2 = x->right;

    x->right = y;
    y->left = t2;

    y->ht = 1 + max(height(y->left), height(y->right));
    x->ht = 1 + max(height(x->left), height(x->right));

    return x;
}

node* insert(node* root, int val)
{
    if (root == NULL)
    {
        node* root = new node;
        root->val = val;
        root->left = NULL;
        root->right = NULL;
        root->ht = 0;
        return root;
    }

    if (val < root->val)
    {
        root->left = insert(root->left, val);
    }
    else if (val > root->val)
    {
        root->right = insert(root->right, val);
    }
    else
    {
        return root;
    }

    root->ht = 1 + max(height(root->left), height(root->right));

    int balanceFactor = getBalanceFactor(root);

    if (balanceFactor > 1 && val < root->left->val)
    {
        return rightRotate(root);
    }
    if (balanceFactor < -1 && val > root->right->val)
    {
        return leftRotate(root);
    }
    if (balanceFactor > 1 && val > root->left->val)
    {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }
    if (balanceFactor < -1 && val < root->right->val)
    {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }

    return root;
}
