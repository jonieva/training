using namespace std;
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <tuple>
#include "Queue.h"
#include "MaxStack.h"
#include "mylists.h"
#include "BinTreeNode.h"
#include <bitset>
#include <map>
#include <vector>
#include <stack>
#include <exception>

// https://www.interviewcake.com/question/python/find-rotation-point
u_long rotatedDictionary(string *list, u_long size){
//    string list[3] = {/*"ptolemaic", //0
//                     "retrograde", //1
//                     "supplant", //2
//                     "undulate",*/ //3
//            "xenoepist",
//            "asymptote", // 5
//            "babka", //6
//            /*"banoffee", //7
//            "engender", //8
//            "karpatka", *///9
//    }; //10

   if (size <= 2){
        // Return first
        return 0;
    }

    if (size == 3)
        return 1;   // This is the only way
    u_long p1 = 0;
    u_long p2 = size / 2;
    //u_long p3 = p2 + 1;
    u_long p3 = size - 1;
    string *w1, *w2, *w3, *w4;
    do {
        w1 = &list[p1];
        w2 = &list[p2];
        w3 = &list[p2+1];
        w4 = &list[p3];

        if (*w2 > *w1) {
            // Regular ascending order. Move the indexes
            p1 = p2 + 1;
            //printf("list[%d] = %s; list[%d] = %s", start, w2, end, w1);
            //start += offset;
        }
        if (*w4 > *w3) {
            // Regular ascending order. Move the indexes
            p3 = p2;
        }
        // Update new intermediate indexes
        p2 = (p3 - p1) / 2 + p1;
        printf ("%lu %lu %lu \n", p1, p2, p3);
    } while (p1 != p3);

    return p1;

}

// https://www.interviewcake.com/question/python/inflight-entertainment
bool moviesExist(int *moviesLengths, int numMovies, int flightLength){
    //int movies[5] = {10,20,15,30,5};
    // First, create a dictionary with all the possible values
    unordered_set<int> movies;
    int firstMovie;
    // For each movie, try to find its couple
    for (int i=0; i<numMovies; i++){
        firstMovie = moviesLengths[i];
        if (movies.find(flightLength-firstMovie) != movies.end())
           return true;
        movies.insert(firstMovie);
    }
    return false;
}

// https://www.interviewcake.com/question/python/cake-thief
int maxDuffelBagValue(){
//    int cakes[4][2] = {
//            {2,3},
//            {3,4},
//            {4,5},
//            {5,6}
//    };
//    int items = 4;
//    int W = 5;

    int cakes[4][2] = {
            {2,15},
            {3,90},
            {7,160},
            {0,0}
    };
    int items = 4;
    int W = 20;

    int values[W+1];
    for (int i=0; i<W+1; i++)
        values[i] = 0;

    for (int w=1; w<=W; w++) {
        for (int i = 0; i < items; i++) {
            if (cakes[i][0] <= w) {
                printf ("Position %d: compare current %d with previous position %d (val %d)\n", w, values[w], w-cakes[i][0], values[w-cakes[i][0]]);
                if (values[w-cakes[i][0]] + cakes[i][1] > values[w]) {
                    values[w] = values[w - cakes[i][0]] + cakes[i][1];
                    printf("Updating position %d: %d\n", w, values[w]);
                }
            }
        }
    }

    return values[W];

    // K0-1 would be implemented like this (review):
//    int m[items][W];
//    //vector<vector<int>> m(items, vector<int>(W));
//    for (int i=0; i<items; i++)
//        m[i][0] = 0;
//    for (int w=0; w<W; w++)
//        m[0][w] = 0;
//
//    for (int i=1; i<items; i++){
//        for (int j=0; j<W; j++){
//            if (cakes[i-1][0] > j){
//                // The item can't be in the solution because the weight is bigger than the limit
//                m[i][j] = m[i-1][j];
//            }
//            else{
//                // The item could be part of the solution
//                m[i][j] = max(m[i-1][j], m[i-1][j-cakes[i-1][0]] + cakes[i-1][1]);
//            }
//        }
//    }

    //return m[items-1][W-1];
}

void queue(){
    Queue<int> q;
    q.insert(1);
    q.insert(2);
    q.insert(3);
    q.printAllElements();
}

void myStack(){
    MaxStack s;
    cout << "insert 1\n";
    s.push(1);
    cout << "Max value: " << s.getMaxValue() << "\n";
    s.printAll();
    cout << "insert 2\n";
    s.push(2);
    cout << "Max value: " << s.getMaxValue() << "\n";
    s.printAll();
    cout << "insert 6\n";
    s.push(6);
    cout << "Max value: " << s.getMaxValue() << "\n";
    s.printAll();
    cout << "insert 4\n";
    s.push(4);
    cout << "Max value: " << s.getMaxValue() << "\n";
    //cout << "Pop: " << s.pop();
    s.printAll();
    s.pop();
    cout << "Max value: " << s.getMaxValue() << "\n";
    //cout << "Pop: " << s.pop();
    s.printAll();
    s.pop();
    cout << "Max value: " << s.getMaxValue() << "\n";
    s.printAll();
}

MyList createList(){
    MyList l;
    l.initList(10);
//    Node* n = l.createNode(2);
//    reinterpret_cast<int*>(reinterpret_cast<uintptr_t>(t1)^reinterpret_cast<uintptr_t>(t2));
//    l.pstart->next = n2;
    Node* n;
    Node* prev = l.pstart;
    for (int i=2; i<10; i++){
        n = l.createNode(i*10);
        prev->next = n;
        prev = n;
    }
    n = l.pstart;
    while (n != NULL) {
        cout << n->info << " ";
        n = n -> next;
    }
    return l;
}



int getKthTillLast(Node* n, int position){
    vector<int> positions;
    while (n != NULL){
        positions.push_back(n->info);
        n = n->next;
    }
    vector<int>::reverse_iterator it = positions.rbegin();
    it+=(position-1);
    return *it;
}

//string reverseOrder(string s){
//    //char *words[s.length()];
////    char *words = &s[0];
////    char *res = words;
////    while (!isspace(words[0]))
////        words++;
////        res
////
////    words++;
////    cout << words[0];
////    cout << c1[0];
//    return "";
//}

bool palyndrome(string s){
//    string s("iccia");
//    if (palyndrome(s))
//        cout << "yes";
//    else
//        cout << "no";

    map<char, int> characters;
    for(int i=0;i<(int)s.length();i++){
        if (characters.find(s[i]) == characters.end())
            // Insert new key
            characters[s[i]] = 1;
        else
            characters[s[i]]++;
    }
    bool foundOdd = false;
    for (map<char,int>::iterator it=characters.begin(); it!=characters.end(); ++it){
        if (it -> second % 2 != 0)
            if (foundOdd)
                return false;
            else
                foundOdd = true;
    }
    return true;
}

int getRepeatedNumber(int *items, int l, int max){
    int n = max;
    for (int i=0; i<l; i++) {
        cout << n << " xor " << items[i] << " = ";
        n = n ^ items[i];
        cout << n << "\n";
        if (n == max)
            return items[i];
    }
    return l;
}

bool isShuffled(){
    //vector<int> full = {1,2,3,5,6,4,10,9,7};
    vector<int> full = {4,1,2,3,8,9,7};
    vector<int> h1 = {1,2,3,8,9,7};
    vector<int> h2 = {4};
    // Iterators for all the lists
    vector<int>::iterator it = full.begin();
    vector<int>::iterator it1 = h1.begin();
    vector<int>::iterator it2 = h2.begin();

    while (it != full.end()){
        // The element must be in the first position of one of the two vectors
        if (*it == *it1)
            it1++;
        else if (*it == *it2)
            it2++;
        else
            return false;
        it++;
    }
    return true;
}




bool contains(vector<vector<int>> source, vector<int> v){
    bool found;
    for (int i=0; i<source.size(); i++){
        vector<int> v1 = source[i];
        found=true;
        for (int j=0; j<v1.size(); j++) {
            if (v1[j] != v[j]) {
                found = false;
                break;
            }
        }
        if (found)
            return true;
    }
    return false;
}

vector<vector<int>> coinChange(vector<int> coins, int totalSum){
    vector<vector<int>> empty;
    vector<vector<vector<int>>> solutions(totalSum + 1, empty);
    int numCoins = coins.size();
//    vector<int>::iterator coins_it = coins.begin();
    // Initial arrays
    for (int i=0;i<numCoins;i++) {
        solutions[coins[i]] = vector<vector<int>>(1);
        solutions[coins[i]][0] = vector<int>(3,0);
        solutions[coins[i]][0][i] = 1;
    }
    int i;
    for (i=1; i<totalSum; i++){
        for (int coin=0; coin < numCoins; coin++) {
            if (solutions[i] == empty) {
                solutions[i] = vector<vector<int>>(1);
                solutions[i][0] = vector<int>(3,0);
                solutions[i][0][coin] = 1;
            }
            else {
                for (int v=0; v<solutions[i].size(); v++){
                    vector<int> copy = vector<int>(solutions[i][v]);
                    copy[coin] ++;
                    // Get the sum
                    int sum=0;
                    for (int s=0; s<numCoins; s++)
                        sum+=(copy[s]*coins[s]);

                    if (sum <= totalSum && !contains(solutions[sum], copy))
                        solutions[sum].push_back(copy);
                }
            }

        }
        cout << "Solutions[" << i << "]=";
        for (int v1=0; v1<solutions[i].size(); v1++) {
            for (int v2 = 0; v2 < numCoins; v2++)
                std::cout << solutions[i][v1][v2] << ',';
            std::cout << ";";
        }
        cout << "\n";
    }

    cout << "Solutions[" << i << "]=";
    for (int v1=0; v1<solutions[i].size(); v1++) {
        for (int v2 = 0; v2 < numCoins; v2++)
            std::cout << solutions[i][v1][v2] << ',';
        std::cout << ";";
    }
    cout << "\n";

    return solutions[totalSum];
}





//BinTreeNode getTree(int *myArray, int length){
//    if (length == 0)
//        return NULL;
//    if (length == 1)
//        return BinTreeNode(myArray[0]);
//    if (length == 2) {
//        // Base case (TODO)
//        return BinTreeNode(myArray[0]);
//    }
//    BinTreeNode root(myArray[0]);
//    BinTreeNode *left = new BinTreeNode(myArray[1]);
//    BinTreeNode *right = new BinTreeNode(myArray[2]);
//    root.left = left;
//    root.right = right;
//
//    int index=3;
//    while (index < length){
//        // Create left child
//        BinTreeNode *child = new BinTreeNode(myArray[index++]);
//        left->left = child;
//        left = child;
//
//        if (index < length){
//            // Create right child
//            child = new BinTreeNode(myArray[index++]);
//            left->right = child;
//            right = child;
//        }
//    }
//    return root;
//}

BinTreeNode getTree(int *myArray, int length){
    int iroot = length / 2;
    BinTreeNode *root = new BinTreeNode(myArray[iroot]);
    int iPos = iroot-1;
    int rPos = iroot+1;

    BinTreeNode *current;
    while (iPos > 1){
        root->left = new BinTreeNode(myArray[iPos]);
        current = root->left;
    }

    root->left =
    root->right = new BinTreeNode(myArray[iroot+1]);

}

string printNode(BinTreeNode* node){
    string s =  "[" + to_string(node->value);
    if (node->left == NULL && node->right == NULL)
        return s + "]";

    if (node->left == NULL)
        s += "L[]";
    else
        s += "L" + printNode(node -> left) + ";";

    if (node->right == NULL)
        s += "R[]";
    else
        s += "R" + printNode(node -> right) + ";";

    s += "]";
    return s;
}



//int rand7(){
//    int sum=0;
//    for (int i=0; i<7; i++){
//        sum += std::experimental::randint(1, 5);
//    }
//
//    if (sum<=5) return 1;
//    if (sum>5 && sum<=10) return 2;
//    if (sum>10 && sum<=15) return 3;
//    if (sum>15 && sum<=20) return 4;
//    if (sum>20 && sum<=25) return 5;
//    if (sum>25 && sum<=30) return 6;
//    return 7;
//
//}


char* reverseWords(char* original, int length){
    int startingPos = 0;
    char c;
    int i = 0;
    for (; i<length; i++){
        if (original[i] == ' '){
            // Replace word
            for (int j=0; j<(i-startingPos)/2; j++){
                c = original[j+startingPos];
                original[j+startingPos] = original[i-j-1];
                original[i-j-1] = c;
            }
            startingPos=i+1;
        }
    }
    // Last word
    for (int j=0; j<(i-startingPos)/2; j++){
        c = original[j+startingPos];
        original[j+startingPos] = original[i-j-1];
        original[i-j-1] = c;
    }
    return original;
}

float reversePolishNotation(vector<string> operators){
    if (operators.size() == 0) return 0;
    stack<float> ops;
    vector<string>::iterator it = operators.begin();
    while (it != operators.end()){
        if (*it != "+" && *it != "-" && *it != "*" && *it != "/"){
            // Add to stack
            float f = stof(*it);
            ops.push(f);
        }
        else{
            // Perform operation
            if (ops.empty()){
                throw std::runtime_error("Bad syntax");
            }
            float op2 = ops.top();
            ops.pop();
            if (ops.empty()){
                throw std::runtime_error("Bad syntax");
            }
            float op1 = ops.top();
            ops.pop();
            if (*it == "+")
                ops.push(op1+op2);
            else if (*it == "-")
                ops.push(op1-op2);
            else if (*it == "*")
                ops.push(op1*op2);
            else if (*it == "/")
                ops.push(op1/op2);
            else
                throw std::runtime_error("Unknown operator");
        }
        it++;
    }
    if (ops.empty())
        throw std::runtime_error("Bad syntax");
    return ops.top();
}

bool isomorphic(string s1, string s2){
    if (s1.size() != s2.size())
        return false;
    std::map<char,char> mymap;
    std::map<char,char>::iterator it;

    for (int i=0; i<s1.size(); i++){
        it = mymap.find(s2[i]);
        if (it == mymap.end()){
            // New key
            mymap[s2[i]] = s1[i];
        }
        else if (mymap.at(s2[i]) != s1[i]){
            return false;
        }
    }
    return true;
}

//int shortestTransform(string start, string end, map<string> dict){
//    vector<tuple<int,string>> visited;
//    int minLength = 0;
//    visited.push_back(make_tuple(0, start));
//    //for (int i=0; i<start.size(); i++)
//}

int median (vector<int> v1, vector<int> v2){
    v1.insert(v1.end(), v2.begin(), v2.end());

    int m = v1.size();
    //int n = v2.size();
    int medianPos = m / 2;
    int pivot;
    //if (m >medianPos-1)
    //	pivot = v1[medianPos];
    //else
    //	pivot = v2[medianPos-m-1];
    pivot = v1[medianPos];

    // Partition

    int temp;
    for (int index=0;index<=medianPos;index++)
    {
        if (v1[index] > pivot){
            // Swap
            temp = v1[index];
            v1[index]  = v1[m-index-1];
            v1[m-index-1] = temp;
        }
    }
    return v1[medianPos];
}


int getRepeatedNumber(int values[], int size) {
    // Go to the "head" of the list, that will be the last element of the array
    int currentPos = size;
    // Move "size" steps to make sure we are in the loop
    for (int i = 0; i <= size; i++)
        currentPos = values[currentPos - 1];
    // Fix the current position and move until we get to the same point
    int next = values[currentPos - 1];
    int loopSize = 1;
    while (next != currentPos) {
        loopSize++;
        next = values[next - 1];
    }
    // Once that I know the size of the loop, I can start navigating the list using the "sticker" method
    currentPos = size;
    int sticker = currentPos;
    // Move the sticker "loopSize" positions
    for (int i = 0; i < loopSize; i++)
        sticker = values[sticker - 1];
    // Loop over the list until the two markers match
    while (sticker != currentPos) {
        currentPos = values[currentPos - 1];
        for (int i = 0; i < loopSize; i++)
            sticker = values[sticker - 1];
    }
    cout << "Result: " << values[currentPos-1];
    return values[currentPos-1];
}

void replace(char* s){
    int spaces = 0;
    int i=0;
    while (s[i] != '\0') {
        if (s[i] == ' ')
            spaces++;
        i++;
    }
    int newLength = spaces*2 + i;
    int addedPositions = 0;
    char s2[newLength];
    for (int j=0; j<i; j++) {
        if (s[j] == ' ') {
            s2[j+addedPositions++] = '%';
            s2[j+addedPositions++] = '2';
            s2[j+addedPositions] = '0';
        }
        else {
            s2[j+addedPositions] = s[j];
        }
    }
    cout << s2;
}

string removeDuplicates(string str){
    // TODO: full alphabet
    string alphabet = "abcdefg";
    char c;
    bool found;
    int originalLength = str.length();
    int currentIndex = 0;
    int forwardIndex = 0;
    int totalRemoved=0;

    for (int i=0;i<=alphabet.length();i++){
        c = alphabet[i];
        found = false;
        currentIndex=0;
        forwardIndex=0;
        while(currentIndex<originalLength-totalRemoved) {
            if (str[forwardIndex] == c) {
                if (!found) {
                    // The first time it's ok
                    found = true;
                    currentIndex++;
                }
                else {
                    // Just increase the number of characters that must be removed
                    totalRemoved++;
                }
            }
            else{
                if (forwardIndex != currentIndex)
                    str[currentIndex] = str[forwardIndex];
                currentIndex++;
            }
            forwardIndex++;
        }
    }
    return str.substr(0, originalLength-totalRemoved);
}


void rotateMatrix(int matrix[], int dimension) {
    int row,col, tmp;
    int nextValue;

    for (int i = 0; i <= dimension / 2; i++) {
        for (int j = 0; j <= dimension / 2; j++) {
            row = i;
            col = j;
            nextValue = matrix[col * dimension + dimension - row - 1];
            matrix[col * dimension + dimension - row - 1] = matrix[row * dimension + col];
            tmp = row;
            row = col;
            col = dimension - tmp - 1;

            for (int h = 0; h < 3; h++) {
                tmp = matrix[row * dimension + col];
                matrix[col * dimension + dimension - row - 1] = nextValue;
                nextValue = tmp;
                tmp = row;
                row = col;
                col = dimension - tmp - 1;
            }
        }
    }
}


int main() {
    int dimension = 3;
    int matrix[dimension*dimension];
    for (int i=0; i<dimension;i++)
        for (int j=0; j<dimension; j++)
            matrix[i*dimension+j] = i*dimension + j + 1;

    rotateMatrix(matrix, dimension);
    for (int i=0; i<dimension;i++){
        cout << "\n";
        for (int j=0; j<dimension; j++)
                // 4 iterations (squared matrix)
            cout << matrix[i*dimension + j] << " ";
    }

    return 0;
}