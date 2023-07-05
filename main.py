from maquinas.MaquinaMoore import MaquinaMoore
from maquinas.AutomatoDePilha import AutomatoDePilha
from utils import *
from combate import Combate
from player import Player


def inicializaPlayer():
    nomePlayer = input("Digite o nome do jogador: ")
    tipoMaquina = input(
        "Digite o tipo de máquina: (1 - Moore, 2 - Automato de Pilha)")
    file1 = input("Digite o nome do arquivo: ")
    if tipoMaquina == '1':
        estados, estadosIniciais, transicoes = leArquivo(file1)
        maquina = MaquinaMoore(estados, estadosIniciais[0], transicoes)
    elif tipoMaquina == '2':
        estados, estadosIniciais, transicoes = leArquivoAp(file1)
        maquina = AutomatoDePilha(estados, estadosIniciais[0], transicoes)

    return Player(maquina, nomePlayer)


def pvp():
    clear()
    file = "ap1.txt"
    estados, estados_iniciais, transicoes = leArquivoAp(file)

    player1 = inicializaPlayer()
    player2 = inicializaPlayer()

    combate = Combate(player1, player2)
    combate.executa()


if __name__ == "__main__":
    pvp()
    # fileType = input("Digite 1 para PVP ou 2 para PVE: ")
    # if fileType == '1':
    #     pvp()
    # elif fileType == '2':
    #     pve()
