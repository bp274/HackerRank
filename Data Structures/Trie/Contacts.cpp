#include <bits/stdc++.h>
#define ALPHABET_SIZE 26

using namespace std;

class Node
{
    public:
        Node* children[ALPHABET_SIZE];
        int numberOfWords;
        bool isEndOfWord;
};

class Trie
{
    public:
        Node* getNode()
        {
            Node* ptr = new Node;

            for (int i = 0; i < ALPHABET_SIZE; i++)
            {
                ptr->children[i] = NULL;
            }
            ptr->numberOfWords = 0;
            ptr->isEndOfWord = false;

            return ptr;
        }

        void insert(Node* root, string name)
        {
            Node* temp = root;

            for (int i = 0; i < name.length(); i++)
            {
                int index;
                index = name[i] - 'a';

                if (temp->children[index] == NULL)
                {
                    temp->children[index] = getNode();
                }
                temp = temp->children[index];
                temp->numberOfWords += 1;
            }
            temp->isEndOfWord = true;
        }

        int getCount(Node* root, string partial)
        {
            Node* temp = root;

            for (int i = 0; i < partial.length(); i++)
            {
                int index;
                index = partial[i] - 'a';

                if (temp->children[index] == NULL)
                {
                    return 0;
                }
                else
                {
                    temp = temp->children[index];
                }
            }

            return temp->numberOfWords;
        }
};

int main()
{
    Trie trie;

    Node* root;
    root = trie.getNode();

    int n;
    cin >> n;

    while(n--)
    {
        string str;
        cin >> str;

        if (str[0] == 'a')
        {
            string name;
            cin >> name;

            trie.insert(root, name);
        }
        else
        {
            string partial;
            cin >> partial;

            cout << trie.getCount(root, partial) << endl;
        }
    }

    return 0;
}
