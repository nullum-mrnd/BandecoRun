from pickle import FALSE
from random import randint
from re import X
from turtle import width
from PPlay import sprite
from PPlay.window import *
from PPlay.sprite import *

## ENTIDADES:

#### Gerador de entidades:

def EntitieGenerator(objetos, frames, pos_inicial, area):
    for objeto in objetos:
        objeto.set_curr_frame(frames)
        objeto.x = area
        objeto.y = pos_inicial
        pos_inicial -= 168

#### Desenho das entidades:

def EntitieDrawer(objetos, frames, limite, nova_pos_inicial, area):
    for objeto in objetos:
        if objeto.y > limite:
            objeto.x = area
            objeto.set_curr_frame(frames)
            objeto.y = nova_pos_inicial
        objeto.draw()

## VEICULOS:

#### Gerador de veiculos em exatamente duas faixas:

def VehicleGenerator(veiculos, frames, pos_inicial):
    for veiculo in veiculos:
        veiculo.set_curr_frame(frames)
        aux = randint(1,2)
        if aux == 1:
            veiculo.x = -10
        if aux == 2:
            veiculo.x = veiculo.width + 40
        veiculo.y = pos_inicial
        pos_inicial -= 200

#### Desenho dos veículos:

def VehicleDrawer(veiculos, frames, limite, nova_pos_inicial):
    for veiculo in veiculos:
        if veiculo.y > limite:
            aux = randint(1,3)
            if aux == 1:
                veiculo.x = -10
            if aux == 2:
                veiculo.x = veiculo.width +40
            if aux == 3:
                veiculo.x = veiculo.width +80
            veiculo.set_curr_frame(frames)
            veiculo.y = nova_pos_inicial
        veiculo.draw()


def InGame():
    in_game = Window(1000, 600)
    in_game.set_title("BandecoRun")
    fundo_vet = [Sprite("Background_1.png",1),Sprite("Background_1.png",1),Sprite("Background_1.png",1)]
    teclado = Window.get_keyboard()


    ## PLAYER
    jogador = Sprite("jogador.png", 1)
    jogador.x = in_game.width/2
    jogador.y = in_game.height/1.1 - jogador.height/2

    ## OBJETOS:

    estudante_vet = [Sprite("estudantes.png",5),Sprite("estudantes.png",5),Sprite("estudantes.png",5),Sprite("estudantes.png",5),Sprite("estudantes.png",5),Sprite("estudantes.png",5),Sprite("estudantes.png",5),Sprite("estudantes.png",5)]
    veiculos_vet = [Sprite("veiculos.png",5),Sprite("veiculos.png",5),Sprite("veiculos.png",5),Sprite("veiculos.png",5),Sprite("veiculos.png",5)]
    moedas = [Sprite("moeda.png", 1)]

    ## INTERFACE

    ## CRIAR INTERFACE NUMA FUNÇÃO SEPARADA, EM OUTRO ARQUIVO TAMBÉM
    ##interface = InterfaceSet(in_game)

    vEntitie = 250  #velocidade das entidades

    ##Posições iniciais dos primeiros objetos gerados

    ## Gerador de estudantes:
    EntitieGenerator(estudante_vet, 4, in_game.height-332, randint(in_game.width/2,740))

    ## Gerador de veiculos em exatamente duas faixas:
    VehicleGenerator(veiculos_vet, randint(1,4), 0)

    ## CENARIO

    fundo_vet[0].y = 0
    fundo_vet[1].y = -fundo_vet[1].height
    fundo_vet[2].y = -2 * fundo_vet[1].height

    ## G A M E    L O O P

    while True:

    ## Movimento do player
        if teclado.key_pressed("LEFT") and jogador.x > 0:
            jogador.x -= vEntitie * 2 * in_game.delta_time()
        if teclado.key_pressed("RIGHT") and jogador.x < 740:
            jogador.x += vEntitie * 2 * in_game.delta_time()
        #if teclado.key_pressed("UP") and jogador.y > 0:
        #    jogador.y -= vEntitie * in_game.delta_time()
        #if teclado.key_pressed("DOWN") and jogador.y < 600-jogador.height:
        #    jogador.y += vEntitie * in_game.delta_time()


    ###### DRAW #######

    ## INTERFACE

    ## CENARIO

        for fundo in fundo_vet:
            fundo.y += vEntitie * in_game.delta_time()
            if fundo.y > 600:
                fundo.y = -2 * fundo.height
            fundo.draw()

    ## ENTIDADES

        jogador.draw()
        EntitieDrawer(estudante_vet, randint(0,5), in_game.height, -200, randint(in_game.width/2, 740))
        VehicleDrawer(veiculos_vet, randint(1,4), in_game.height, -800)
        EntitieDrawer(moedas, 1, in_game.height, -randint(100,500),randint(0, 740))


    ## MOVIMENTAÇÃO DOS OBJETOS

        for estudante in estudante_vet:
            estudante.y += vEntitie * in_game.delta_time()

        for veiculo in veiculos_vet:
            veiculo.y += vEntitie* 2 * in_game.delta_time()

        for moeda in moedas:
            moeda.y += vEntitie * in_game.delta_time()


        if teclado.key_pressed("ESC"):
            return FALSE

        in_game.update()