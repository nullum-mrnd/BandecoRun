from random import randint
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from entities import *
from interface import *


in_game = Window(1000, 600)
in_game.set_title("BandecoRun")
fundo_vet = [Sprite("Sprites/GAME/fundo1_sem_predios.png",1),Sprite("Sprites/GAME/fundo1_sem_predios.png",1),Sprite("Sprites/GAME/fundo1_sem_predios.png",1)]
fundos = [Sprite("Sprites/fundo_menus.png",1), Sprite("Sprites/MENU/fade_bordas.png",1) ]
click = Window.get_mouse()
teclado = Window.get_keyboard()

game_status = 0
tempo_recarga = 0

## PLAYER
jogador = Sprite("Sprites/GAME/jogador.png", 1)
jogador.x = in_game.width/2
jogador.y = in_game.height/1.1 - jogador.height/2

## OBJETOS:

estudantes = [Sprite("Sprites/GAME/estudantes.png",5),Sprite("Sprites/GAME/estudantes.png",5),Sprite("Sprites/GAME/estudantes.png",5),Sprite("Sprites/GAME/estudantes.png",5),Sprite("Sprites/GAME/estudantes.png",5),Sprite("Sprites/GAME/estudantes.png",5),Sprite("Sprites/GAME/estudantes.png",5),Sprite("Sprites/GAME/estudantes.png",5)]
veiculos = [Sprite("Sprites/GAME/veiculos.png",5),Sprite("Sprites/GAME/veiculos.png",5),Sprite("Sprites/GAME/veiculos.png",5),Sprite("Sprites/GAME/veiculos.png",5),Sprite("Sprites/GAME/veiculos.png",5)]
moedas = [Sprite("Sprites/moeda.png", 1), Sprite("Sprites/moeda.png", 1)]

## INTERFACE


Interface_jogo = InterfaceSet(in_game)
Interface_saida = InterfaceSair(in_game)
Interface_menu = InterfaceMenu(in_game)
Interface_loja = InterfaceLoja(in_game)
cont1 = 0; cont2 = 0; cont3 = 0; cont4 = 0; cont5 = 0

vEntitie = 250  #velocidade das entidades

#PREDIOS

predios = [Sprite("Sprites/GAME/predios.png",5), Sprite("Sprites/GAME/predios.png",5), Sprite("Sprites/GAME/predios.png",5), Sprite("Sprites/GAME/predios.png",5), Sprite("Sprites/GAME/predios.png",5), Sprite("Sprites/GAME/predios.png",5)]
EntitieGenerator(predios, randint(0,4), in_game.height, randint(760, 850))

## Gerador de estudantes:
EntitieGenerator(estudantes, 4, in_game.height-332, randint(in_game.width/2,740))

## Gerador de veiculos em exatamente duas faixas:
VehicleGenerator(veiculos, randint(1,4), 0)

## CENARIO INICIAL

fundo_vet[0].y = 0
fundo_vet[1].y = -fundo_vet[1].height
fundo_vet[2].y = -2 * fundo_vet[1].height


# RELOGIO

relogio = CriaRelogio(in_game)
dez_seg = 2
uni_seg = 9
minutos = 0
tempo = 10

prox = 0
## G A M E    L O O P

while True:


    # ----------- TELA MENU -----------
    if game_status == 0:
        InterfaceDraw(fundos)
        InterfaceDraw(Interface_menu)

        #APLICA "CLICK" NOS BOTÕES
        if (click.is_over_object(Interface_menu[0]) == True ) and (click.is_button_pressed(1)):
            game_status = 1
        elif (click.is_over_object(Interface_menu[1]) == True ) and (click.is_button_pressed(1)):
            game_status = 2
        elif (click.is_over_object(Interface_menu[2]) == True ) and (click.is_button_pressed(1)):
            game_status = 0

    
    # ----------- TELA JOGO -----------

    elif game_status == 1:
        if int(tempo) != 0:
            ## Movimento do player
            if teclado.key_pressed("LEFT") and jogador.x > 0:
                    jogador.x -= vEntitie * 2 * in_game.delta_time()
            if teclado.key_pressed("RIGHT") and jogador.x < 720:
                    jogador.x += vEntitie * 2 * in_game.delta_time()

            ###### DRAW #######

            ## CENARIO

            for fundo in fundo_vet:
                fundo.y += vEntitie * in_game.delta_time()
                if fundo.y > 600:
                    fundo.y = -2 * fundo.height
                fundo.draw()

            ## ENTIDADES

            jogador.draw()

            EntitieDrawer(estudantes, randint(0,5), in_game.height, -200, randint(in_game.width/2, 740))
            EntitieDrawer(moedas, randint(0,5), in_game.height, -randint(100,500),randint(0, 740))
            VehicleDrawer(veiculos, randint(1,4), in_game.height, -800)
            BuildingDrawer(predios, randint(0,4), in_game.height, -predios[0].height, randint(760,900))

            ## MOVIMENTAÇÃO DOS OBJETOS

            for estudante in estudantes:
                estudante.y += vEntitie * in_game.delta_time()

            for veiculo in veiculos:
                veiculo.y += vEntitie* 2 * in_game.delta_time()

            for moeda in moedas:
                moeda.y += vEntitie * in_game.delta_time()
            
            for predio in predios:
                predio.y += vEntitie * in_game.delta_time()

            ## INTERFACE
            InterfaceDraw(Interface_jogo)


            ## RELOGIO
            tempo -= 1 * in_game.delta_time()
            uni_seg -= 1 * in_game.delta_time()
            for num in relogio:
                num.draw()
            relogio[0].set_curr_frame(int(uni_seg))
            relogio[1].set_curr_frame(dez_seg)
            relogio[3].set_curr_frame(minutos)
            
            if uni_seg < 0:
                dez_seg -= 1
                uni_seg = 10
                
            if dez_seg < 0:
                minutos -= 1
                dez_seg = 5

    ## FINAL DO JOGO
    if int(tempo) == 0 and prox == 0 and game_status == 1:            
        interface_vit = InterfaceVitoria(in_game)
        InterfaceDraw(interface_vit)
        if(click.is_over_object(interface_vit[2]) == True ) and (click.is_button_pressed(1)):
            prox = 1

    if int(tempo) == 0 and prox == 1 and game_status == 1:
        final = Final_da_fase(in_game)
        InterfaceDraw(final)
        if(click.is_over_object(final[3]) == True ) and (click.is_button_pressed(1)) and prox == 1:
            print("debug")
            game_status = 0

        
        #CONTROLE DE SAIDA
    if (teclado.key_pressed("ESC") == 1): 
        InterfaceDraw(Interface_saida)
        if(click.is_over_object(Interface_saida[1]) == True ) and (click.is_button_pressed(1)):
            game_status = 0


    elif game_status == 2:
        Interface_num_loja = InterfaceNumLoja(in_game, 0 + cont1, 0 + cont2, 0 + cont3, 0 + cont4, 0 + cont5)
        InterfaceDraw(fundos)
        InterfaceDraw(Interface_loja)
        InterfaceDraw(Interface_num_loja)

        #VOLTA AO MENU
        if (teclado.key_pressed("ESC") == 1):      
            game_status = 0
        if (click.is_over_object(Interface_loja[0]) == True ) and (click.is_button_pressed(1)):
            game_status = 0

        #MUDA O VALOR DA QUANTIDADE DE ITENS COMPRADOS
    
        tempo_recarga += in_game.delta_time()

        if (click.is_over_object(Interface_loja[1]) == True ) and (click.is_button_pressed(1)) and (tempo_recarga > 0.5) and (cont1 <= 4) :
            cont1 += 1
            tempo_recarga = 0

        elif (click.is_over_object(Interface_loja[2]) == True ) and (click.is_button_pressed(1)) and (tempo_recarga > 0.5) and (cont2 <= 4) :
            cont2 += 1
            tempo_recarga = 0

        elif (click.is_over_object(Interface_loja[3]) == True ) and (click.is_button_pressed(1)) and (tempo_recarga > 0.5) and (cont3 <= 4) :
            cont3 += 1
            tempo_recarga = 0

        elif (click.is_over_object(Interface_loja[4]) == True ) and (click.is_button_pressed(1)) and (tempo_recarga > 0.5) and (cont4 <= 4) :
            cont4 += 1
            tempo_recarga = 0

        elif (click.is_over_object(Interface_loja[5]) == True ) and (click.is_button_pressed(1)) and (tempo_recarga > 0.5) and (cont5 <= 4) :
            cont5 += 1
            tempo_recarga = 0


    in_game.update()