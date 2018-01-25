/* 
The structure of the node is

typedef struct node
{
    int freq;
    char data;
    node * left;
    node * right;
    
}node;

*/


void decode_huff(node * root,string s)
{
    int i = 0 ;
    node* temp ;
    temp = root ;
    for(int i = 0 ; s[i] != '\0' ; i++)
    {
        if(s[i] == '0')
        {
            temp = temp->left ;
        }
        else
        {
            temp = temp->right ;
        }
        if(temp->data != '\0')
        {
            cout << temp->data ;
            temp = root ;
        }
    }
}
