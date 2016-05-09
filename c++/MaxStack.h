//
// Created by Jorge Onieva on 4/10/16.
//

using namespace std;
//#include <stack>
//template <class T>
//class MaxStack: public std::stack<T>{
//public:
//    void push(T item){
//        // Invoke regular parent push
//        stack<T>::push(item);
//    }
//
//    void printAll(){
//        while(!this->empty()) {
//            cout << this->top() << ",";
//            this->pop();
//        }
//    }
//};

class MaxStack{
    vector<int> elems;
    int maxValue = -10000;
    vector<int> indexes;
public:
    void push(int elem){
        elems.insert(elems.end(), elem);
        if (elem >= maxValue) {
            // Insert a new position that will point to this item
            indexes.push_back(elems.size()-1);
            // Update max value
            maxValue = elem;
            cout << "Max value updated\n";
        }
    }

    int pop(){
        if (elems.empty())
           throw std::invalid_argument("empty stack");
        int i = elems.back();
        cout << "Pop: " << i << "\n";
        elems.pop_back();
        if (i == maxValue){
            // Remove last index
            indexes.pop_back();
            // Update new max value
            int p = indexes.back();
            maxValue = elems[p];

        }
        return i;
    }

    int getMaxValue(){
        return maxValue;
    }

    void printAll(){
        vector<int>::reverse_iterator it = elems.rbegin();
        while (it != elems.rend()){
            cout << *it << ",";
            it ++;
        }
        cout << "\n";
    }
};