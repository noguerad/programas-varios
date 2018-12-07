#include <cstdlib>
#import <iostream>

using namespace std;

void jocAdivina()
{
    srand(time(0));
    int random = std::rand() % 10;
    int contador = 0;
    int intent = -1;

    std::cout << "Adivina el nombre entre 0 i 9. Tens 3 intents.\n";
    while (contador < 3)
    {
        std::cin >> intent;
        if (intent > random)
        {
            std::cout << "Mes baix";
            contador++;
        }
        else if (intent < random)
        {
            std::cout << "Mes alt";
            contador++;
        }
        else
        {
            std::cout << "Correcte!";
            contador = 3;
        }
    }
    std::cout << "\nVols tornar-ho a intentar? s/n\n";
    string resposta;
    std::cin >> resposta;
    if (resposta == "s")
        jocAdivina();
}

int main()
{
    jocAdivina();
    return 0;
}
