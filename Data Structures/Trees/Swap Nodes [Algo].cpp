#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct node
{
    int data ;
    node* left ;
    node* right ;
    node* link ;
};

void inOrderSwap(node* root, int depth, int k)
{
    if(root)
    {
        if(depth % k == 0)
        {
            node* temp = root->left ;
            root->left = root->right ;
            root->right = temp ;
        }
        
        if(root->left)
        {
            inOrderSwap(root->left, depth + 1, k) ;
        }
        cout << root->data << " " ;
        if(root->right)
        {
            inOrderSwap(root->right, depth + 1, k) ;
        }
    }
}

void create(node* root, int n)
{
    int a, b ;
    node *front, *rear, *temp ;
    
    temp = front = rear = root ;
    rear->link = NULL ;
    
    for(int i = 1 ; i <= n ; i++)
    {
        cin >> a >> b ;
        
        if(a != -1)
        {
            temp->left = new node ;
            temp->left->data = a ;
        }
        else
        {
            temp->left = NULL ;
        }
        
        if(b != -1)
        {
            temp->right = new node ;
            temp->right->data = b ;
        }
        else
        {
            temp->right = NULL ;
        }
        
        if(temp->left)
        {
            rear = rear->link = temp->left ;
        }
        if(temp->right)
        {
            rear = rear->link = temp->right ;
        }
        front = front->link ;
        temp = front ;
    }
}

int main()
{
    node* root ;
    node* queue ;
    int n, a, b, t, k, depth = 1 ;
    
    cin >> n ;
    
    root = new node ;
    root->data = 1 ;
    
    create(root, n) ;
    
    cin >> t ;
    while(t--)
    {
        cin >> k ;
        inOrderSwap(root, depth, k) ;
        cout << endl ;
    }
    
    return 0;
}
