# Grafo ponderado - no dirigido

class Graph:
    def __init__(self):
        self.__structure = {}

    def __str__(self):
        return f'{self.__structure}'

    def add_node(self, node):
        """Función add_node: Agrega un nodo al grafo."""
        self.__structure[node] = {} 

    def add_edge(self, first_node, second_node, value):
        """Función add_node: Agrega una arista con un peso entre un par de nodos."""
        try:
            if not first_node in self.__structure:
                raise Exception(f'El nodo {first_node} no existe.')

            if not second_node in self.__structure:
                raise Exception(f'El nodo {second_node} no existe.')

            self.__structure[first_node][second_node] = value
            self.__structure[second_node][first_node] = value

        except Exception as e:
            print(e)

    def nodes(self):
        """Función nodes: Devuelve todos los nodos del grafo."""
        return list(self.__structure.keys())

    def neighbors(self, node):
        """Función neighbors: Devuelve todos los vecinos de un nodo."""
        return list(self.__structure[node].keys())

    def neighbor_value(self, first_node, second_node):
        """Función neighbors: Devuelve el peso o valor de una arista."""
        return self.__structure[first_node][second_node]

    def __dijkstra_algorithm(self, start_node):
        """Función dijkstra_algorithm: Ejecuta el algoritmo de dijkstra,
        a partir de un nodo inicial."""
        unvisited_nodes = list(self.nodes())
        shortest_path = { node: float('inf') for node in unvisited_nodes }
        previous_nodes = {}

        shortest_path[start_node] = 0

        while unvisited_nodes:
            min_node = None
            for node in unvisited_nodes:
                if min_node == None or \
                        shortest_path[node] < shortest_path[min_node]:
                            min_node = node

            neighbors = self.neighbors(min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[min_node] + self.neighbor_value(min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor], previous_nodes[neighbor] = tentative_value, min_node

            unvisited_nodes.remove(min_node)

        return previous_nodes, shortest_path

    def find_shortest_path(self, start_node, target_node):
        """Función find_shortest_path: Muestra el camino más corto
        haciendo uso del algoritmo de dijkstra."""
        previous_nodes, shortest_path = self.__dijkstra_algorithm(start_node)
        path = []
        node = target_node
        
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]
     
        # Add the start node manually
        path.append(start_node)
        
        print(f"La mejor ruta tiene el valor de: { shortest_path[target_node] } KM.")
        print(" -> ".join(reversed(path)))
