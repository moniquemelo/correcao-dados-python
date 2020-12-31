## CORREÇÃO DE DADOS CORROMPIDOS E VALIDAÇÃO DOS DADOS

### INTRODUÇÃO:
Você é responsável por um software de gestão de estoque de produtos. Ao fazer uma alteração no sistema, uma rotina que não foi devidamente testada acabou quebrando todo o banco de dados. Por sorte, não houve perda completa dos dados, mas eles não estão mais no formato esperado pelo sistema. 

**MISSÃO:** Recuperar os dados e deixá-los no formato adequado novamente. Além disso, você precisará criar também alguns métodos para validação das correções.

**PROBLEMAS DETECTADOS NO BANCO DE DADOS CORROMPIDO:**

Banco de dados corrompido: https://gitlab.com/snippets/1818996

- [X] **1. Nomes** - Todos os nomes de produto tiveram alguns caracteres modificados, houve substituição de todos os "a" por "æ", "c" por "¢", "o" por "ø", "b" por "ß". É preciso reverter essas substituições para recuperar os nomes originais.

- [X] **2. Preços** - Os preços dos produtos devem ser sempre do tipo number, mas alguns deles estão no tipo string. É necessário transformar as strings novamente em number.

- [X] **3. Quantidades** - Nos produtos onde a quantidade em estoque era zero, o atributo "quantity" sumiu. Ele precisa existir em todos os produtos, mesmo naqueles em que o estoque é 0.

### ETAPAS: 

1. Recuperação dos dados originais do banco de dados:
Criar uma função para ler o arquivo broken-database.json e criar três funções para percorrer o banco de dados corrompido e corrigir os três erros descritos anteriormente, além de uma função para exportar um arquivo .json com a saída.
Portanto serão 5 funções:

        a) Ler o arquivo Json;

        b) Corrigir nomes;

        c) Corrigir preços;

        d) Corrigir quantidades;

        e) Exportar um arquivo JSON com o banco corrigido;
    
2. Validação do banco de dados corrigido:
Implementar funções para validar a recuperação do banco de dados. Todas essas funções deverão ter como input o banco de dados corrigido na Etapa 1. As funções de validação são:

        a) Uma função que imprime a lista com todos os nomes dos produtos, ordenados primeiro por 
        categoria em ordem alfabética e ordenados por id em ordem crescente. 
       
        b) Uma função que calcula qual é o valor total do estoque por categoria, ou seja, a soma do valor 
        de todos os produtos em estoque de cada categoria, considerando a quantidade de cada produto.

### SAÍDA:
- Um arquivo chamado ‘resolucao.py’ contendo o código fonte de toda a implementação. 
- Um arquivo chamado ‘saida.json’ contendo a resposta da execução do algoritmo.
