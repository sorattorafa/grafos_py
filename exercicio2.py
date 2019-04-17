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
g.add_vetor_arestas(arestas)  
#mostra o grafo
#g.print_grafo()   
# busca em profundidade	 
#for v in vetor_auxiliar: 
#	v.mudar_cor('Branco')		 
g.print_grafo()  

g.busca_em_profundidade()    
if(len(g.componentes_separados) > 1): 
	print('Sistema em Falha')  
if(len(g.componentes_separados) == 1): 
	print('Sistema em Conectado')  
	
