
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

def inicializa_lista_frequencia_com_zeros(lista_frequencia):
    for n in range(0, 256):
        lista_frequencia.append(0)
        
    return lista_frequencia

def preenche_lista_frequencia(texto, lista_frequencia):
    for indice, caractere in enumerate(texto):
        for n in range(0, 255):
            caractere_traduzido = int(ord(caractere))
            if n == caractere_traduzido:
                lista_frequencia[n] += 1
    return lista_frequencia

def criacao_da_lista(lista: ListaNos):
    lista.inicio = None
    lista.tamanho = 0
    return lista
    
def inserir_ordenado(lista: ListaNos, no: No):
    auxiliar = No()
    if(lista.inicio == None):
        lista.inicio = no
    elif no.frequencia < lista.inicio.frequencia:
        no.proximo = lista.inicio
        lista.inicio = no
    else:
        auxiliar = lista.inicio
        while (auxiliar.proximo and auxiliar.proximo.frequencia <= no.frequencia):
            auxiliar = auxiliar.proximo
        no.proximo = auxiliar.proximo
        auxiliar.proximo = no
    lista.tamanho += 1
    return lista
            
def preencher_lista(lista_frequencia, lista: ListaNos):
    lista_criada = ListaNos()
    for indice in range(0, 256):
        novo_no = No()
        if(int(lista_frequencia[indice]) > 0):
            novo_no.chave = indice
            novo_no.frequencia = lista_frequencia[indice]
            novo_no.direita = None
            novo_no.esquerda = None
            novo_no.proximo = None
            lista_criada = inserir_ordenado(lista, novo_no)
    return lista_criada

def imprimir_lista(lista: ListaNos):
    no_auxiliar = lista.inicio
    print('\n\tLista ordenada: Tamanho: %d\n' % (lista.tamanho))
    while(no_auxiliar.proximo != None):
        print('\n\tCaractere: %c Frequência: %d\n' % (no_auxiliar.chave, no_auxiliar.frequencia))
        no_auxiliar = no_auxiliar.proximo

def imprimir_lista_frequencia(lista_frequencia):
    for n in range(0, 256):
        if(lista_frequencia[n] > 0):
            print("\t%d = %d = %c\n" % (n, lista_frequencia[n], n))
        # print("\t%d = %d = %c\n" % (n, lista_frequencia[n], n))
        
def remover_no_do_inicio_da_lista(lista: ListaNos):
    no_auxiliar = None
    
    if(lista.inicio != None):
        no_auxiliar = lista.inicio;
        lista.inicio = no_auxiliar.proximo
        no_auxiliar.proximo = None
        lista.tamanho -= 1

    return no_auxiliar

def montar_arvore(lista: ListaNos):
    primeiro = No()
    segundo = No()
    novo_no = No()
    
    while(lista.tamanho > 1):
        primeiro = remover_no_do_inicio_da_lista(lista)
        segundo = remover_no_do_inicio_da_lista(lista)
        novo_no = No()
        
        if(novo_no != None):
            novo_no.chave = "+"
            novo_no.frequencia = primeiro.frequencia + segundo.frequencia
            novo_no.esquerda = primeiro
            novo_no.direita = segundo
            novo_no.proximo = None
            lista = inserir_ordenado(lista, novo_no)
    return novo_no

def imprimir_arvore(raiz: No, tamanho: int):
    if (raiz.esquerda == None) and (raiz.direita == None):
        print("\tFolha: %c\tAltura: %d\n" % (raiz.chave, tamanho))
    else:
        imprimir_arvore(raiz.esquerda, tamanho + 1)
        imprimir_arvore(raiz.direita, tamanho + 1)
        
def altura_arvore(raiz):
    esquerda = 0
    direita = 0
    if(raiz == None):
        return -1
    else:
        esquerda = altura_arvore(raiz.esquerda) + 1
        direita = altura_arvore(raiz.direita) + 1
        
        if(esquerda > direita):
            return esquerda
        else:
            return direita
        
def aloca_dicionario(colunas):
    dicionario = [' ' * 6 for item in range(0, 255)]
    
    for indice in range(0, 255):
        dicionario[indice] = ''
    
    return dicionario

def gerar_dicionario(dicionario, raiz, caminho, colunas):
    esquerda = []
    direita = []
    if(raiz.esquerda == None and raiz.direita == None):
        dicionario[raiz.chave] = str(caminho)
    else:
        esquerda = str(caminho)
        direita = str(caminho)
        esquerda = esquerda + "0"
        direita = direita + "1"
        gerar_dicionario(dicionario, raiz.esquerda, esquerda, colunas)
        gerar_dicionario(dicionario, raiz.direita, direita, colunas)
        
def imprime_dicionario(dicionario):
    print("\n\tDicionário:\n")
    for indice in range(0, 255):
        if(len(dicionario[indice]) > 0):
            print("\t%3d: %s\n" % (indice, dicionario[indice]))
            
def calcula_tamanho_da_palavra(dicionario, texto):
    tamanho = 0
    for indice, valor in enumerate(texto):
        tamanho += len(dicionario[int(ord(valor))])
        indice += 1

    return tamanho + 1

def codificar(dicionario, texto):
    indice = 0
    tamanho = calcula_tamanho_da_palavra(dicionario, texto)
    codigo = [] 
    
    for indice, valor in enumerate(texto):
        codigo += dicionario[int(ord(valor))]
        indice += 1

    return codigo

def decodificar(texto, raiz: No):
    no_auxiliar = raiz
    variavel_temporaria = ['','']
    decodificado = [] 
    for indice, valor in enumerate(texto):
        if(valor == '0'):
            no_auxiliar = no_auxiliar.esquerda
        else:
            no_auxiliar = no_auxiliar.direita
        
        if(no_auxiliar.esquerda == None and no_auxiliar.direita == None):
            variavel_temporaria[0] = chr(no_auxiliar.chave)
            variavel_temporaria[1] = '\0'
            decodificado += variavel_temporaria
            no_auxiliar = raiz
        
        indice += 1
    return decodificado

if __name__ == '__main__':
    
    texto = "Vamos montar uma arvore de Huffman"
    lista = ListaNos()
    arvore = No()
    colunas = 0
    dicionario = ''
    codificado = ''
    decodificado = ''

    lista_frequencia = inicializa_lista_frequencia_com_zeros([])
    lista_frequencia = preenche_lista_frequencia(texto, lista_frequencia)
    imprimir_lista_frequencia(lista_frequencia=lista_frequencia)
    
    lista = criacao_da_lista(lista)
    lista = preencher_lista(lista_frequencia=lista_frequencia, lista=lista)
    imprimir_lista(lista)
    
    arvore = montar_arvore(lista)
    print("\n\tÁrvore de Huffman\n")
    imprimir_arvore(arvore, 0)
    
    colunas = altura_arvore(arvore) + 1
    dicionario = aloca_dicionario(colunas)
    gerar_dicionario(dicionario, arvore, "", colunas)
    imprime_dicionario(dicionario)
    
    codificado = codificar(dicionario, texto)
    print("\n\tTexto codificado: %s\n" % (codificado))
    print(*codificado)
    
    decodificado = decodificar(codificado, arvore)
    print("\n\tTexto decodificado: %s\n" % (decodificado))
    print(*decodificado)
    