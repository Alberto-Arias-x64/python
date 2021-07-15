#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;

class Enemy
{
    public:
    private:
    protected:
};

void drawmap(int heropos[2], char map[5][5])
{
    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < 5; j++)
            if(i == heropos[0] && j == heropos[1]) cout << 'h';
            else cout << map[i][j];
        cout << endl;
    }
}

int main()
{
    ofstream gamedata("gamedata.txt");
    if (gamedata.is_open()) cout << "se ha iniciado con exito" << endl;
    gamedata.close();
    bool gameover = false;
    char input = ' ';
    char map[5][5] = {{'1','1','1','1','1'},
    {'1','1','1','1','1'},
    {'1','1','1','1','1'},
    {'1','1','1','1','1'},
    {'1','1','1','1','1'}};
    int heropos[2] = {1,1};
    while (gameover == false)
    {
        drawmap(heropos,map);
        cin >> input;

        if (input == 'd') heropos[1]++;
        else if (input == 'a') heropos[1]--;
        else if (input == 'w') heropos[0]--;
        else if (input == 's') heropos[0]++;
        system("cls");
        system("intro");
    }
    return 0;
}