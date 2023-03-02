from graph import Graph

def all_capitalize(text):
    """Función all_capitalize: Capitaliza todas y cada una de 
    las palabras de una cadena"""
    return ' '.join([x.capitalize() for x in text.split(' ')])

# Nodos del grafo (Aeropuertos)
nodes = ['Bogotá', 'Bucaramanga', 'Medellín',
         'Cali', 'Cúcuta', 'Villavicencio',
         'Florencia', 'Cartagena', 'Riohacha',
         'Santa Marta', 'Barranquilla', 'Yopal',
         'Manizales', 'Sincelejo', 'Tunja',
         'Quibdó', 'Montería', 'Popayán',
         'Pasto', 'Valledupar']

# Aristas del grafo (Relaciones de un Aeropuerto a otro)
edges = [('Bogotá', 'Bucaramanga', 291.81),
         ('Bogotá', 'Medellín', 242.07),
         ('Bogotá', 'Cali', 305.07),
         ('Bogotá', 'Cartagena', 656.73),
         ('Bogotá', 'Barranquilla', 704.58),
         ('Bogotá', 'Cúcuta', 397.37),
         ('Bucaramanga', 'Medellín', 286.83),
         ('Bucaramanga', 'Cartagena', 339.22),
         ('Bucaramanga', 'Santa Marta', 473.24),
         ('Bucaramanga', 'Tunja', 178.92),
         ('Bucaramanga', 'Yopal', 214.28),
         ('Medellín', 'Manizales', 131.64),
         ('Medellín', 'Quibdó', 136.12),
         ('Medellín', 'Montería', 280.71),
         ('Medellín', 'Cartagena', 461.26),
         ('Medellín', 'Cali', 330.67),
         ('Cali', 'Popayán', 111.07),
         ('Cali', 'Pasto', 261.07),
         ('Cúcuta', 'Valledupar', 296.82),
         ('Cúcuta', 'Yopal', 284.86),
         ('Villavicencio', 'Yopal', 284.86),
         ('Villavicencio', 'Florencia', 356.82),
         ('Villavicencio', 'Quibdó', 377.52),
         ('Villavicencio', 'Popayán', 381.84),
         ('Florencia', 'Pasto', 191.44),
         ('Florencia', 'Popayán', 144.61),
         ('Cartagena', 'Riohacha', 311.80),
         ('Cartagena', 'Montería', 187.29),
         ('Riohacha', 'Santa Marta', 145.75),
         ('Riohacha', 'Valledupar', 126.06),
         ('Santa Marta', 'Valledupar', 135.68),
         ('Santa Marta', 'Barranquilla', 69.59),
         ('Barranquilla', 'Sincelejo', 196.93),
         ('Yopal', 'Tunja', 109.81),
         ('Manizales', 'Villavicencio', 233.53),
         ('Manizales', 'Quibdó', 133.09),
         ('Sincelejo', 'Montería', 81.31)]

# Instancia del Grafo
GRAPH = Graph()

# Se agregan todos y cada uno de los nodos de la lista nodes.
for node in nodes:
    GRAPH.add_node(node)


# Se agregan todas y cada una de las arista de la lista edges.
for edge in edges:
    first_node, second_node, distance = edge
    GRAPH.add_edge(first_node, second_node, distance)

source_node = all_capitalize(input('Digite su origen: '))
destination_node = all_capitalize(input('Digite su destino: '))

GRAPH.find_shortest_path(source_node, destination_node)
