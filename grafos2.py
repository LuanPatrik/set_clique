class Grafo:
    #Inicializa a matriz de adjacencia referente ao Grafo não direcionado
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [] 
        for i in range(self.vertices):
            linha = [0] * self.vertices 
            self.grafo.append(linha)     

    #Adiciona uma aresta não direcionada entre os vértices u e v
    def adicionaAresta(self, u, v):
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1

    #Retorna a lista de adjacências do vértice
    def get_adj(self, v):
        adj = []
        for i in range(len(self.grafo[v - 1])):
            if self.grafo[v - 1][i] == 1:
                adj.append(i + 1)
        return adj

    #Exibe a Matriz de Adjacencia
    def exibeMatriz(self):
        for i in range(self.vertices):
            print(self.grafo[i])