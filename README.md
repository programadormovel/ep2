# IPT - Instituto de Pesquisas Tecnológicas
    Mestrado em Computação Aplicada
    2024.1 - Estruturas de Dados e Análise de Algoritmos
    Professor Dr. Eng. Eduardo Takeo Ueda
    Turma 8
    Adriano Domingues - RM: 43830

# Exercício Problema 2 - Árvore de Huffman
- Endereço do vídeo de apresentação: 

- Repositório do GitHub: https://github.com/programadormovel/ep2.git

    # Exercício-Programa 2
Compactação de arquivos com o algoritmo guloso de Huffman &nbsp;&nbsp;

Uma aplicação interessante de árvore binária é a compactação de arquivos usando os chamados códigos de Human. Os códigos de Human são códigos binários (atribuídos, por exemplo, a caracteres em um texto) de comprimentos variados que são determinados a partir da frequência de uso de um determinado caractere. &nbsp;&nbsp;

A ideia central é associar números binários com menos bits aos caracteres mais usados em um texto, possibilitando a sua compactação. O algoritmo de compactação usando códigos de Human tem três fases:

 (1) Cálculo da frequência de cada caractere no texto;

 (2) Execução do algoritmo de Human para construção de uma árvore binária
 (árvore de Human);

 (3) Codi cação propriamente dita.

 No algoritmo de descompactação usando os códigos de Human são necessárias duas fases:

 (1) Leitura e reconstrução da árvore de Human;

 (2) Decodi cação propriamente dita.

Para facilitar nosso trabalho podemos considerar pseudo-bits (caracteres 0s e 1s em vez de bits 0s e 1s).

O algoritmo de Human tem como propósito a construção de uma árvore binária baseada na frequência do uso de letras em um texto. Como exemplo, consideremos o texto a seguir.

 GNU's Not Unix
 
Temos que as frequências dos caracteres do texto apresentado como exemplo são:
 `\n': 1, ` ': 2, ` : 1, `G': 1, `N': 2, `U': 2, `i': 1, `n': 1, `o': 1, `s': 1, `t': 1, `x': 1.
 
 A árvore binária de Hu man será construída de baixo para cima (das folhas para a raiz), começando a partir das letras menos usadas até atingir a raiz. Em cada passo do algoritmo, existe uma coleção de árvores de Human. No início, cada uma das letras forma uma árvore que é composta apenas pela raiz e cujo conteúdo é a
 frequência com que esta letra ocorre no texto. Em seguida, são escolhidas as duas árvores com as menores frequências associadas e elas são transformadas em uma só árvore cujo valor é a soma do valor destas duas. Este processo é repetido até a alcançar a existência de uma única árvore (veja o algoritmo a seguir e a Figura 1).


 Algoritmo de Huffman

 Entrada: Conjunto C com n caracteres
 
  Saída: Árvore de Human

  1. Q←Conjunto de n árvores formadas por nós com os caracteres em C, e suas respectivas frequências
 2. para (i = 1;i < n; i++) faça
 3. r ←nova raiz
 4. filho esquerdo de r ← árvore A1 com frequência mínima em Q, sendo que A1 deve ser removido de Q
 5. filho direito de r ← árvore A2 com frequência mínima em Q, sendo que A2 deve ser removido de Q
 6. frequência de r ← soma das frequências de A1 e A2
 7. retorna árvore nal em Q


#
A codicação dos caracteres é realizada,associando-se 0 às arestas da árvore de Huffman que ligam um nó com seu lho esquerdo e 1, às arestas que ligam um nó com seu lho direito. O código correspondente a cada letra será formado pelo número binário associado ao caminho da raiz até a folha correspondente. Desta forma, os códigos resultantes da árvore de Human do exemplo são:

 `x': 000
 `\n': 0010
 ` : 0011
 ` ': 010
 `G': 0110
 `i': 0111
 2
`N': 100
 `U': 101
 `n': 1100
 `o': 1101
 `s': 1110
 `t': 1111

![Árvore de Huffman](https://github.com/programadormovel/ep2/blob/main/huffman.png)

 Figura 1: Árvore de Human
 
 Desta maneira, o arquivo compactado caria (lembre-se que são pseudo-bits):
 01101001010011111001010011011111010101110001110000010

 Perceba que para descompactar, basta percorrer a árvore da raiz até uma folha, obtendo os caracteres.
  Considerando o contexto apresentado sua tarefa consiste em implementar um programa para simular a compactação e descompactação de arquivos de texto. No caso do processo de compactação o programa deve receber como entrada um arquivo
 .txt e devolver como saída o arquivo .txt compactado (sequência de pseudo-bits 0 e 1). Para descompactar o programa deve receber o arquivo .txt compactado anteriormente e retornar um arquivo .txt com o texto original.

 Durante o processo de compactação deve ser mostrado na tela para o usuário: 
 
 (1)
 a frequência dos caracteres do texto; 
 
 (2) a árvore de Human obtida pelo algoritmo
 3
(percurso pré-ordem estudado na disciplina), e 

(3) sequência de pseudo-bits do texto
 compactado.

    class No:
        def __init__(self):
            self.chave = None
            self.frequencia = None
            self.esquerda = None
            self.direita = None
            self.proximo = None

    class ListaNos:
        def __init__(self):
            self.inicio = None
            self.tamanho = 0

As operações disponíveis são:
# para inicializar a lista de contagem de frequência
inicializa_lista_frequencia_com_zeros(lista_frequencia)

# método para preenchimento da lista de frequência
preenche_lista_frequencia(texto, lista_frequencia)

# método de criação da lista
criacao_da_lista(lista: ListaNos)

# método de inserção ordenada
inserir_ordenado(lista: ListaNos, no: No)

# método de preenchimento da lista de nós
preencher_lista(lista_frequencia, lista: ListaNos)

# método de impressão da lista de nós
imprimir_lista(lista: ListaNos)

# método de impressão da lista de frequência
imprimir_lista_frequencia(lista_frequencia)

# remoção do nó no início da lista
remover_no_do_inicio_da_lista(lista: ListaNos)

# montagem da árvore
montar_arvore(lista: ListaNos)

# impressão da árvore
imprimir_arvore(raiz: No, tamanho: int)

# preparação do dicionário de caracteres
aloca_dicionario(colunas)

# método de criação do dicionário
gerar_dicionario(dicionario, raiz, caminho, colunas)

# cálculo do tamanho do texto para compactação
calcula_tamanho_da_palavra(dicionario, texto)

# método de codificação
codificar(dicionario, texto)

# método de decodificação
decodificar(texto, raiz: No)

# menu de interação com a pessoa
menu_interativo()

# área de programação procedural, onde os objetos são carregados (instanciados) e chamados.
    if __name__ == '__main__'


Para executar o EP2 pelo Terminal do Visual Studio Code deve-se inserir os comandos:

- python arvore_huffman.py

O menu abaixo será disponibilizado:

Exercício Programa 2 - Árvore de Huffman
Tecle uma opção desejada (0 - para parar o programa):
1 - Compactar arquivo input.txt
2 - Descompactar arquivo zip.txt
Digite aqui a sua opção:

Digite a opção desejada e efetue a entrada da informação para obter resposta (saída):

- Opção 1: um arquivo chamado input.txt será lido e frase nele contida será compactada e gravada no arquivo chamado zip.txt.

    - Abaixo o resultado da escolha da opção 1

        1. Lista de frequência de caracteres no texto:

                32 = 8 =

                69 = 1 = E

                97 = 5 = a

                99 = 1 = c

                100 = 3 = d

                101 = 3 = e

                104 = 1 = h

                105 = 2 = i

                109 = 1 = m

                110 = 1 = n

                111 = 3 = o

                114 = 1 = r

                115 = 1 = s

                117 = 2 = u

                118 = 2 = v


                2. Árvore de Huffman

                Folha: s        Altura: 4

                Folha: i        Altura: 4

                Folha: u        Altura: 4

                Folha: v        Altura: 4

                Folha:          Altura: 2

                Folha: E        Altura: 5

                Folha: c        Altura: 5

                Folha: h        Altura: 5

                Folha: m        Altura: 5

                Folha: a        Altura: 3

                Folha: n        Altura: 5

                Folha: r        Altura: 5

                Folha: d        Altura: 4

                Folha: e        Altura: 4

                Folha: o        Altura: 4


                3. Texto codificado:

        1 0 0 0 0 0 0 1 0 0 1 0 0 0 0 1 1 1 1 0 0 1 0 0 1 1 1 1 1 0 1 1 0 0 0 1 1 0 1 1 0 0 1 1 0 0 0 1 1 1 0 0 0 1 0 0 1 0 1 1 1 1 0 1 1 0 1 0 1 0 0 1 1 1 1 1 0 1 1 0 0 1 1 1 0 1 1 0 1 1 1 0 1 1 1 1 0 0 1 1 1 1 0 0 1 1 0 1 0 1 0 0 1 1 0 0 0 1 1 1 0 1 1 0 1

Opção 2: Descompactação do arquivo zip.txt, irá gerar um arquivo descompactado chamado zip_decodificado.txt, e na tela o resultado abaixo:

 Texto decodificado: 

E  u     s  o  u     o     c  a  m  i  n  h  o     a     v  e  r  d  a  d  e     e     a     v  i  d  a 

# Referência Bibliográfica

- Prof. Dr. Eng. Eduardo Takeo Ueda. Árvore Binária e seus percursos. Aula 6 e 7. Estrutura de Dados e Algoritmos.

- https://airtonbjunior.github.io/mestrado/analysis-algorithms/presentation/huffman-tree.pdf
    - Acessado em 19/05/2024

- https://wagnergaspar.com/como-ler-nosso-arquivo-compactado-com-o-algoritmo-de-huffman/
    - Acessado em 19/05/2024

- https://pt.stackoverflow.com/questions/274060/ascii-em-python
    - Acessado em 19/05/2024

- https://www.youtube.com/@kutova. 
    - Acessado em 19/05/2024