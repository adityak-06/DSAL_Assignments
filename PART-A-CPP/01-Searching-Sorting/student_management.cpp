#include<iostream>
#include<cstring>
using namespace std;

struct student{
    float cgpa;
    char name[50];
    int id;
};

void input(student* s, int n){
    for(int i=0;i<n;i++){
        cout<<"\nEnter student details:\n";
        cout<<"Name: ";
        cin>>s[i].name;
        cout<<"ID: ";
        cin>>s[i].id;
        cout<<"CGPA: ";
        cin>>s[i].cgpa;
    }
}

void display(student* s, int i){
    cout<<"\nName: "<<s[i].name;
    cout<<"\nID: "<<s[i].id;
    cout<<"\nCGPA: "<<s[i].cgpa<<endl;
}

void displayAll(student* s, int n){
    for(int i=0;i<n;i++){
        display(s,i);
    }
}

// Linear Search
void linearSearch(student* s, int n, int id){
    bool found=false;
    for(int i=0;i<n;i++){
        if(s[i].id==id){
            cout<<"Student Found at index "<<i<<endl;
            display(s,i);
            found=true;
            break;
        }
    }
    if(!found) cout<<"Student not found\n";
}

// Bubble Sort by Name
void sortByName(student* s, int n){
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(strcmp(s[j].name,s[j+1].name)>0){
                swap(s[j],s[j+1]);
            }
        }
    }
    cout<<"\nSorted by Name:\n";
    displayAll(s,n);
}

// Selection Sort by CGPA
void sortByCGPA(student* s, int n){
    for(int i=0;i<n;i++){
        int min=i;
        for(int j=i+1;j<n;j++){
            if(s[j].cgpa<s[min].cgpa)
                min=j;
        }
        swap(s[i],s[min]);
    }
    cout<<"\nSorted by CGPA:\n";
    displayAll(s,n);
}

// Binary Search (after sorting by ID)
void sortByID(student* s, int n){
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if(s[j].id<s[i].id)
                swap(s[i],s[j]);
        }
    }
}

void binarySearch(student* s, int n, int key){
    sortByID(s,n);
    int low=0, high=n-1;

    while(low<=high){
        int mid=(low+high)/2;
        if(s[mid].id==key){
            cout<<"Found at index "<<mid<<endl;
            display(s,mid);
            return;
        }
        else if(key>s[mid].id) low=mid+1;
        else high=mid-1;
    }
    cout<<"Student not found\n";
}

int main(){
    int n, choice, id;
    cout<<"Enter number of students: ";
    cin>>n;

    student* s=new student[n];
    input(s,n);

    do{
        cout<<"\n--- MENU ---\n";
        cout<<"1. Linear Search\n2. Binary Search\n3. Sort by Name\n4. Sort by CGPA\n5. Exit\n";
        cin>>choice;

        switch(choice){
            case 1:
                cout<<"Enter ID: ";
                cin>>id;
                linearSearch(s,n,id);
                break;
            case 2:
                cout<<"Enter ID: ";
                cin>>id;
                binarySearch(s,n,id);
                break;
            case 3:
                sortByName(s,n);
                break;
            case 4:
                sortByCGPA(s,n);
                break;
        }
    }while(choice!=5);

    delete[] s;
    return 0;
}