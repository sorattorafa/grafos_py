class Vertice:
	def __init__(self, n):
		self.name = n 
		self.grau = 0  
		self.grau_entrada = 0  
		self.grau_saida = 0 
		self.tempo_entrada = 0 
		self.tempo_saida = 0 
		self.cor = 'Branco' 
		self.predecessor = None 
		self.d_inicial = 0
	def __repr__(self): 
		return "{}".format(self.name) 
	def get_cor(self): 
		print('A cor do vertice:['+self.name+'] é '+self.cor)	 
	def mudar_cor(self,cor):
		self.cor = cor		 

class Grafo: 
	def __init__(self):
		self.vertices = {}
		self.arestas = []
		self.aresta_indices = {}  
		self.time = 0

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
			# A-B == B-A
			#self.arestas[self.aresta_indices[v]][self.aresta_indices[u]] = weight
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
		return len(self.vertices) 

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
		if (vertice not in self.vertices): 
			print('Vertice nao existe no grafo') 
			return 
		adjacentes = []   
		for aresta in arestas:  
			if(aresta[:1] == vertice): 
				adjacentes += aresta[2:] 
		return adjacentes		  

	def get_indiretos(self,vertice): 
		if (vertice not in self.vertices): 
			print('Vertice nao existe no grafo') 
			return 
		adjacentes = []   
		for aresta in arestas:  
			if(aresta[2:] == vertice): 
				adjacentes += aresta[:1] 
		return adjacentes		  

	def get_grau_saida(self,vertice): 
		if (vertice not in self.vertices): 
			print('Vertice nao existe no grafo') 
			return  
		grau_saida = 0 
		for aresta in arestas: 
			if(aresta[:1] == vertice): 
				grau_saida +=1		   
		return grau_saida  

	def get_grau_entrada(self,vertice): 
		if (vertice not in self.vertices): 
			print('Vertice nao existe no grafo') 
			return  
		grau_entrada = 0 
		for aresta in arestas: 
			if(aresta[2:] == vertice): 
				grau_entrada +=1		  
		return grau_entrada  

	def is_completo(self):  
		expoent = len(self.aresta_indices.items()) 
		expoent = expoent * expoent 
		auxiliarzao = 0   
		for v, i in sorted(self.aresta_indices.items()): 
			for j in range(len(self.arestas)):  
				if(self.arestas[i][j] == 1):  
					auxiliarzao += 1  
		if (auxiliarzao == expoent): 
			print('O grafo é completo') 
		else: 
			print('Não é completo')				

	def is_conexo(self):  
		is_conexo = 0
		auxizin = 0  
		for v in self.vertices: 
			if(self.get_grau_saida(v) == 0 and self.get_grau_entrada(v) == 0): 
				auxizin = 1 
			if(self.get_grau_saida(v) == 1 and self.get_grau_entrada(v) == 1): 
				if(v in self.get_adjacentes(v)): 
					auxizin = 1
		 
		if(auxizin == 1): 
			is_conexo = 0 
			return is_conexo
		else:  
			is_conexo = 1 
			return is_conexo
			 
	def is_arvore(self): 
		if(self.is_conexo() == 1): 
			if(len(self.vertices)-1 == len(arestas)): 
				print('É arvore')   
			else: 
				print('Não é árvore')	
				
	def ftd_vertice(self,vertice): 
		adja = []     
		ftd = []
		for v, i in sorted(self.aresta_indices.items()):
			if(vertice == v ):  
				for j in range(len(self.arestas)):  
					if(self.arestas[i][j] == 1):  
						adja.append(j)	  
		for i in adja:   
			for j in range(len(self.arestas)): 
				if(self.arestas[i][j] == 1): 
					if(j not in adja): 
						adja.append(j)		 

		auxiliante = 0		  				 
		for v in self.vertices:   
			if(auxiliante in adja): 
				ftd += v	   
			auxiliante += 1 
		print('O FTD do vertice ['+vertice+'] é :') 
		print(ftd) 
		# LISTA OS INDICES J DE TODOS ADJACENTES AO VERTICE PROCURADO				 	  
		# print(adja) 
		#   
	
	def fti_vertice(self,vertice): 
		adja = []     
		fti = []
		for v, i in sorted(self.aresta_indices.items()):
			if(vertice == v ):  
				for j in range(len(self.arestas)):  
					if(self.arestas[j][i] == 1):  
						adja.append(j)	 
		for i in adja:   
			for j in range(len(self.arestas)): 
				if(self.arestas[j][i] == 1): 
					if(j not in adja): 
						adja.append(j)	
		auxiliante = 0		  				 
		for v in self.vertices:   
			if(auxiliante in adja): 
				fti += v		
			auxiliante += 1 
		print('O FTI do vertice ['+vertice+'] é :') 
		print(fti)   

	## funcao recursiva para a busca em profundidade	  
	 
	def dfs_visit(self,vertice):  
		self.time += 1   
		vertice.tempo_entrada = self.time 
		vertice.mudar_cor('Cinza') 
		advert = self.get_adjacentes(vertice.name) 
		listaadjacentes = [] 
		for auxiliar in vetor_auxiliar: 
			if(auxiliar.name in advert):  
				listaadjacentes.append(auxiliar) 
		for auxiliar in listaadjacentes: 
			if(auxiliar.cor == 'Branco'): 
				auxiliar.predecessor = vertice 
				self.dfs_visit(auxiliar)  
		vertice.mudar_cor('Preto')					   
		self.time += 1
		vertice.tempo_saida = self.time

## busca em profundidade 
	def busca_em_profundidade(self): 
		for v in vetor_auxiliar:  
			v.mudar_cor('Branco') 
		self.time = 0	  
		for v in vetor_auxiliar: 
			if(v.cor == 'Branco'):  
				self.dfs_visit(v)
## busca em largura  
	def busca_em_largura(self,vertice): 
		vertice.mudar_cor('Cinza') 
		sequencia = []     
		q = []
		sequencia.append(vertice) 
		q.append(vertice)
		while len(q) > 0:
			desempilhado = q[0]		 
			q.pop(0)  
			adj2 = self.get_adjacentes(desempilhado.name) 
			for a in vetor_auxiliar: 
				if(a.name in adj2): 
					if(a.cor == 'Branco'): 
						a.mudar_cor('Cinza') 
						q.append(a) 
						sequencia.append(a) 
			desempilhado.mudar_cor('Preto')			
#		while len(sequencia) != len(vetor_auxiliar): 

			
# main  

g = Grafo()
# print(str(len(g.vertices)))
u = Vertice('U')
g.add_vertice(u) 
v = Vertice('V')
g.add_vertice(v) 
w = Vertice('W')
g.add_vertice(w) 
x = Vertice('X')
g.add_vertice(x) 
y = Vertice('Y')
g.add_vertice(y) 
z = Vertice('Z')
g.add_vertice(z)   

vetor_auxiliar = [] 
vetor_auxiliar.append(u)
vetor_auxiliar.append(v) 
vetor_auxiliar.append(w) 
vetor_auxiliar.append(x) 
vetor_auxiliar.append(y) 
vetor_auxiliar.append(z)
#g.add_vertice(Vertice('B'))  
#cria um vetor de vertices de A té D
#g.add_vetor_vertices('A','C')  

#cria o vetor de arestas
# insere tais arestas no grafo 
arestas = ['U-V','U-X', 'X-V', 'Y-X', 'W-Y', 'W-Z', 'Z-Z','V-Y']
g.add_vetor_arestas(arestas)  
#mostra o grafo
g.print_grafo()   
# procura o grau de algum vertice no grafo 
#g.get_grau('C')    
# verifica se dois vertices são adjacentes
#g.sao_adjacentes('C','C') 
# mostra uma lista de vertices adjacentes a este vertice
#g.get_adjacentes('A')   
# todos vertices se ligam com todos 
#g.is_completo() 
#conexo = g.is_conexo()   

#if(conexo == 1): 
#	print('É conexo') 
#g.is_arvore()    

# fecho transitivo direto de um vértice do grafo 
## = conjunto de vertices que se chega a partir 
## deste vertice, lembrando que o grafo é digrafo 
#g.ftd_vertice('B') 
 
# fecho transitivo indireto de um vértice do grafo 
## é o conjunto de vertices que chegam nesse grafo 
## por algum caminho existente  
#g.fti_vertice('B')
#g.get_grau_entrada('A')
#g.get_grau_saida('A')
#g.get_grau_entrada('A')  

#g.getOrdem() 
#g.getVertices()   
  
 
# busca em largura 
g.busca_em_largura(w)		 
g.busca_em_profundidade()
