// Online C++ compiler to run C++ program online
#include <bits/stdc++.h>
using namespace std;

struct nod{
    int info;
    nod *urm, *ant;
};

void push(nod*& cap, nod*& coada, int x){
    nod *nou = new nod;
    nou->info = x;
    nou->urm = nullptr;
    nou->ant = coada;
    // schimbam urmatorul
    if(coada != nullptr)
        coada->urm = nou;
    // mutam coada
    coada = nou;
}

int front(nod* cap){
    return cap->info;
}

void pop(nod*& cap){
    nod *temp = cap;
    cap = cap->urm;
    cap->ant = nullptr;
    delete temp;
}




int main()
{
    nod *cap = nullptr;
    nod *coada = nullptr;

    int n;
    char s[6];
    cin >> n;
    for(int i = 1, x; i <= n; ++i){
        cin >> s;
        if(strcmp(s, "push") == 0)
            cin >> x, push(coada, x);
        else if(strcmp(s, "pop") == 0)
            pop(cap);
        else
            cout << front(cap) << '\n';
    }

    return 0;
}