//
// Created by Jorge Onieva on 6/1/16.
//

#ifndef TEMP_NODE_H
#define TEMP_NODE_H


class BinTreeNode{
public:
    int value;
    BinTreeNode *left;
    BinTreeNode *right;

    BinTreeNode(int value){
        this->value = value;
        left = NULL;
        right = NULL;
    }
};



#endif //TEMP_NODE_H
