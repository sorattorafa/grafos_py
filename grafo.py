class Vertice:
	def __init__(self, n):
		self.name = n 
		self.grau = 0 
	def __repr__(self): 
		return "{}".format(self.name)	 

class Grafo: 
	def __init__(self):
		self.vertices = {}
		self.arestas = []
		self.aresta_indices = {} 

	def add_vertice(self, vertice):
		if isinstance(vertice, Vertice) and vertice.name not in self.vertices:
			self.vertices[vertice.name] = vertice
			for row in self.arestas:
				row.append(0)
			self.arestas.append([0] * (len(self.arestas)+1))
			self.aresta_indices[vertice.name] = len(self.aresta_indices)
			return True
		else:
			return False
	
	def add_aresta(self, u, v, weight=1):
		if u in self.vertices and v in self.vertices:
			self.arestas[self.aresta_indices[u]][self.aresta_indices[v]] = weight
			self.arestas[self.aresta_indices[v]][self.aresta_indices[u]] = weight
			return True
		else:
			return False
			
	def print_grafo(self):
		for v, i in sorted(self.aresta_indices.items()):
			print(v + ' ', end='')
			for j in range(len(self.arestas)):
				print(self.arestas[i][j], end='')
			print(' ') 
			 
	def get_grau(self,vertice): 
		if vertice not in self.vertices: 
			return 
		cont = 0  
		aux = 0 
		for v in self.vertices:  
			cont += 1
			if v == vertice: 
				aux = cont  
		aux2 = aux  
		grau = 0 
		for v in range(len(self.vertices)):
			grau += self.arestas[aux-1][v]  	  
		print(grau)   

	def sao_adjacentes(self,vertice1,vertice2):  
		bool = 0
		for aresta in arestas:
			if(vertice1 == aresta[:1] and vertice2 == aresta[2:] ):
				bool = 1
		if(bool == 1): 
			print("Vertices adjacentes")
		else: 
			print("Vertices não adjacentes") 

	def getOrdem(self):
		print(len(self.vertices)) 

	def getVertices(self):  
		for x in self.vertices: 
			print(x)
		
	 
 
g = Grafo()
# print(str(len(g.vertices)))
#a = Vertice('A')
#g.add_vertice(a)
#g.add_vertice(Vertice('B'))
for i in range(ord('A'), ord('D')):
	g.add_vertice(Vertice(chr(i)))

arestas = ['C-C'] 

for aresta in arestas:
	g.add_aresta(aresta[:1], aresta[2:])

g.print_grafo() 
g.get_grau('C')   
g.sao_adjacentes('C','C')

#g.getOrdem() 
#g.getVertices()   
 