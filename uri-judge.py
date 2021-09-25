/*Flíper é um tipo de jogo onde uma bolinha de metal cai por um labirinto de caminhos até chegar na parte de baixo do labirinto. 
A quantidade de pontos que o jogador ganha depende do caminho que a bolinha seguir. 
O jogador pode controlar o percurso da bolinha mudando a posição de algumas portinhas do labirinto. 
Cada portinha pode estar na posição 0, que significa virada para a esquerda, ou na posição 1 que quer dizer virada para a direita. 
Considere o flíper da figura abaixo, que tem duas portinhas. A portinha P está na posição 1 e a portinha R, na posição 0. Desse jeito, a bolinha vai cair pelo caminho B.
Você deve escrever um programa que, dadas as posições das portinhas P e R, neste flíper da figura, diga por qual dos três caminhos, A, B ou C, a bolinha vai cair!*/


a,b = input().split()
a = int(a)
b = int(b)
if(a==0):
    print("C")
if(a==1 and b == 0):
    print("B")
if(a==1 and b == 1):
    print("A")
    
/*Beatriz gosta muito de jogar cartas com as amigas. Para treinar memória e raciocínio lógico, ela inventou um pequeno passatempo com cartas. 
Ela retira as cinco primeiras cartas do topo de um baralho bem embaralhado, e as coloca em sequência, da esquerda para a direita, na mesa, com as faces voltadas para baixo.
Então ela olha, por um breve instante, cada uma das cartas da sequência (e logo as recoloca na mesa, com a face para baixo). 
Usando apenas a sua memória, Beatriz deve agora dizer se a sequência de cartas está ordenada crescentemente, decrescentemente, ou não está ordenada.
De tanto jogar, ela está ficando cansada, e não confia em seu próprio julgamento para saber se acertou ou errou. 
Por isso, ela pediu para você fazer um programa que, dada uma sequência de cinco cartas, determine se a sequência dada está ordenada crescentemente, decrescentemente, ou não está ordenada.
A entrada consiste de uma única linha que contém as cinco cartas da sequência. Os valores das cartas são representados por inteiros entre 1 e 13. As cinco cartas têm valores distintos.*/

a,b,c,d,e = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

if (a<b and b<c and c <d and d<e):
    print ("C")
elif (a>b and b>c and c >d and d>e):
    print ("D")
else:
    print ("N")
