from grafo import Vertice, Grafo	 
import numpy as np

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
#print(vertices)
for v in vertices: 
	x = Vertice(v)  
	## adiciona um vertice ao grafo
	g.add_vertice(x) 
	vetor_auxiliar.append(x) 

## adiciona vetores auxiliares com vertices e arestas no grafo	   
g.vetor_auxiliar = vetor_auxiliar 
g.arestasaux = arestas	  
# adiciona as arestas de fato
g.add_vetor_arestas(arestas)  

# em desenvolvimento, obrigado pela compreensão #	
## algoritmo de kosajaru
#g.busca_em_profundidade() 
#matriztransposta = np.transpose(g.arestas)  
#g.arestas = matriztransposta   
#g.busca_em_profundidade() 
#print(g.pilha_scc)  

#print(matriztransposta)
#for v, i in sorted(g.aresta_indices.items()):
#	for j in range(len(g.arestas)):  
#		if(g.arestas[i][j] != ''):
#			g.arestas[i][j] = matriztransposta[i][j] 			
#g.print_grafo()  

# # componentes fortemente conexos ##
#g.busca_em_profundidade()
#g.busca_em_profundidade()
#if(len(g.componentes_separados) > 1): 
#	print('Sistema em Falha pois existem dois componentes desconexos')  
#if(len(g.componentes_separados) == 1): 
#	print('Sistema em Conectado totalmente')  

#algoritmo de khan  
g.algoritimo_de_kahn() 
