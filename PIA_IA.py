import random
import time

class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
    #
    def get_neighbors(self, v):
        return self.adjac_lis[v]

    # Esta es una funcion que tiene valores iguales para todos los nodos
    def h(self, n):
        H = {
            1: 1,
            2: 1,
            3: 1,
        }
        for i in range (3,1000): #Aqui creamos un valor heuristico para cada nodo
            H[i]=1
        return H[n]
    #
    def a_star_algorithm(self, start, stop):
        open_lst = set([start])
        closed_lst = set([])
        g = {}
        g[start] = 0
        par = {}
        par[start] = start

        while len(open_lst) > 0:
            n = None
            for v in open_lst:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v
            if n == None:
                print('Path does not exist!')
                return None
            if n == stop:
                reconst_path = []
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
                reconst_path.append(start)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path
            for (m, weight) in self.get_neighbors(n):
              
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        g[m] = n
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
            open_lst.remove(n)
            closed_lst.add(n)
        print('Path does not exist!')
        return None
#Inicializamos una cola
visited = [] # Lista de nodos visitados.
queue = [] 

def bfs(visited, graph, node): 
    visited.append(node)
    queue.append(node)

    while queue: # Creando bucle para visitar cada nodo
        m = queue.pop(0) 
        print (m, end = " ")
        for neighbour in graph[m]:
            if neighbour == 932: #Este numero representa el numero que estamos buscando, aqui se detiene la busqueda
                    break
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour) 
adjac_lis = {
    1: [(2, random.randint(5,30)), (3, random.randint(5,30))],
    2: [(3, random.randint(5,30)),(4, random.randint(5,30))]
}

for i in range (3,1000): 
    inicio = i
    v1 = i+1
    v2 = i+2
    adjac_lis[inicio]=[(v1,random.randint(5,30)), (v2, random.randint(5,30))]
print (adjac_lis)
graph1 = Graph(adjac_lis)
seconds = time.time()
graph1.a_star_algorithm(1, 986) #El primer parametro es el nodo inicial y el segundo es el nodo que se busca
end = time.time()
print(end-seconds)

adjac_lis2 = {
    1: [2, 3],
    2: [3, 4],
    999: [1000],
    1000: []        #Hay que limitarlo desde la lista porque si no, durante el recorrido va a marcar que es el fin pero 
}                   #Aun tiene nodos vecinos por lo tanto sería una incongruencia

for i in range (3,999):
    inicio = i
    v1 = i+1
    v2 = i+2
    adjac_lis2[inicio]=[v1, v2]
seconds = time.time()
bfs(visited, adjac_lis2, 1) 
end = time.time()
print(end-seconds)

