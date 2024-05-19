

def conta_letras(frase: str):
    resultado = []
    flag = 0
    for letra in frase:
        for indice, item in enumerate(resultado):
            if resultado[indice].get('chave') == letra:
                flag = resultado[indice].get('valor') + 1
                resultado[indice] = {'chave':letra,'valor':flag}
        if(flag == 0):        
            resultado.append({'chave':letra,'valor':1})          
        flag = 0
    return resultado


def ordenar_prioridade(resultado):
    for indice, item in enumerate(resultado):      
        for indice, item in enumerate(resultado):
            if len(resultado) > indice+1:
                aux = resultado[indice+1]
                atual = resultado[indice] 
                if atual.get('valor') > aux.get('valor'):
                    resultado[indice+1] = resultado[indice]
                    resultado[indice] = aux 
    return resultado

class No:
    def __init__(self, chave: str, esquerda, direita):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
    
# def montar_arvore_huf(resultado_ordenado):    
#     for indice, elemento in enumerate(resultado_ordenado):
#         if(indice == 0):
#             no = No(chave='+', esquerda=resultado_ordenado[indice], direita=resultado_ordenado[indice+1])
#         if len(resultado_ordenado) > indice+1:
#             no = No(chave='+', esquerda=resultado_ordenado[indice], direita=resultado_ordenado[indice+1])
#             resultado_ordenado.pop()
#             resultado_ordenado.pop()
#     print(f'resultado {resultado_ordenado}')
#     return no



if __name__ == "__main__":
    frase = "Vamos aprender Python"
    print(conta_letras(frase = frase))
    print(ordenar_prioridade(conta_letras(frase = frase)))
    # print(montar_arvore_huf(ordenar_prioridade(conta_letras(frase = frase))))