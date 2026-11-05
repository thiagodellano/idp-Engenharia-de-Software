# Sistema de média acadêmica

Projeto da atividade da imagem: implementação orientada a objetos em JavaScript, C++ e Python, com notas iguais, recuperação e menções.

## Regras implementadas

- São informadas três avaliações, cada uma de 0 a 10, com o mesmo peso. A média inicial é a soma dividida por três.
- Média inicial igual ou superior a 6,0: aprovado.
- Média inicial abaixo de 6,0: verifica-se a recuperação. Se a diferença entre a maior e a menor nota for **maior que 3,33**, há reprovação automática.
- Se a diferença for até 3,33, o aluno pode fazer uma recuperação. A nota informada substitui a menor das três notas e a média final é recalculada. Média final a partir de 6,0 aprova; abaixo de 6,0 reprova.
- Menção da média final: abaixo de 6,0 = MI; de 6,0 a menos de 8,0 = MM; de 8,0 a menos de 9,0 = MS; de 9,0 a 10,0 = SS.
- As notas fora de 0 a 10 e entradas não numéricas são rejeitadas.

Quando o programa detectar recuperação necessária, solicita a nota da recuperação. Se a classe for usada por outro programa sem essa nota, seu estado é `Recuperação necessária`. A menção é sempre derivada da média final (portanto, uma nota abaixo de 6,0 resulta em MI mesmo quando a situação é reprovação automática).

## Arquivos

```text
media-academica/
├── javascript/
│   ├── media.js
│   └── media.test.js
├── cpp/
│   ├── main.cpp
│   └── testes.cpp
├── python/
│   ├── media.py
│   └── test_media.py
└── README.md
```

## Como executar

Abra um terminal na pasta `media-academica` e escolha a linguagem. Os exemplos abaixo usam PowerShell.

### JavaScript

Requer Node.js. Para iniciar o programa:

```powershell
node .\javascript\media.js
```

Para executar os testes:

```powershell
node --test .\javascript\media.test.js
```

### C++

Requer um compilador C++17, como g++ ou clang++.

```powershell
g++ -std=c++17 -Wall -Wextra .\cpp\main.cpp -o .\cpp\media.exe
.\cpp\media.exe
```

Para compilar e executar os testes:

```powershell
g++ -std=c++17 -Wall -Wextra .\cpp\testes.cpp -o .\cpp\testes.exe
.\cpp\testes.exe
```

### Python

Requer Python 3.10 ou superior.

```powershell
python .\python\media.py
```

Para executar os testes:

```powershell
python -m unittest discover -s .\python -p "test_*.py" -v
```

## Como a implementação foi montada

1. **Modele a entidade.** A classe `Media` recebe três notas e, opcionalmente, a nota da recuperação.
2. **Valide os dados.** O construtor rejeita qualquer nota que não seja numérica e esteja no intervalo fechado de 0 a 10.
3. **Calcule a média inicial.** Some as três notas e divida por três; não há pesos diferentes.
4. **Determine a situação.** Se a média inicial alcançar 6,0, aprove. Caso contrário, compare maior e menor notas: diferença acima de 3,33 reprova automaticamente; diferença até 3,33 permite recuperação.
5. **Aplique a recuperação.** Troque a menor nota pela nota da recuperação e recalcule a média. A recuperação substitui a nota, não é uma quarta avaliação.
6. **Converta a média em menção.** Aplique os quatro intervalos MI, MM, MS e SS.
7. **Exiba e teste.** O programa de console mostra média com duas casas, menção e situação. Os testes cobrem os cortes, os extremos de validação, recuperação suficiente/insuficiente e reprovação automática.

## Observação de interpretação

A atividade chama de recuperação a substituição da menor nota, mas não informa uma fórmula diferente para o resultado da recuperação. O projeto interpreta a regra literalmente: a nota obtida na recuperação ocupa o lugar da menor nota e a média aritmética é refeita. O limite de 3,33 é tratado como elegível; apenas diferença estritamente maior que 3,33 gera reprovação automática.
