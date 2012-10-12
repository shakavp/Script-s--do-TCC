'''
Created on 10/10/2012

@author: Geraldo
'''


from math import sqrt

TAMANHOS = ['100', '250', '500', '1000', '2000', '3000', '4000']
FITNESS = ['_pmx_']
ESCOLHA = ['ranking', 'wheel']

def faz_arq():
    for i in TAMANHOS:
        for j in FITNESS:
            for k in ESCOLHA:
                yield r"./benchmarks/" + k + j + i + ".out"
                
def media (lista):
    """teste
    >>> media([9,7,5,3,2])
    5.2
    """
    return float(sum(lista))/len(lista)

def variancia (media, lista):
    """teste
    >>> variancia(media([9,7,5,3,2]), [9,7,5,3,2])
    6.6
    """
    return float(sum([i**2 for i in [(media - item) for item in lista]]))/len(lista)

def desvio_padrao (var):
    """teste
    >>> desvio_padrao(variancia(media([9,7,5,3,2]), [9,7,5,3,2]))
    2.56124969497
    """
    return sqrt(var)

def nome_do_grafico(nome_do_arquivo):
    return nome_do_arquivo.split(".")[1].split(r"/")[2] + ".png"



def desenha_grafico (x, y, z, titulo, save_as):
    '''Desenha o grafico onde x, y e z sao tuplas da forma (valor_do_eixo, titulo_do_eixo)
    '''
    print "\nDesenho grafico", titulo, "com", x, y, z, "como eixos e salvando como", save_as

if __name__ == '__main__':
    tipo_selecao = ""
    tipo_cross = ""
    otimo_do_otimo = -1
    
    interacaoes = 0
    
    populacao_inicial = 0
    num_geracoes = 0
    elementos_fitness = 0
    
    lista_de_tempos = []
    lista_de_otimos = []
    
    flag = True #Flag para impressao apenas do primeiro caso de teste, para debug
    
    for arquivo in faz_arq():
        with open(arquivo) as entry:
            linhas = entry.readlines()
            cabecalho = linhas[:3]
            cabecalho = [m[:len(m)-1].split(' ') for m in cabecalho]
            tipo_selecao = cabecalho[0][0]
            tipo_cross = cabecalho[0][1]
            otimo_do_otimo = int(round(float(cabecalho[0][2])))
            interacoes = int(cabecalho[1][0])
            populacao_inicial = int(cabecalho[2][0])
            num_geracoes = int(cabecalho[2][1])
            elementos_fitness = int(cabecalho[2][2])
            teste = linhas[3:]
            teste = [int(round(float(m[:len(m)-1]))) for m in teste]
            for l in range(len(teste)):
                if l % 2 == 0:
                    lista_de_tempos.append(teste[l])
                else:
                    lista_de_otimos.append(teste[l])
                    
            if flag:
                print "Selecao:", tipo_selecao
                print "Crossover", tipo_cross
                print "OtimoReal", otimo_do_otimo
    
                print "instancias:", interacoes
    
                print "TamanhoDaPopInicial:", populacao_inicial
                print "numeroDeGeracoes:", num_geracoes
                print "qdeElementosParaFitness:", elementos_fitness 
                
                print "tempoDeExecucaoEmMilissegundos (lista):", lista_de_tempos
                print "OtimoEncontrado (lista):", lista_de_otimos
                
                #Exemplo de chamada
                desenha_grafico(([], "x"), ([], "y"), ([], "z"), "teste", nome_do_grafico(arquivo))
                
                flag = False    