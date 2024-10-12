# TEORIA
#
# Um grafo é uma estrutura composta por pontos (vertices)
# e ligações entre pontos (arestas)
#
# Por exemplo, podemos ter uma rede social. Os vértices
# seriam pessoas, e as arestas seriam amizades entre pessoas
# 
# Ou poderiamos ter uma rede de computadores. No caso, os vértices seriam computadores, as arestas,
#  os cabos de rede
# 
# Ou poderiamos ter um mapa. Os vértices seriam cidades, as arestas, estradas ligando essas cidades.
#
# Exemplo:
#
# 0 - 2
# |   
# 1 - 3
#
# Esse grafo tem 4 vertices (0, 1, 2 e 3) e 3 arestas
# (uma ligação entre 0 e 1, que denotarei (0,1),
# uma entre 0 e 2 -- (0,2) e (1,3)
#
# Uma forma de representar grafos, que usaremos nesse arquivo
# é usando matrizes
#
# Para representar esse grafo, podemos usar a seguinte matriz
#
# [[0,1,1,0],
#  [1,0,0,1],
#  [1,0,0,0],
#  [0,1,0,0]]
#
# Estamos usando 1 para representar a existencia de uma aresta, e 
# 0 para representar a inexistência.
#
# Por exemplo, se olharmos para a linha 0 e coluna 1 
# [[0,X,1,0],
#  [Y,0,0,1],
#  [1,0,0,0],
#  [0,1,0,0]]
# (marcada com um X na matriz) vemos que há uma aresta entre 0 e 1
# a linha 1 coluna 0 (marcada com Y na matriz) diz o mesmo
#
# Se olharmos para a linha 2 coluna 3 (marcada com X)
# [[0,1,1,0],
#  [1,0,0,1],
#  [1,0,0,X],
#  [0,1,Y,0]]
# vemos que não há aresta entre 2 e 3
# (a linha 3 coluna 2, marcada com Y, diz o mesmo)
#
# Perceba que estamos contando do zero sempre
# [[0,1,1,0],
#  [X,X,X,X],  -> linha 1 
#  [1,0,0,1],
#  [0,1,0,0]]
#
#
# [[0,1,X,0],
#  [1,0,X,0],
#  [1,0,X,1],
#  [0,1,X,0]]
#       |
#       --> coluna 2


# Vamos começar exercitando a leitura de um grafo nesse formato de matrizes
# 
# A pergunta que você vai ter que responder é:
# se estão ligados
# 0 e 1, 0 e 2, 0 e 3, 1 e 2, 1 e 3, 3 e 2
# 
# Considerando o grafo
# [[0,0,0,0],
#  [0,0,0,0],
#  [0,0,0,1],
#  [0,0,1,0]]
#
# Podemos fazer o seguinte esboço
#
#  0   1     
#
#  2 - 3
#  
# a resposta seria que os vertices 0 e 1 não estão ligados,
# como podemos ver tanto na posicao X quanto na posicao Y
# [[0,X,0,0],
#  [Y,0,0,0],
#  [0,0,0,1],
#  [0,0,1,0]]
# Eu queria responder todos esses:
# 0 e 1, 0 e 2, 0 e 3, 1 e 2, 1 e 3, 3 e 2
# Então a lista ficaria:
# exemplo = [False,False,False,False,False,True]

# Considerando o grafo
# [[0,1,0,0],
#  [1,0,1,1],
#  [0,1,0,1],
#  [0,1,1,0]]
#
# faça um esboço do grafo, depois
# diga, na lista arestas_1, se estão ligados
# 0 e 1, 0 e 2, 0 e 3, 1 e 2, 1 e 3, 3 e 2
#
# crie uma lista como no exemplo acima
arestas_1 = [True, False, False, True, True, True]

# Considerando o grafo
# [[0,1,1,1],
#  [1,0,0,1],
#  [1,0,0,0],
#  [1,1,0,0]]
#
# diga, na lista arestas_2, se estão ligados
# 0 e 1, 0 e 2, 0 e 3, 1 e 2, 1 e 3, 3 e 2
#
# crie uma lista como no exemplo
arestas_2 = [True, True, True, False, True, False]

# Considerando o grafo
# [[0,0,0,1],
#  [0,0,1,0],
#  [0,1,0,0],
#  [1,0,0,0]]
#
# diga, na lista arestas_3, se estão ligados
# 0 e 1, 0 e 2, 0 e 3, 1 e 2, 1 e 3, 3 e 2
#
# crie uma lista como no exemplo:
arestas_3 = [False, False, True, True, False, False]

# Alias, qual o máximo de arestas que um grafo com
# 2 vértices pode ter? e com 3? e com 4? e com 5? e com 6?
#
# coloque suas respostas em uma lista max_arestas como no exemplo max_arestas = [0,0,-1,3,4] (mas preenchendo
# os números corretos)
max_arestas = [1, 3, 6, 10, ]

# para lembrar como manipular matrizes no python, temos o seguinte link:
# https://pythontutor.com/render.html#code=m%20%3D%20%5B%5B'a','b','c','d'%5D,%0A%20%20%20%20%20%5B'e','f','g','h'%5D,%0A%20%20%20%20%20%5B'i','j','k','l'%5D,%0A%20%20%20%20%20%5B'm','n','o','p'%5D%5D%0A%20%20%20%20%20%20%20%20%20%20%0Adef%20valor_posicao%28matriz,%20linha,%20coluna%29%3A%0A%20%20%20%20print%20%28matriz%5Blinha%5D%29%0A%20%20%20%20print%20%28matriz%5Blinha%5D%5Bcoluna%5D%29%0A%20%20%20%20return%20matriz%5Blinha%5D%5Bcoluna%5D%0A%20%20%20%20%0Avalor_posicao%28m,0,0%29%0Avalor_posicao%28m,2,3%29%0Avalor_posicao%28m,3,2%29&cumulative=false&curInstr=6&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

# Escreva uma funcao que recebe um grafo,
# representado por uma matriz e dois vertices,
# v1 e v2, e devolve True se existe aresta entre eles.

def existe_aresta(arestas, v1, v2):
    return arestas [v1][v2] == 1



# Escreva uma funcao que recebe um grafo,
# representado por uma matriz,  e dois vertices,
# v1 e v2, e altera o grafo para que haja arestas entre os vertices

def adiciona_aresta(arestas, v1, v2):
     arestas[v1][v2] = 1
     arestas[v2][v1] = 1

# faca o mesmo, agora para remover arestas, em uma funcao remove_aresta
def remove_aresta(arestas, v1, v2):
    arestas[v1][v2] = 0
    arestas[v2][v1] = 0



# faca uma funcao conta_arestas, que conta o numero de arestas
# de um grafo.
def conta_arestasOLD(arestas):
    soma = 0 
    for linha in arestas:
        soma+= sum(linha)
    return soma

def conta_arestas(arestas):
    nro_vertices = len(arestas) #len(arestas[0])
    soma = 0
    for i in range(0, nro_vertices):
        for j in range(0, nro_vertices):
            soma += arestas[1][j]
    return soma


# direi que um grafo eh uma "estrela", ou ainda um "asterisco"
# se todos existe um vertice "central", conectado a todos os
# demais, e todo vertice nao central so tem uma aresta: aquela
# que vai para o central.
#
# ex:
#        2
#        |
#    0 - 3 - 1
#        |
#        4
# Esse grafo eh uma estrela com vertice central 3
#
# Crie uma funcao eh_estrela, que recebe o grafo e devolve True ou False
def eh_estrela(arestas):
    pass




# Crie uma função que recebe a matriz que representa
# um grafo e o numero de um
# vertice V específico. 
# Ela retorna uma lista com todos os vertices vizinhos de 
# V

# Cuidado para não repetir vertices, e pra não colocar o proprio V na lista

def vizinhos(arestas, V):
    pass

# Crie uma função que recebe a matriz que representa
# um grafo e o numero de um
# vertice V específico. 
# Retorna uma lista com todos os números dos vizinhos
# de V, mas também os vizinhos de vizinhos. 
#
# Nao coloque vizinho de vizinho de vizinho
#
# Cuidado para não repetir vertices, e pra não colocar o proprio V na lista

def mais_vizinhos(arestas, V):
    pass

# Para podermos continuar nosso estudo de grafos, vamos ter que fazer um pequeno desvio e 
# definir uma estrutura de dados chamada fila

# Uma fila é uma estrutura de dados dinâmica que admite remoção de elementos 
# e inserção de novos objetos.  Mais especificamente, uma  fila  (= queue)  
# é uma estrutura sujeita à seguinte regra de operação:  
# cada remoção remove o elemento mais antigo da fila, 
# isto é, o elemento que está na estrutura há mais tempo.

# Em outras palavras, o primeiro objeto inserido na fila é também o primeiro a ser removido.
# Essa política é conhecida pela sigla FIFO (= First-In-First-Out).

# Podemos implementar uma fila no python usando uma lista e um indice:
# Ao adicionar um elemento, fazemos um append
# Ao remover um elemento, pegamos o valor atualmente apontado pelo indice, e aumentamos o indice
# em 1

# Por exemplo, se tivermos a seguinte fila:

fila = {'proximo':2, 'lista':[20,30,40,50,60]}

# estamos definindo que o 20 e o 30 'já sairam' da fila. Se eu pedir um elemento,
# usando proximo(fila), receberei o 40 como retorno, e a fila passará a ser

fila = {'proximo':3, 'lista':[20,30,40,50,60]}

# isto é, o próximo é o 50. Os elementos 20,30,40 ainda estão na lista só
# pra gente não ter que pagar o custo caro (O(n)) da remoção, mas já
# sairam da fila

# para eu inserir um elemento (por exemplo 12) na fila, vou chamar a funcao
# insere(fila,12)
# e o novo estado da fila será

fila = {'proximo':3, 'lista':[20,30,40,50,60,12]}

# cria_fila_nova, que cria uma fila sem nenhum elemento, ja vou te
# dar de graça

def cria_fila_nova():
   return {'posicao': 0, 'lista': []} #essa ja veio de graça

# vamos agora criar essas duas funções: insere e proximo


def insere_na_fila(fila, elemento):
   pass

def remove_da_fila(fila):
   pass

# façamos mais uma função
# verifica fila_vazia, que verifica se a fila está vazia (ou porque
# ninguém entrou, ou porque todos os elementos que entraram também depois sairam)

def verifica_fila_vazia(fila):
   pass

# agora faca uma funcao alcancaveis, que inclui V, seus vizinhos imediatos,
# seus vizinhos "de segundo grau", "de terceiro grau" e assim ate o fim do grafo
# a assinatura da função será
# def alcancaveis(arestas, V):
# V é o vértice inicial
# O conjunto que contém V, e todos os vértices alcançaveis a partir dele é chamado
# uma 'componente conexa'

# Como fazer isso?
# a idéia é manter uma fila de vizinhos, que no inicio vai ter só V
# toda vez que um vizinho novo é descoberto, ele entra na fila
# vamos 'eliminando' elementos da fila, e colocando todos os vizinhos *deles*
# na fila. 

# Tome cuidado para não ter loops infinitos: se a aresta 0-3 existir,
# e o 0 'colocar' o 3 'pra dentro', é importante o 3 não colocar o 0 'pra dentro'
# de novo!

def alcancaveis(arestas, V):
   pass

# para passar os ultimos testes, reforme a sua funcao alcancaveis
# em vez de retornar uma lista de alcancaveis, ela vai retornar agora um
# dicionario.
# Esse dicionario vai dizer a distância de cada vértice para o V

gr1 = [[0,1,0,0,0,1],      #     1 - 2
       [1,0,1,0,0,0],      #    /    | 
       [0,1,0,1,0,0],      #   0     3 
       [0,0,1,0,1,0],      #    \    |
       [0,0,0,1,0,1],      #     5 - 4
       [1,0,0,0,1,0]]

# Considerando esse grafo dado, se V for 0, 
# d[0] = 0
# d[1] = 1
# d[5] = 1
# d[2] = 2
# d[4] = 2
# d[3] = 3



# A partir daqui, soh codigo de testes/utilitario
# Nada para voce fazer

gr1 = [[0,1,0,0,0,1],      #     1 - 2
       [1,0,1,0,0,0],      #    /    | 
       [0,1,0,1,0,0],      #   0     3 
       [0,0,1,0,1,0],      #    \    |
       [0,0,0,1,0,1],      #     5 - 4
       [1,0,0,0,1,0]]

gr2 = [[0,1,0,0,0,1],       # ----------------
       [1,0,0,0,0,1],       # |    1    2    |
       [0,0,0,1,1,0],       # |   /|    |\   |
       [0,0,1,0,1,0],       # |  0 |    3 |  |
       [0,0,1,1,0,0],       # |   \|    |/   |
       [1,1,0,0,0,0]];      # |    5    4    |
                            # ----------------

gr3 = [[0,1,0,1,0,1],       # ----------------
       [1,0,0,0,0,1],       # |    1    2    |
       [0,0,0,1,1,0],       # |   /|    |\   |
       [1,0,1,0,1,0],       # |  0----- 3 |  |
       [0,0,1,1,0,0],       # |   \|    |/   |
       [1,1,0,0,0,0]]       # |    5    4    |
                            # ----------------

gr4 = [[0,1,1,1,1,1],       # ------------------
       [1,0,0,0,0,0],       # |  1 2  estrela! |
       [1,0,0,0,0,0],       # |  |/            |
       [1,0,0,0,0,0],       # |  0--3          |
       [1,0,0,0,0,0],       # |  |\            |
       [1,0,0,0,0,0]]       # |  5 4           |
                            # ------------------

gr5 = [[0,0,1,0,0,0],       # ------------------
       [0,0,1,0,0,0],       # |  1 0  estrela! |
       [1,1,0,1,1,1],       # |  |/            |
       [0,0,1,0,0,0],       # |  2--3          |
       [0,0,1,0,0,0],       # |  |\            |
       [0,0,1,0,0,0]];      # |  5 4           |
                            # ------------------

gr6 = [[0,0,1],     #
       [0,0,1],     #  0 - 2 - 1
       [1,1,0]]     #
                    #  (eh estrela?)
       
gr7 = [[0,0,1,0,0,0],    # ------------------
       [0,0,1,0,0,0],    # |  1       4     |
       [1,1,0,0,0,0],    # |  |       |     |
       [0,0,0,0,1,1],    # |  2       3     |
       [0,0,0,1,0,0],    # |  |       |     |
       [0,0,0,1,0,0]]    # |  0       5     |
                         # ------------------


# clean: ideias: uma função que retorna um dicionario vertice-distancia
# clean: ideias: ver o video e achar mais exemplos simples


import unittest

def verifica_lista_b(lista, tamanho, soma_esperada):
    potencia = 1
    soma = 0
    for i in range(tamanho):
        soma += lista[i] * potencia
        potencia *= 2
    if soma == soma_esperada:
        return True
    raise ValueError("A lista passada nao correspondeu a lista esperada")



class TestStringMethods(unittest.TestCase):

   def test01a_listas_true_false(self):
      self.assertEqual(len(arestas_1),6)
      verifica_lista_b(arestas_1,6,57)

   def test01b_listas_true_false(self):
       self.assertEqual(len(arestas_2),6)
       verifica_lista_b(arestas_2,6,23)

   def test01c_listas_true_false(self):
       self.assertEqual(len(arestas_3),6)
       verifica_lista_b(arestas_3,6,12)


   def test02_lista_tamanhos(self):
       self.assertEqual(len(max_arestas),5)
       verifica_lista_b(max_arestas,5,351)
   

   def test03a_existe_aresta(self):
    self.assertTrue (existe_aresta(gr1,0,1))
    self.assertFalse(existe_aresta(gr1,0,2))
    self.assertTrue (existe_aresta(gr1,1,2))
    self.assertTrue (existe_aresta(gr1,5,4))
    self.assertFalse(existe_aresta(gr1,1,4))
    self.assertFalse(existe_aresta(gr1,1,5))
    self.assertFalse(existe_aresta(gr1,2,4))

   def test03b_existe_aresta(self):
    self.assertTrue (existe_aresta(gr2,0,1))
    self.assertFalse(existe_aresta(gr2,0,2))
    self.assertFalse(existe_aresta(gr2,1,2))
    self.assertFalse(existe_aresta(gr2,5,4))
    self.assertFalse(existe_aresta(gr2,1,4))
    self.assertTrue (existe_aresta(gr2,1,5))
    self.assertTrue (existe_aresta(gr2,2,4))
    self.assertFalse(existe_aresta(gr2,0,3))
    self.assertTrue (existe_aresta(gr3,0,3))

   def test04a_adiciona_aresta(self):
    self.assertFalse(existe_aresta(gr3,1,2))
    adiciona_aresta (gr3,1,2)
    self.assertTrue (existe_aresta(gr3,1,2))
    self.assertTrue (existe_aresta(gr3,2,1))
   
   def test04b_adiciona_aresta(self):
   
    self.assertFalse(existe_aresta(gr3,5,4))
    adiciona_aresta(gr3,5,4)
    self.assertTrue(existe_aresta(gr3,5,4))
    self.assertTrue(existe_aresta(gr3,4,5))

   def test05_remove_aresta(self):
    remove_aresta(gr3,5,4)
    remove_aresta(gr3,1,2)
    self.assertFalse(existe_aresta(gr3,5,4))
    self.assertFalse(existe_aresta(gr3,4,5))
    self.assertFalse(existe_aresta(gr3,1,2))
    self.assertFalse(existe_aresta(gr3,2,1))
    remove_aresta(gr1,0,1)
    self.assertFalse(existe_aresta(gr1,0,1))
    self.assertFalse(existe_aresta(gr1,1,0))
    adiciona_aresta(gr1,0,1)
    self.assertTrue(existe_aresta(gr1,0,1))
    self.assertTrue(existe_aresta(gr1,1,0))

   def test06_conta_arestas(self):
    self.assertEqual(conta_arestas(gr1),6)
    self.assertEqual(conta_arestas(gr2),6)
    self.assertEqual(conta_arestas(gr3),7)
    self.assertEqual(conta_arestas(gr4),5)
    self.assertEqual(conta_arestas(gr5),5)
    self.assertEqual(conta_arestas(gr6),2)

   def test07_eh_estrela(self):
    self.assertFalse(eh_estrela(gr1))
    self.assertFalse(eh_estrela(gr2))
    self.assertFalse(eh_estrela(gr3))
    self.assertTrue (eh_estrela(gr4))
    self.assertTrue (eh_estrela(gr5))
    self.assertTrue (eh_estrela(gr6))

   def test08a_vizinhos(self):
       self.assertEqual(len(vizinhos(gr1,1)),2)
       self.assertIn(0,vizinhos(gr1,1)) # 0 tem que ser elemento dessa lista
       self.assertIn(2,vizinhos(gr1,1)) # 2 tem que ser elemento dessa lista


   def test08b_vizinhos(self):
       self.assertEqual(len(vizinhos(gr3,0)),3)
       self.assertIn(1,vizinhos(gr3,0)) # 1 tem que ser elemento dessa lista
       self.assertIn(5,vizinhos(gr3,0)) # 5 tem que ser elemento dessa lista
       self.assertIn(3,vizinhos(gr3,0)) # 3 tem que ser elemento dessa lista

   def test09a_mais_vizinhos(self):
       self.assertEqual(len(mais_vizinhos(gr1,1)),4)
       
       self.assertIn(0,mais_vizinhos(gr1,1))
       self.assertIn(5,mais_vizinhos(gr1,1))
       self.assertIn(3,mais_vizinhos(gr1,1))
       self.assertIn(2,mais_vizinhos(gr1,1))

   def test09b_mais_vizinhos(self):
       self.assertEqual(len(mais_vizinhos(gr7,2)),2)
       self.assertIn(0,mais_vizinhos(gr7,2))
       self.assertIn(1,mais_vizinhos(gr7,2))

       self.assertEqual(len(mais_vizinhos(gr7,1)),2)
       self.assertIn(0,mais_vizinhos(gr7,1))
       self.assertIn(2,mais_vizinhos(gr7,1))

       self.assertEqual(len(mais_vizinhos(gr7,5)),2)
       self.assertIn(3,mais_vizinhos(gr7,5))
       self.assertIn(4,mais_vizinhos(gr7,5))

   #fila = {'proximo':3, 'lista':[20,30,40,50,60,12]}
   def test100a_fila_insere(self):
    fila = {'proximo':3, 'lista':[20,30,40,50,60,12]}
    insere_na_fila(fila,33)
    self.assertEqual(fila,{'proximo':3, 'lista':[20,30,40,50,60,12,33]})
    insere_na_fila(fila,97)
    self.assertEqual(fila,{'proximo':3, 'lista':[20,30,40,50,60,12,33,97]})

   def test100b_fila_remove(self):
    fila = {'proximo':0, 'lista':[10,20]}
    a1=remove_da_fila(fila)
    self.assertEqual(a1,10)
    self.assertEqual(fila,{'proximo':1, 'lista':[10,20]})
    a2=remove_da_fila(fila)
    self.assertEqual(a2,20)
    self.assertEqual(fila,{'proximo':2, 'lista':[10,20]})
    insere_na_fila(fila,33)
    self.assertEqual(fila,{'proximo':2, 'lista':[10,20,33]})
    a3=remove_da_fila(fila)
    self.assertEqual(a3,33)
    self.assertEqual(fila,{'proximo':3, 'lista':[10,20,33]})
      

   def test101a_alcancaveis(self):
    self.assertEqual(len(alcancaveis(gr1,1)),6)
    self.assertIn(0,alcancaveis(gr1,1))
    self.assertIn(5,alcancaveis(gr1,1))
    self.assertIn(3,alcancaveis(gr1,1))
    self.assertIn(2,alcancaveis(gr1,1))
    self.assertIn(4,alcancaveis(gr1,1))
    self.assertIn(1,alcancaveis(gr1,1))

   def test101b_alcancaveis(self):
    self.assertEqual(len(alcancaveis(gr7,2)),3)

    self.assertIn(0,alcancaveis(gr7,2))
    self.assertIn(1,alcancaveis(gr7,2))
    self.assertIn(2,alcancaveis(gr7,2))

    self.assertEqual(len(alcancaveis(gr7,1)),3)
    self.assertIn(0,alcancaveis(gr7,1))
    self.assertIn(2,alcancaveis(gr7,1))
    self.assertIn(1,alcancaveis(gr7,1))

    self.assertEqual(len(alcancaveis(gr7,5)),3)
    self.assertIn(3,alcancaveis(gr7,5))
    self.assertIn(4,alcancaveis(gr7,5))
    self.assertIn(5,alcancaveis(gr7,5))

   def test102a_alcancaveis_dicionario_distancias(self):

    if type(alcancaveis(gr7,2)) == list:
       self.fail("para esse ultimo teste, o retorno de alcancaveis tem que ser um dicionario")
    self.assertEqual(len(alcancaveis(gr7,2)),3)

    self.assertEqual(alcancaveis(gr7,2)[0],1)
    self.assertEqual(alcancaveis(gr7,2)[1],1)
    self.assertEqual(alcancaveis(gr7,2)[2],0)

    self.assertEqual(len(alcancaveis(gr7,1)),3)
    self.assertEqual(alcancaveis(gr7,1)[0],2)
    self.assertEqual(alcancaveis(gr7,1)[2],1)
    self.assertEqual(alcancaveis(gr7,1)[1],0)

    self.assertEqual(len(alcancaveis(gr7,5)),3)
    self.assertEqual(alcancaveis(gr7,5)[5],0)
    self.assertEqual(alcancaveis(gr7,5)[3],1)
    self.assertEqual(alcancaveis(gr7,5)[4],2)
   
try: 
   from intro_grafos_gabarito import *
except:
   pass

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()
