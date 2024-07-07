import sys
import time
from grafos2 import Grafo

#Encontra a cobertura mínima de cliques no grafo dentro do limite definido
def encontrar_cobertura_min(grafo, tempo_limite):
    tempo_inicio = time.time()
    
    #Inicia a variavel com a pior caso, todos os vertices estao em apenas um clique
    melhor_cobertura = [list(range(1, grafo.vertices + 1))]  
    
    encontrar_cliques([], list(range(1, grafo.vertices + 1)), grafo, melhor_cobertura, tempo_inicio, tempo_limite)
    
    #Retorna a melhor cobertura encontrada
    return melhor_cobertura[0]

#Busca por coberturas de cliques
def encontrar_cliques(cobertura_atual, vert_restantes, grafo, melhor_cobertura, tempo_inicio, tempo_limite):
    if time.time() - tempo_inicio > tempo_limite:
        return

    #Se não restarem mais vertices
    if not vert_restantes:
        #compara o tamanho da cobertura atual com o tamanho da melhor cobertura encontrada
        if len(cobertura_atual) < len(melhor_cobertura[0]):
            melhor_cobertura[0] = cobertura_atual[:]
        return

    #Inicia a variavel clique com o primeiro vértice dos vértices restantes.
    v = vert_restantes[0]
    clique = [v]
    
    #Percorreer os vértices restantes
    for u in vert_restantes[1:]:
        vert_adj = True
        for w in clique:
            #Verifica se cada vertice é adjacente a todos os vértices atuais no clique
            if grafo.grafo[u-1][w-1] != 1:
                vert_adj = False
                break
        if vert_adj:
            clique.append(u)

    #Percorre e atualizar a lista de vértices restantes removendo os que já estão no clique.
    novos_vert_restantes = []
    for u in vert_restantes:
        if u not in clique:
            novos_vert_restantes.append(u)

    encontrar_cliques(cobertura_atual + [clique], novos_vert_restantes, grafo, melhor_cobertura, tempo_inicio, tempo_limite)


def main():
    global tempo_inicio, tempo_exe

    caminho = sys.argv[1]
    tempo_exe = int(sys.argv[2])

    arquivo = open(caminho, 'r')

    cont = 0
    for i in arquivo:
        cont += 1
        if i[0] == 'c':
            pass
        elif i[0] == 'p':
            qtd_vertice = int(i.split(" ")[2])
            grafo = Grafo(qtd_vertice)
        elif i[0] == 'e':
            v1 = int(i.split(" ")[1])
            v2 = int(i.split(" ")[2])
            grafo.adicionaAresta(v1, v2)
        elif cont == 1:
            qtd_vertice = int(i.split(" ")[0])
            grafo= Grafo(qtd_vertice)
        else:
            v1 = int(i.split(" ")[0])
            v2 = int(i.split(" ")[1])
            grafo.adicionaAresta(v1, v2)

    arquivo.close()
    tempo_inicio = time.time()

    melhor_cobertura  = encontrar_cobertura_min(grafo, tempo_exe)
    print(len(melhor_cobertura))
    for clique in melhor_cobertura:
        print(" ".join(map(str, clique)))

if __name__ == '__main__':
    main()