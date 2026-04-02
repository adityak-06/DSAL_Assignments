#include <iostream>
#include <string>
using namespace std;

class Node {
public:
    char data;
    Node* next;
    Node(char val){
        data = val;
        next = NULL;
    }
};

class Stack {
    Node* top;
public:
    Stack(){ top = NULL; }

    void push(char x){
        Node* temp = new Node(x);
        temp->next = top;
        top = temp;
    }

    char pop(){
        if(!top) return -1;
        char val = top->data;
        Node* temp = top;
        top = top->next;
        delete temp;
        return val;
    }

    char peek(){
        if(!top) return -1;
        return top->data;
    }

    bool isEmpty(){
        return top == NULL;
    }
};

int precedence(char op){
    if(op=='+'||op=='-') return 1;
    if(op=='*'||op=='/') return 2;
    if(op=='^') return 3;
    return 0;
}

string infixToPostfix(string infix){
    Stack s;
    string postfix="";

    for(char c:infix){
        if(isalpha(c)) postfix+=c;
        else if(c=='(') s.push(c);
        else if(c==')'){
            while(!s.isEmpty() && s.peek()!='(')
                postfix+=s.pop();
            s.pop();
        }
        else{
            while(!s.isEmpty() && precedence(s.peek())>=precedence(c))
                postfix+=s.pop();
            s.push(c);
        }
    }

    while(!s.isEmpty())
        postfix+=s.pop();

    return postfix;
}

int main(){
    string infix;
    cout<<"Enter infix: ";
    cin>>infix;

    cout<<"Postfix: "<<infixToPostfix(infix)<<endl;
    return 0;
}