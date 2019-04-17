from grafo import Vertice, Grafo		
# main   
vertices = []
try:
   f = open("entrada.txt")
   copia = f.read() 
finally:
   f.close()  

for c in copia: 
	if(c != '-' and  c != ' ' and c != '\n' and c != '\t'): 
		if(c not in vertices): 
			vertices.append(c)    			 
arestas = [] 
for i in range(len(copia)):  
	if(copia[i] == '-'): 
		arestas.append(copia[i-1]+copia[i]+copia[i+1])  

vertices = sorted(vertices) 
vetor_auxiliar = [] 
g = Grafo() 
print(vertices)
for v in vertices: 
	x = Vertice(v) 
	g.add_vertice(x) 
	vetor_auxiliar.append(x) 

## adiciona vetores com vertices e arestas no grafo	   
g.vetor_auxiliar = vetor_auxiliar 
g.arestasaux = arestas	 

# print(str(len(g.vertices)))
#u = Vertice('U')
#g.add_vertice(u) 
#v = Vertice('V')
#g.add_vertice(v) 
#w = Vertice('W')
#g.add_vertice(w) 
#x = Vertice('X')
#g.add_vertice(x) 
#y = Vertice('Y')
#g.add_vertice(y) 
#z = Vertice('Z')
#g.add_vertice(z)   

#vetor_auxiliar.append(u)
#vetor_auxiliar.append(v) 
#vetor_auxiliar.append(w) 
#vetor_auxiliar.append(x) 
#vetor_auxiliar.append(y) 
#vetor_auxiliar.append(z)
#g.add_vertice(Vertice('B'))  
#cria um vetor de vertices de A té D
#g.add_vetor_vertices('A','C')  

#cria o vetor de arestas
# insere tais arestas no grafo 
#arestas = ['1-2','2-1']  
g.add_vetor_arestas(arestas)  
#mostra o grafo
#g.print_grafo()   
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
#g.busca_em_largura('1')	  

# busca em profundidade	 
#for v in vetor_auxiliar: 
#	v.mudar_cor('Branco')		 
g.print_grafo()  

g.busca_em_profundidade()      
