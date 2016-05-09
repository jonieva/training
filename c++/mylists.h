//
// Created by Jorge Onieva on 4/12/16.
//

#ifndef TEMP_MYLISTS_H
#define TEMP_MYLISTS_H

#endif //TEMP_MYLISTS_H

struct Node
{
    int info;
    struct Node *next;
};

class MyList{
    Node* plast;
    public:
    Node* pstart;
    void initList(int value){
        pstart = createNode(value);
    }

    Node* createNode(int value){
        Node* n = new(Node);
        n->info = value;
        n->next = NULL;
        return n;
    }

    bool hasLoops(){
        Node* n1 = pstart;
        Node* n2 = pstart;
        if (pstart == NULL)
            return false;
        if (pstart->next == pstart)
            return true;
        if (pstart->next == NULL)
            return false;
        do{
            n1 = n1->next;
            n2 = n2->next;
            if (n2 != NULL)
                n2 = n2->next;
            if (n1 == n2)
                // The first pointer reached the end and the two of them "met" there
                return true;
        } while (n1 != NULL && n2 != NULL);
        return false;
    }
};
