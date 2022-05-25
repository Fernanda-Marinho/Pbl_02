from funcoes import *
"""Autor: Fernanda Marinho Silva
Componente Curricular: MI - Algoritmos I
Concluido em: 22/05/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação."""

jogador1 = input("\tNome do Jogador 01:\n").upper()
jogador2 = input("\tNome do Jogador 02:\n").upper()

#Variáveis contadoras e listas vazias que serão usadas ao longo do jogo
listaJog = [jogador1,jogador2]
revelados = []
pontos1 = 0
pontos2 = 0 
historico = []
historicoJog1 = []
historicoJog2 = [] 
revelados1 = []
revelados2 = []

print("Escolha o nível:\n3)Fácil\n4)Médio\n5)Difícil")
nivel = validaMenu(input(),3,5)
 
print("Com quantos tabuleiros vocês desejeam jogar?\n1)Um tabuleiro\n2)Dois tabuleiros")
quantTabs = validaMenu(input(),1,2)

cond_encerramento = escolhaEncerramento()

if quantTabs == 1: #Modo de 1Tabuleiro 

    #Criação dos tabuleiros 
    tbCheio = contadorTabuleiroCheio(nivel)
    tabuleiroOculto = criaTabuleiroOculto(nivel)
    tabuleiroReal = criaTabuleiroReal(nivel)

    while cond_encerramento > 0 and tbCheio != 0:

            print("\n#N O V A                  J O G A D A#")
            placar(listaJog,pontos1,pontos2)
            mostraTabuleiro(tabuleiroOculto) 

            for i in range(len(listaJog)):
                print(f"Jogador {listaJog[i]}, escolha linha ou coluna [L/C]:")
                if i == 0:

                    #Jogador 1 jogando 
                    aprox1, resultado1, escolha1, numero1, historico = jogada(tabuleiroOculto,\
                    tabuleiroReal,nivel,historico)
                else:
                    
                    #Jogador 2 jogando 
                    aprox2, resultado2, escolha2, numero2, historico = jogada(tabuleiroOculto,\
                    tabuleiroReal,nivel,historico)

            """Aqui é definido o vencedor da rodada, o elemento a ser revelado, fazendo também a 
            alteração na matriz oculta e atribuindo os pontos corretos a cada um dos jogadores"""
            vencedor = comparaAprox(aprox1,aprox2,listaJog,quantTabs)
            elemento = lidandoComAproximacao(vencedor,resultado1,escolha1,numero1,tabuleiroReal,revelados,\
            listaJog,resultado2,escolha2,numero2)
            revelados,pontos1,pontos2,tabuleiroOculto,pt = lidandoComAcertos(elemento,vencedor,\
            pontos1,pontos2,revelados,tabuleiroOculto,tabuleiroReal,listaJog)
            
            #Final da rodada 
            tbCheio -= pt
            mostrarHistorico(historico)
            cond_encerramento -= 1

    """Aqui o jogo já foi encerrado. Será mostrando quem venceu o jogo, o placar final e o
    tabuleiro final."""
    vencedorFinal(tbCheio,listaJog,pontos1,pontos2)
    placar(listaJog,pontos1,pontos2)
    mostraTabuleiro(tabuleiroOculto)
    print("-*"*40)


else: #Modo de 2Tabuleiros 

    #Criação dos tabuleiros
    tabOcultoJog1 = criaTabuleiroOculto(nivel)
    tabRealJog1 = criaTabuleiroReal(nivel)
    tabOcultoJog2 = criaTabuleiroOculto(nivel)
    tabRealJog2 = criaTabuleiroReal(nivel)
    tabsCheios = 1
    tbCheio1 = contadorTabuleiroCheio(nivel)
    tbCheio2 = contadorTabuleiroCheio(nivel)

    while cond_encerramento > 0 and tabsCheios != 0:

        #Verifica se pelo menos um dos tabuleiros já foi completo 
        tabsCheios = verif2Tabs(tbCheio1,tbCheio2)

        if tabsCheios == 1: #Ambos tabuleiros incompletos, rodada pode acontecer 
            for i in range(len(listaJog)):

                print("\n#N O V A                  J O G A D A#")
                placar(listaJog,pontos1,pontos2)

                if i == 0:

                    #Jogador 1 jogando 
                    inicio2tabs(listaJog[0],historicoJog1,tabOcultoJog1)
                    aprox1, resultado1, escolha1, numero1, historicoJog1 = jogada(tabOcultoJog1,\
                    tabRealJog1,nivel,historicoJog1)
                else:

                    #Jogador 2 jogando 
                    inicio2tabs(listaJog[1],historicoJog2,tabOcultoJog2)
                    aprox2, resultado2, escolha2, numero2, historicoJog2 = jogada(tabOcultoJog2,\
                    tabRealJog2,nivel,historicoJog2)
            
            """Aqui é definido o vencedor da rodada, o elemento a ser revelado, fazendo também a 
            alteração na matriz oculta e atribuindo os pontos corretos a cada um dos jogadores"""
            vencedor = comparaAprox(aprox1,aprox2,listaJog,quantTabs)
            pR1 = 0
            pR2 = 0 
            tabOcultoJog1,tabOcultoJog2,revelados1,revelados2,pontos1,pontos2,pR1,pR2\
            = finalJogada(vencedor,listaJog,escolha1,numero1,resultado1,escolha2,numero2,resultado2,tabRealJog1,revelados1,tabRealJog2,revelados2\
            ,tabOcultoJog1,tabOcultoJog2,pontos1,pontos2,pR1,pR2)

        #Final da rodada
        tbCheio1 -= pR1
        tbCheio2 -= pR2
        tabsCheios = verif2Tabs(tbCheio1,tbCheio2)
        cond_encerramento -= 1
    
    """Aqui o jogo já foi encerrado. Será mostrando quem venceu o jogo, o placar final e o
    tabuleiro final."""
    vencedorFinal(tabsCheios,listaJog,pontos1,pontos2)
    placar(listaJog,pontos1,pontos2)
    printar2TabsFinal(listaJog,tabOcultoJog1,tabOcultoJog2)