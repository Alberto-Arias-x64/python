#include "stdlib.h"
#include "stdio.h"
#include "string.h"

struct cliente
{
    char Name[50];
    char ID[10];
    float Credit;
    char Address[100];
};

int main(int argc, char const *argv[])
{
    struct cliente client1 = {0};
    strcpy(client1.Name , "El Simio");
    strcpy(client1.ID , "0000000001");
    client1.Credit = 1000;
    strcpy(client1.Address , "Hoarana kk 69");

    printf("el nombre del cliente es : %s", client1.Name);
    return 0;
}
