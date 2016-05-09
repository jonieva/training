//
// Created by Jorge Onieva on 4/9/16.
//

#ifndef TEMP_QUEUE_H
#define TEMP_QUEUE_H

#include <vector>
#include <stack>
using namespace std;

template <class T>
class Queue {
     //vector<T> elems;
    stack<T> stack1, stack2;

public:
    void insert(T elem){
        // elems.push_back(elem);
        // Move Stack 1 to Stack 2
        while (!stack1.empty()){
            stack2.push(stack1.top());
            stack1.pop();
        }
        // Push the element in main
        stack1.push(elem);
        // Get the other elements back
        while (!stack2.empty()){
            stack1.push(stack2.top());
            stack2.pop();
        }

    }

    T getFirst(){
        return stack1.top();
    }

    void printAllElements(){
        while(!stack1.empty()) {
            cout << stack1.top() << ",";
            stack1.pop();
        }

    }
};


#endif //TEMP_QUEUE_H
