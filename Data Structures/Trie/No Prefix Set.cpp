#include <bits/stdc++.h>
#define ALPHABET_SIZE 10

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

        bool isPrefix(Node* root, string partial)
        {
            Node* temp = root;
            int flag = 0;

            for (int i = 0; i < partial.length(); i++)
            {
                int index;
                index = partial[i] - 'a';

                if (temp->children[index] == NULL)
                {
                    flag = -1;
                    break;
                }
                else
                {
                    temp = temp->children[index];
                    if (temp->isEndOfWord == true)
                    {
                        flag = 1;
                        break;
                    }
                }
            }

            if (flag == -1)
            {
                return false;
            }
            else
            {
                return true;
            }
        }
};

int main()
{
    Trie trie;

    Node* root;
    root = trie.getNode();

    bool isGood = true;

    int n;
    cin >> n;

    while(n--)
    {
        string str;
        cin >> str;

        if (trie.isPrefix(root, str))
        {
            cout << "BAD SET" << endl;
            cout << str;

            isGood = false;
            break;
        }

        trie.insert(root, str);
    }
    if (isGood)
    {
        cout << "GOOD SET";
    }
    return 0;
}
