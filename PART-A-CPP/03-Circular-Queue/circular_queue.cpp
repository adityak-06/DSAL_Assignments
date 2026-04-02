#include<iostream>
using namespace std;

#define MAX 100

class Queue{
    int front, rear, size;
    int arr[MAX];

public:
    Queue(int s){
        size=s;
        front=rear=-1;
    }

    void enqueue(int val){
        if((rear+1)%size==front){
            cout<<"Overflow\n";
            return;
        }
        if(front==-1) front=0;
        rear=(rear+1)%size;
        arr[rear]=val;
    }

    void dequeue(){
        if(front==-1){
            cout<<"Underflow\n";
            return;
        }
        cout<<"Deleted "<<arr[front]<<endl;
        if(front==rear) front=rear=-1;
        else front=(front+1)%size;
    }

    void display(){
        if(front==-1){
            cout<<"Empty\n";
            return;
        }
        int i=front;
        while(true){
            cout<<arr[i]<<" ";
            if(i==rear) break;
            i=(i+1)%size;
        }
        cout<<endl;
    }
};

int main(){
    Queue q(5);
    q.enqueue(10);
    q.enqueue(20);
    q.display();
    q.dequeue();
    q.display();
    return 0;
}