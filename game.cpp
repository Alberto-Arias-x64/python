#include<iostream>

using namespace std;

class player
{
    public:
        void callinput()
        {
            char userInput = ' ';
            cin >> userInput;
            switch (userInput)
            {
            case 'w':
                cout<<"Adelante";
                break;
            
            case 'a':
                cout<<"Derecha";
                break;
            
            case 's':
                cout<<"Atras";
                break;
            
            case 'd':
                cout<<"Izquierda";
                break;
            
            default:
                cout<<"C hace kk";
                break;
            }
            cout<<endl;
        }
    protected:
        int coordenadas[2]={0,0};
};

class mapa
{
    public:
    int id;
    
};

int main()
{
    bool gameover = false;
    player hero;
    while (gameover == false)
    {
        hero.callinput();
    }
    return 0;
}