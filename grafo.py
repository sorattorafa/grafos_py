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
		for aresta in self.arestas:
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
	def add_vetor_arestas(self,arestas): 
		for aresta in arestas:
			g.add_aresta(aresta[:1], aresta[2:])		
	 
	def add_vetor_vertices(self,str1,str2): 
		for i in range(ord(str1), ord(str2)):
			g.add_vertice(Vertice(chr(i)))  
			 
	def get_adjacentes(self,vertice): 
		adjacentes = []  
		for aresta in arestas:
			if(aresta[:1] == vertice): 
				adjacentes += aresta[2:]
			else:  
				if(aresta[2:] == vertice): 
					adjacentes += aresta[:1]	 
		print(adjacentes)			 
				
		
		
g = Grafo()
# print(str(len(g.vertices)))
#a = Vertice('A')
#g.add_vertice(a)
#g.add_vertice(Vertice('B'))  
#cria um vetor de vertices de A até D
g.add_vetor_vertices('A','F') 
#cria o vetor de arestas
# insere tais arestas no grafo 
arestas = ['A-A', 'A-B', 'A-C']
g.add_vetor_arestas(arestas)  
#mostra o grafo
g.print_grafo() 
# procura o grau de algum vertice no grafo 
g.get_grau('C')    
# verifica se dois vertices são adjacentes
#g.sao_adjacentes('C','C') 
# mostra uma lista de vertices adjacentes a este vertice
g.get_adjacentes('A')
#g.getOrdem() 
#g.getVertices()   
 
