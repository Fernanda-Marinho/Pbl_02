from random import sample

"""Abaixo estão as funções referentes ao TABULEIRO: sua formação,
comportamento e modificações."""

def criaTabuleiroOculto(num):  
    #Recebe como parâmetro o número correspondente ao nível 
    linha = [0]*num
    matriz = [linha]*num

    for l in range(num):
        linha = []
        for c in range(num):
            linha.append(0)
        matriz[l] = linha
    return matriz #Retorna uma matriz cheia de 0 

def criaTabuleiroReal(num):  
    #Recebe como parâmetro o número correspondente ao nível

    #Verifica o nível escolhido para gerar uma uma lista com números no intervalo correto 
    if num == 3:
        sort = sample(range(1,31),9) #Cria uma lista "sort" com números que não se repetem 
    elif num == 4:
        sort = sample(range(1,61),16)
    else:
        sort = sample(range(1,101),25)

    #Só a partir disso cria a matriz 
    linha = [0]*num
    matriz = [linha]*num
    cont = 0 # Vai ser usado para percorrer o índice da lista "sort" 
    for l in range(num):
        linha = []
        for c in range(num):
            linha.append(sort[cont]) 
            cont += 1 #Garante que todos os elementos da lista "sort" serão adicionados 
        matriz[l] = linha
    return matriz #Retorna a matriz com os números sorteados 

def alteraMatriz(element, mOriginal, mFake):
    #Recebe como parâmetro o(s) elemento(s) a ser removido, a matriz real e a oculta 
    pontos = 0
    if type(element) == list: #Caso de ter mais de um elemento a ser revelado
        for l in range(len(mFake)):
            for c in range(len(mFake)):
                for e in range(len(element)):
                    if mOriginal[l][c] == element[e] and mFake[l][c] == 0:
                        mFake[l][c] = element[e] 
                        pontos += 1           
        return mFake,pontos
    else: #Caso de ter apenas um elemento a ser revelado 
        for l in range(len(mFake)):
            for c in range(len(mFake)):
                if mOriginal[l][c] == element:
                    mFake[l][c] = element
                    pontos += 1
                    return mFake,pontos
    #Ambos os casos retorna a matriz oculta(alterada) e a quantidade de pontos (casas reveladas)

def contadorTabuleiroCheio(n): 
    #Recebe o nível como parâmetro 
    if n == 3:
        cont = 9 
    elif n == 4:
        cont = 16
    else:
        cont = 25
    return cont #Retorna quantas casas tem na matriz. Serve para ver se a matriz já está completa 



"""Abaixo estão as funções de PRINT que servem apenas para printar 
mensagens na tela. São funções que não retornam nenhum valor."""

def mostraTabuleiro(m):
    #Recebe como parâmetro o tabuleiro desejado e mostra-o na tela  
    for i in m:
        for j in i:  
            lenght = len(str(j))
            quant = 4 - lenght
            print(" " * quant, j, end = ' ')
        print("")

def mostrarHistorico(h):
    #Recebe o histórico desejado como parâmetro e mostra-o na tela 
    print("HISTÓRICO:")
    print("-"*30)
    for i in range(len(h)):
        if i%2 == 0: #Índices pares mostram sempre o valor chutado 
            print(f"Valor chutado =\t {h[i]}")
        else: #Índices ímpares mostram sempre o resultado (Maior ou Menor)
            print(f"Resultado =\t {h[i]}")
    print("-"*30)

def placar(lista,pts1,pts2):
    #Apenas mostra o placar 
    print("\n\tPLACAR:")
    print(f"{lista[0]}  {pts1}  X  {pts2}   {lista[1]}\n")

def printarMesmaAproximacao(jogador,e,n,r):
    #Usada quando os dois jogadores tem a mesma aproximação e diz o que será revelado na matriz 
    print()
    if r == "Maior":
            print(f"\t{jogador}:\nValor chutado é maior que a soma.\nRevela-se o MAIOR elemento de\
            {e}{n}")
    elif r == "Menor":
        print(f"\t{jogador}:\nValor chutado é menor que a soma.\nRevela-se o MENOR elemento de\
        {e}{n}")
    else:
        print(f"\t{jogador}:\nPARABÉNS! Você acertou a soma.\nRevela-se TODOS os elementos de\
        {e}{n}")
    print("-"*30) 

def printar2TabsFinal(lista,tbO1,tbO2): 
    """Recebe os jogadores e seus respectivos tabuleiros como parâmetro. É usada quando se joga
    com 2 tabuleiros e ao final da partida mostra os dois tabuleiros"""
    for i in range(len(lista)):
        print("-"*30)
        print(f"TABULEIRO DE {lista[i]}")
        if i == 0:
            mostraTabuleiro(tbO1)
        else:
            mostraTabuleiro(tbO2)
    print("-*"*40)

def vencedorFinal(tab,jogadores,p1,p2):
    #Função chamada quando o jogo encerra e mostra quem ganhou 
    print("-*"*40)
    if tab == 0:
        print("\t\t\tJOGO ENCERRADO! TABULEIRO CHEIO!")
    else:
        print("\t\t\tJOGO ENCERRADO! ACABARAM-SE AS RODADAS!")
    if p1 > p2:
        print(f"\t\t\t\t\tVENCEDOR = {jogadores[0]}")
    elif p2 > p1:
        print(f"\t\t\t\t\tVENCEDOR = {jogadores[1]}")
    else:
        print("\t\t\tEMPATE!!!")

def inicio2tabs(jog,hist,tbOculto):
    #Função que mostra a mensagem padrão de jogada para o modo de 2Tabuleiros 
    if len(hist) != 0:
        print(f"HISTÓRICO DE {jog}")
        mostrarHistorico(hist)
    print(f"TABULEIRO DE {jog}")
    mostraTabuleiro(tbOculto)
    print("-"*30)
    print(f"Jogador {jog}, escolha linha ou coluna [L/C]:")



"""Abaixo estão as funções responsáveis pelas JOGADAS: Os palpites, quem ganhou, 
O que será revelado, modificalções no placar e nas matrizes e como elas irão ocorrer."""

def escolhaEncerramento():
    #Serve para saber qual vai ser o modo de encerramento do jogo 
    print("Defina a condição de encerramento:\n1)Número de rodadas\n2)Tabuleiro cheio")
    resposta = validaMenu(input(),1,2)
    if resposta == 1:
        numeroRodadas = validaImpar(input("Digite com quantas rodadas você quer encerrar o jogo:"))
        return numeroRodadas
    else:
        return 500 #Número grande o suficiente para o jogo não acabar antes do tabuleiro encher 

def chute(m,n):
    #Recebe a matriz e o nível como parâmetro(variável nível usada pra validações)
    escolha = validaLetra(input("").upper())
    numero = validaNumero(input("Agora escolha o número da linha ou coluna:\n"),n) 
    cond = validaPreenchimento(m,escolha,numero,n)
    while cond == False:
        print("Essa linha ou coluna já foi COMPLETADA! Por favor escolha outra!\n[L/C]:\n")
        escolha = validaLetra(input("").upper())
        numero = validaNumero(input("Agora escolha o número da linha ou coluna:\n"),n)
        cond = validaPreenchimento(m,escolha,numero,n)
    chute = validaInteiro(input(f"Diga seu palpite de soma na {escolha}{numero}:\n")) 
    
    return escolha, numero, chute #Retorna a L ou C que o usuário escolheu e o seu chute  

def descobreAprox(escolha,numero,chute,m):
    #Recebe em qual L ou C o jogador jogou, seu chute e a matriz real 
    soma = 0
    for i in m:
        if escolha == "L":
            soma = sum(m[numero-1])
        else:
            soma += i[numero-1]
    if soma > chute:
        resul = "Menor"
        aprox = soma - chute
    elif soma < chute:
        resul = "Maior"
        aprox = chute - soma
    else:
        resul = "Igual"
        aprox = 0

    return aprox, resul #O valor(int) da aproximação e se ela foi maior, menor ou igual à soma

def comparaAprox(aprox1, aprox2, lista,qtTabs):
    #Recebe a aproximação e o nome de cada jogador, e com quantos tabuleiros estão sendo jogados  
    if aprox1 < aprox2:
        if qtTabs == 1: #Jogos com 2Tabuleiros, a informação do print será mostrada depois 
            print(f"\t{lista[0]} ganhou nesta rodada!")
        return lista[0] #Retorna o nome do vencedor 
    elif aprox2 < aprox1:
        if qtTabs == 1:
            print(f"\t{lista[1]} ganhou nesta rodada!")
        return lista[1]
    else:
        if qtTabs == 1:
            print("\tAmbos tiveram a mesma aproximação!")
        return lista #Nesse caso: Mesma aproximação = os dois jogadores são vencedores 

def dadosVencedor(lista,vencedor, escolha1, escolha2, numero1, numero2, result1, result2):
    #Recebe o nome dos jogadores e suas respectivas escolhas e o vencedor da rodada  

    if vencedor == lista[0]: #Significa que o jogador 1 é o vencedor 
        if result1 == "Maior":
            print(f"Valor chutado é maior que a soma.\nRevela-se o MAIOR elemento de \
            {escolha1}{numero1}")
        elif result1 == "Menor":
            print(f"Valor chutado é menor que a soma.\nRevela-se o MENOR elemento de\
            {escolha1}{numero1}")
        else:  
            print(f"PARABÉNS! Você acertou a soma.\nRevela-se TODOS os elementos\
            de {escolha1}{numero1}")
        return result1, escolha1, numero1  

    elif vencedor == lista[1]: #Significa que o jogador 1 é o vencedor
        if result2 == "Maior":
            print(f"Valor chutado é maior que a soma.\nRevela-se o MAIOR elemento\
            de {escolha2}{numero2}")
        elif result2 == "Menor":
            print(f"Valor chutado é menor que a soma.\nRevela-se o MENOR elemento\
            de {escolha2}{numero2}")
        else:
            print(f"PARABÉNS! Você acertou a soma.\nRevela-se TODOS os \
            elementos de {escolha2}{numero2}")
        return result2, escolha2, numero2
        """Retorna os dados referentes ao vencedor, essa função só é chamada quando tem APENAS 1 
        vencedor. Nesse caso não há a possibilidade dos dois tiverem a mesma aproximação."""

def identificaElemento(result, escolha, numero,m,elRev):
    #Recebe dos dados do vencedor, a matriz real e a lista dos elementos revelados 
    listaC = []
    for i in m:
        if result == "Maior":
            if escolha == "L":
                elem = max(m[numero-1])
                elemCerto = elementoJaReveladoLinha(elem,elRev,m,numero,result)
            else: 
                listaC.append(i[numero-1]) 
        elif result == "Menor":
            if escolha == "L":
                elem = min(m[numero-1])
                elemCerto = elementoJaReveladoLinha(elem,elRev,m,numero,result)
            else: 
                listaC.append(i[numero-1])
        else: #result == Igual
            if escolha == "L":
                elemCerto = m[numero-1]
            else:
                listaC.append(i[numero-1])
             

    if escolha == "C":
        if result == "Maior":
            elem = max(listaC)
            elemCerto = elementoJaReveladoColuna(elem,elRev,listaC,result)
        elif result == "Menor":
            elem = min(listaC)
            elemCerto = elementoJaReveladoColuna(elem,elRev,listaC,result)
        else:
            elemCerto = listaC

    return elemCerto #Retorna o elemento que deve ser revelado na matriz oculta 

def adicionaElementosNaLista(e,lista): 
    #Recebe o elemento a ser revelado e a lista de revelados 
    if type(e) == list: #Se ele for uma lista, é porque o jogador vencedor acertou a soma
        for i in e:
            lista.append(i) #Adiciona os elementos a serem revelados na lista de revelados 
    else: 
        lista.append(e)
    return lista #Retorna a lista de revelados 

def lidandoComAproximacao(venc,re1,el1,num1,tbReal,listaEl,listaJ,re2,el2,num2 ):
    """Função que recebe os dados do vencedor, as escolhas e resultados de todos os jogadores, a 
    lista de revelados e a matriz real. A função dela é descobrir o elemento a ser revelado. Porém
    ela trabalha com a possibilidade de ter dois vencedores (ambos com a mesma aproximação)"""

    if type(venc) == list: #Ambos tiveram a mesma aproximação 
        element = []
        elem1 = identificaElemento(re1,el1,num1,tbReal,listaEl)
        printarMesmaAproximacao(listaJ[0],el1,num1,re1)
        element = adicionaElementosNaLista(elem1,element)
        elem2 = identificaElemento(re2,el2,num2,tbReal,listaEl)
        printarMesmaAproximacao(listaJ[1],el2,num2,re2)
        element = adicionaElementosNaLista(elem2,element) 
                
    else:
        rV, eV, nV = dadosVencedor(listaJ,venc,el1,el2,num1,num2,re1,re2)
        element = identificaElemento(rV,eV,nV,tbReal,listaEl)

    return element #element pode ser uma lista ou inteiro 

def lidandoComAcertos(element,venc,p1,p2,listaEl,tbOculto,tbReal,listaJ):
    #Recebe elemento a ser revelado, dados dos jogadores, tabuleiros(real ou não) e lista de revelados
    if type(element) == list: #Acerto de soma  
        listaEl = adicionaElementosNaLista(element,listaEl)
        tbOculto,pts = alteraMatriz(element,tbReal,tbOculto) #pts = casas reveladas 
        if type(venc) == list: #Ambos com mesma aproximação 
            p1 += pts #Nesse caso essa função é usada para a modalidade de 1Tabuleiro
            p2 += pts #Por isso o segundo jogador recebe a mesma quantidade de pontos também 
        else:
            if venc == listaJ[0]:
                p1 += pts
            else:
                p2 += pts
    else: #Apenas um elemento a ser revelado(sem acerto de soma)
        listaEl.append(element)
        tbOculto,pts = alteraMatriz(element,tbReal,tbOculto)
        if type(venc) == list: 
            p1 += pts
            p2 += pts
        else:
            if venc == listaJ[0]:
                p1 += pts
            else:
                p2 += pts
    """Retorna a lista de revelados, as pontuações e a matriz oculta (ambos atualizados).
    o "pts" vai ser ajudar o programa a descobrir quando o tabuleiro se encheu. Por isso precisa
    ser retornado."""
    return listaEl,p1,p2,tbOculto,pts 

def finalJogada(venc,listaJ,el1,num1,re1,el2,num2,re2,tbR1,rev1,tbR2,rev2,tbO1,tbO2,p1,p2,pr1,pr2):
    """Função usada quando se joga com 2Tabuleiros que recebe todos os dados de todos os jogadores, 
    o vencedor, a lista de revelados de todos os jogadores, seus respectivos pontos e tabuleiros."""
    if type(venc) == list:
        print("AMBOS TIVERAM A MESMA APROXIMAÇÃO!")
        printarMesmaAproximacao(listaJ[0],el1,num1,re1)
        printarMesmaAproximacao(listaJ[1],el2,num2,re2)
        elem1 = identificaElemento(re1,el1,num1,tbR1,rev1)
        rev1 = somas2Tabs(elem1,rev1)
        tbO1,pts = alteraMatriz(elem1,tbR1,tbO1)
        pr1 = pts
        p1 += pts

        elem2 = identificaElemento(re2,el2,num2,tbR2,rev2)
        rev2 = somas2Tabs(elem2,rev2)
        tbO2,pts = alteraMatriz(elem2,tbR2,tbO2)
        pr2 = pts
        p2 += pts
    else:
        if venc == listaJ[0]:
            print(f"VENCEDOR DA RODADA --> {listaJ[0]} <--")
            printarMesmaAproximacao(listaJ[0],el1,num1,re1)
            elem1 = identificaElemento(re1,el1,num1,tbR1,rev1)
            rev1 = somas2Tabs(elem1,rev1)
            tbO1,pts = alteraMatriz(elem1,tbR1,tbO1)
            pr1 = pts
            p1 += pts
        else:
            print(f"VENCEDOR DA RODADA --> {listaJ[1]} <--")
            printarMesmaAproximacao(listaJ[1],el2,num2,re2)
            elem2 = identificaElemento(re2,el2,num2,tbR2,rev2)
            rev2 = somas2Tabs(elem2,rev2)
            tbO2,pts = alteraMatriz(elem2,tbR2,tbO2)
            pr2 = pts
            p2 += pts 
    """Revela os tabuleiros de ambos alterados, suas listas de revelados, pontos e pontos de rodadas
    (pr1 e pr2) que servem para auxiliar a descobrir se algum dos tabuleiros estão cheios"""
    return tbO1,tbO2,rev1,rev2,p1,p2,pr1,pr2

def somas2Tabs(elem,listaRev):
    #Função que adiciona o(s) elemento(s) a ser revelados à lista. Porém para trabalhar com 2Matrizes 
    if type(elem) == list: 
        listaRev = adicionaElementosNaLista(elem,listaRev) 
    else:
        listaRev.append(elem)
    return listaRev

def jogada(tbOculto,tbReal,niv,hist):
    #Jogada padrão. Pega os dados do jogador e adiciona ao seu histórico
    e, n, ch = chute(tbOculto,niv)
    hist.append(str(ch)+" Na "+str(e)+str(n))
    a, r = descobreAprox(e,n,ch,tbReal)
    hist.append(r)
    return a, r, e, n, hist #Retorna suas escolhas e seu histórico 



"""Abaixo estão as funções referentes a VALIDAÇÕES, onde é feita a verificação se determinado
input dado pelo usuário pode ser aceitado ao não, tanto em relação as dimensões da matriz quanto
à caracteres do teclado"""

def validaPreenchimento(m,escolha,num,niv):
    #Verifica se todos os elementos de uma determinada linha ou coluna estão totalmente preenchidos 
    cont = 0
    listaColuna = []
    for l in m:
        if escolha == "L":
            if l == m[num-1]:
                for i in l:
                    if i != 0:
                        cont += 1
        else:
            listaColuna.append(l[num-1])
    for j in listaColuna:
        if j != 0:
            cont += 1
    if cont == niv: 
        return False #Significa que todos os elementos da L ou C estão preenchidos 
    else: 
        return True #Pelo menos um elemento da L ou C está sem preencher

def elementoJaReveladoLinha(el,lista,m,numero,resul):
    #Verifica se determinado elemento está presente na linha
    aux = []
    for i in m[numero-1]:
        aux.append(i)
    if el in lista:
        cond = True
        while cond == True: 
            """Garante que se o elemento estiver na linha, ele será removido 
            e outro de igual propriedade será retornado no lugar"""
            aux.remove(el)
            if resul == "Maior":
                el = max(aux)
            else:
                el = min(aux)
            if el in lista:
                cond = True
            else:
                cond = False
        return el
    else:
        return el #Por fim, será removido o elemento correto. 

def elementoJaReveladoColuna(el,lista,listC,resul):
    #Faz a mesma coisa da função acima, porém na coluna 
    if el in lista:
        cond = True
        while cond == True:
            listC.remove(el)
            if resul == "Maior":
                el = max(listC)
            else:
                el = min(listC)
            if el in lista:
                cond = True
            else:
                cond = False
        return el
    else:
        return el

def validaMenu(variavel,num1,num2):
    #Recebe o input do usuário, o primeiro nº do menu e o último 
    while variavel.isdigit() == False or int(variavel) < num1 or int(variavel)> num2:
        #Valida qualquer menu que aparece no jogo
        variavel = input(f"Por favor digite um número entre {num1} e {num2}!\n")
    return int(variavel) #Retorna o input correto em forma de inteiro 

def validaLetra(var):
    #Garante que vai ser a letra L ou C. Usa quando o jogador escolhe a linha ou coluna pra jogar 
    while var != 'L' and var != 'C':
        var = input("Erro\nDigite apenas L ou C!\n").upper()
    return var #Retorna a letra correta 

def validaNumero(num,nivel):
    #Garante que o usuário vai digitar uma L ou C válida naquele tabuleiro 
    while num.isdigit() == False or int(num) < 1 or int(num) > nivel:
        num = input("ERRO!\nEssa linha ou coluna não existe no tabuleiro\nDigite novamente:\n")
    return int(num) #Retorna esse número em formato de inteiro 

def validaImpar(num):
    #Garante que o input será um número ímpar 
    while num.isdigit() == False or int(num)%2 == 0:
        num = input("ERRO!\nDigite um número ÍMPAR:\n")
    return int(num) #Retorna esse número em formato de inteiro 

def validaInteiro(num):
    #Garante o input será um número. Usado quando o jogador vai chutar a soma
    while num.isdigit() == False:
        num = input("ERRO!\nDigite um NÚMERO:\n")
    return int(num) #Retorna esse número em formato de inteiro 

def verif2Tabs(tb1,tb2):
    #Usada no modo de 2Matrizes. Verifica se pelo menos um das matrizes estão completas 
    if tb1 == 0 or tb2 == 0:
        return 0
    else: 
        return 1

