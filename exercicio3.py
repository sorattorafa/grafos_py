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

#algoritmo de khan  
g.algoritimo_de_kahn() 
