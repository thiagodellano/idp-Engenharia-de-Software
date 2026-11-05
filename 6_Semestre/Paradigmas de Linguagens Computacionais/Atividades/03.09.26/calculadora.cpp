#include <iostream>
using namespace std;

int main() {

    int opcao;
    double a, b, resultado;

    do {

        cout << "\n--- CALCULADORA ---\n";
        cout << "1 - Soma\n";
        cout << "2 - Multiplicacao\n";
        cout << "3 - Divisao\n";
        cout << "4 - Subtracao\n";
        cout << "5 - Elevar ao quadrado\n";
        cout << "6 - Exponencial\n";
        cout << "7 - Taylor Exponencial\n";
        cout << "8 - Taylor Seno\n";
        cout << "0 - Sair\n";

        cout << "Escolha: ";
        cin >> opcao;

        if (opcao == 1) {

            cout << "Digite dois numeros: ";
            cin >> a >> b;

            resultado = a + b;

            cout << "Resultado: " << resultado << endl;
        }

        else if (opcao == 2) {

            cout << "Digite dois numeros: ";
            cin >> a >> b;

            resultado = a * b;

            cout << "Resultado: " << resultado << endl;
        }

        else if (opcao == 3) {

            cout << "Digite dois numeros: ";
            cin >> a >> b;

            if (b != 0) {
                resultado = a / b;
                cout << "Resultado: " << resultado << endl;
            }
            else {
                cout << "Nao pode dividir por zero." << endl;
            }
        }

        else if (opcao == 4) {

            cout << "Digite dois numeros: ";
            cin >> a >> b;

            resultado = a - b;

            cout << "Resultado: " << resultado << endl;
        }

        else if (opcao == 5) {

            cout << "Digite um numero: ";
            cin >> a;

            resultado = a * a;

            cout << "Resultado: " << resultado << endl;
        }

        else if (opcao == 6) {

            int n;
            resultado = 1;

            cout << "Digite n: ";
            cin >> n;

            for (int i = 0; i < n; i++) {
                resultado = resultado * 2.72;
            }

            cout << "Resultado: " << resultado << endl;
        }

        else if (opcao == 7) {

            double x;
            int termos;

            cout << "Digite x: ";
            cin >> x;

            cout << "Digite a quantidade de termos: ";
            cin >> termos;

            resultado = 1;
            double termo = 1;

            for (int i = 1; i < termos; i++) {

                termo = termo * x / i;
                resultado = resultado + termo;
            }

            cout << "Resultado aproximado: " << resultado << endl;
        }

        else if (opcao == 8) {

            double x;
            int termos;

            cout << "Digite x em radianos: ";
            cin >> x;

            cout << "Digite a quantidade de termos: ";
            cin >> termos;

            resultado = x;
            double termo = x;
            int sinal = -1;

            for (int i = 1; i < termos; i++) {

                termo = termo * x * x;
                termo = termo / ((2 * i) * (2 * i + 1));

                resultado = resultado + sinal * termo;

                sinal = sinal * -1;
            }

            cout << "Resultado aproximado: " << resultado << endl;
        }

        else if (opcao != 0) {
            cout << "Opcao invalida." << endl;
        }

    } while (opcao != 0);

    return 0;
}