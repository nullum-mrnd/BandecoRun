from random import randint

from pygame.time import delay
from PPlay import collision
from PPlay.animation import Animation
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.collision import * 
from PPlay.sprite import *
from entities import *
from interface import *

## PRECISA FAZER UMA VARIAVEL GLOBAL DE MOEDAS PRA GUARDAR O QUE VOCÊ COLETOU EM TODAS AS FASES
## PRECISA IMPLEMENTAR O POWER UP FANTASMA
## PRECISA VER SE TODOS OS MENUS TÃO COM AS SPRITES NOS LUGARES CERTOS
## PRECISA IMPLEMENTAR O ONIBUS + COLISAO
## PRECISA ARRUMAR O NUMERO DA LOJA DO POWER UP QUE N TEM (NEM SEI QUAL IMPLEMENTARIA) E O CLIQUE DOS PONTOS DE RESISTENCIA EXTRA
## PRECISA IMPLEMENTAR OS PONTOS DE RESISTENCIA EXTRA

in_game = Window(1000, 600)
in_game.set_title("BandecoRun")
fundo_vet = [Sprite("Sprites/GAME/ruas.png",3),Sprite("Sprites/GAME/ruas.png",3),Sprite("Sprites/GAME/ruas.png",3)]
fundos = [Sprite("Sprites/fundo_menus.png",1), Sprite("Sprites/MENU/fade_bordas.png",1) ]
click = Window.get_mouse()
teclado = Window.get_keyboard()
fundo_pv = [Sprite("Sprites/GAME/uff_pv.png",3),Sprite("Sprites/GAME/uff_pv.png",3),Sprite("Sprites/GAME/uff_pv.png",3)]
fundo_grag = [Sprite("Sprites/GAME/uff_grag.png",3),Sprite("Sprites/GAME/uff_grag.png",3),Sprite("Sprites/GAME/uff_grag.png",3)]


# VARIAVEIS DO GAME
game_status = 0
tempo_recarga = 0
estado_pausa = 0
perdeu = 0
venceu = 0

## VELOCIDADES
vEntitie = 170  #velocidade das entidades
vPlayer = 250




## PLAYER
jogador = Sprite("Sprites/GAME/jogador1.png", 3)
jogador.x = in_game.width/2
jogador.y = in_game.height/1.1 - jogador.height/2
lista_contadores = [5,0,3,0,0,0]

## INTERFACE
Interface_menu = InterfaceMenu(in_game)
interface_vit = InterfaceVitoria(in_game)
interface_derrota = InterfaceDerrota(in_game)
final = Final_da_fase(in_game)
Interface_loja = InterfaceLoja(in_game)
num_moedas = [0,0]
cont1 = 0; cont2 = 0; cont3 = 0; cont4 = 0; cont5 = 0 #controlador dos numeros (loja)
count1_1 = 0; count1_2 = 0;count1_3 = 0


# GERACAO DE OBJETOS
onibus = Sprite("Sprites/GAME/onibus.png",1)
predios = Sprite("Sprites/GAME/predios.png",2)
estudantes = [Sprite("Sprites/GAME/estudantes.png",5),Sprite("Sprites/GAME/estudantes.png",5),Sprite("Sprites/GAME/estudantes.png",5),Sprite("Sprites/GAME/estudantes.png",5),Sprite("Sprites/GAME/estudantes.png",5)]  
moedas = [Sprite("Sprites/moeda.png", 1)]
veiculos = [Sprite("Sprites/GAME/carros.png",4),Sprite("Sprites/GAME/carros.png",4),Sprite("Sprites/GAME/carros.png",4), onibus]
poças = [Sprite("Sprites/GAME/poça.png",1)]


##COLISAO
prox = 0
contador = [0,1,3]
roberto = 0
pisou_poca = 0
delay_colision = 4
delay_moeda = 4
delay_drawer = [0, 0, 0]
delay_fantasma = 4
delay_fantasma2 = 0

etapa_final_fase = 0
chuva = 0
chover = Animation("Sprites/GAME/chuva.png",3,True)
delay_menu = 2

##ITENS LOJA

sapato = 0
galocha = 0
fantasma = 0
pdrextra = 0
comprou_sapato = 0
comprou_galocha = 0

fase = 1

## G A M E    L O O P
while True:
    
    # ----------- TELA MENU -----------
    if game_status == 0:

        #SETANDO PARA UMA FASE
        pisca_player = 0
        clima_chuva = 0
        perdeu = 0
        venceu = 0
        etapa_final_fase = 0
        vEntitie = 250
        vPlayer = 250
        jogador.x = in_game.width/2
        jogador.y = in_game.height/1.1 - jogador.height/2
        fundo_vet[0].y = 0
        fundo_vet[1].y = -600
        fundo_vet[2].y = -2 * 600
        EntitieGenerator(estudantes, 4, -100, in_game.width/2, 740)
        EntitieGenerator(moedas, 1, - -1000, 100, 500)
        VehicleGenerator(veiculos, 4, -1000)
        EntitieGenerator(poças,1,-2000,0,740)

        


        delay_menu += in_game.delta_time()
        Interface_num_game = InterfaceNumGame(in_game, cont3)
        InterfaceDraw(fundos)
        InterfaceDraw(Interface_menu)
        #APLICA "CLICK" NOS BOTÕES
        if (click.is_over_object(Interface_menu[0]) == True ) and (click.is_button_pressed(1)) and delay_menu >= 0.3:
            jogador.set_curr_frame(0)
            ##PRAIA VERMELHA
            if fase == 1 or fase == 4:
                ## CAMPUS PV SET
                bandejao_pv = Sprite("Sprites/GAME/bandejao_pv.png",1)
                bandejao_pv.x = 1000 - bandejao_pv.width
                fundo_pv[0].set_curr_frame(0)
                fundo_pv[1].set_curr_frame(1)
                fundo_pv[2].set_curr_frame(2)
                
                fundo_pv[0].y = -600
                fundo_pv[1].y = -1200
                fundo_pv[2].y = -1800
            ## GRAGOATA
            elif fase == 2 or fase == 4:
                ## CAMPUS GRAG SET
                bandejao_grag = Sprite("Sprites/GAME/bandejao_grag.png",1)
                arvores_grag = Sprite("Sprites/GAME/arvores_grag.png",1)
                fundo_grag[0].set_curr_frame(0)
                fundo_grag[1].set_curr_frame(1)
                fundo_grag[2].set_curr_frame(2)

                fundo_grag[0].y = -600
                fundo_grag[1].y = -1200
                fundo_grag[2].y = -1800
                #arvores_grag.y = fundo_grag[2].y
                bandejao_grag.y = fundo_grag[2].y

            
            ## VIDAS
            if cont4 == 0:
                lista_contadores[0] = 3
            if cont4 == 1:
                lista_contadores[0] = 4
            if cont4 == 2:
                lista_contadores[0] = 5
            
            print(vEntitie)
            ## BOTAS
            if sapato == 1:
                vEntitie = vEntitie*1.3
                vPlayer = vPlayer*1.5
            
            
            ## RELOGIO
            tempo = 30
            relogio = CriaRelogio(in_game)
            dez_seg = 3
            uni_seg = 0
            minutos = 1

            ## PONTUACAO
            pontos = CriaPontos(1000, 0)
            score = 0
            unidades_ponto = [0,0,0,0,0,0]

            # MOEDAS
            qtd_moedas = CriaMoedas(930, 535)

            ##INTERFACE
            Interface_jogo = InterfaceSet(in_game, cont4, galocha, sapato)
            # for fundo in fundo_vet:
            #     fundo.set_curr_frame(randint(0,2))

            game_status = 1

        elif (click.is_over_object(Interface_menu[1]) == True ) and (click.is_button_pressed(1)):
            game_status = 2
        elif (click.is_over_object(Interface_menu[2]) == True ) and (click.is_button_pressed(1)):
            game_status = 0

    
    # ----------- TELA JOGO -----------

    elif game_status == 1:
        ## ANIMAÇAO FINAL PLAYER
        if etapa_final_fase == 1:
            if fase == 1 or fase == 3:
                if jogador.y > 200:
                    jogador.move_y(-150*in_game.delta_time())
                if jogador.y <= 200 and jogador.x < 750:
                    jogador.set_curr_frame(1)
                    jogador.move_x(150*in_game.delta_time())
                if jogador.y <= 200 and jogador.x >= 750:
                    venceu = 1
                

            elif fase == 2 or fase == 4: ## CAMPUS GRAG (AINDA NÃO TEM A ANIMACAO DO GRAGOATA)
                if jogador.y > 200:
                    jogador.move_y(-150*in_game.delta_time())
                if jogador.y <= 200 and jogador.x < 750:
                    jogador.set_curr_frame(2)
                    jogador.move_x(-150*in_game.delta_time())
                if jogador.y <= 200 and jogador.x <= 200:
                    venceu = 1
                    

        if fase == 1 or fase == 3:
            if fundo_pv[2].y >= 0:
                vEntitie = 0
        elif fase == 2 or fase == 4:
            if fundo_grag[2].y >= 0:
                vEntitie = 0

        if int(tempo) != 0 and perdeu == 0:

            ## CENARIO
            for fundo in fundo_vet:
                if estado_pausa == 0:
                    fundo.y += vEntitie * in_game.delta_time()
                    if fundo.get_curr_frame() == 0  and fundo.y >= -600 and fundo.y <= 600:
                        predios.y = fundo.y
                    if fundo.y > 600 and fundo.get_curr_frame() != 0:
                        fundo.y = -2 * fundo.height
                        fundo.set_curr_frame(randint(0,2))
                    if fundo.y > 600 and fundo.get_curr_frame() == 0:
                        fundo.y = -2 * fundo.height
                        fundo.set_curr_frame(randint(0,2))
                fundo.draw()
                predios.draw()

            if fase == 1 or fase == 3:
                if int(tempo) <= 8:
                
                    for fundo in fundo_pv:
                        if estado_pausa == 0:
                            fundo.y += vEntitie * in_game.delta_time()
                            bandejao_pv.y = fundo_pv[2].y
                            fundo.draw()

            if fase == 2 or fase == 4:
                if int(tempo) <= 8:
                    for fundo in fundo_grag:
                        if estado_pausa == 0:
                            fundo.y += vEntitie * in_game.delta_time()
                            bandejao_grag.y = fundo_grag[2].y
                            fundo.draw()
            if fase == 1 or fase == 3:
                if fundo_pv[2].y >= 0:
                    etapa_final_fase = 1
            if fase == 2 or fase == 4:
                if fundo_grag[2].y >= 0:
                    etapa_final_fase = 1

            ## PLAYER

            if estado_pausa == 0:
                if teclado.key_pressed("LEFT") and jogador.x > 0 and etapa_final_fase == 0:
                    jogador.x -= vPlayer * 2 * in_game.delta_time()
                if teclado.key_pressed("RIGHT") and jogador.x < 720 and etapa_final_fase == 0:
                    jogador.x += vPlayer * 2 * in_game.delta_time()
                
                if etapa_final_fase != 1:
                    if pisca_player > 0:
                        pisca_player -= 1
                        if pisca_player % 2 == 1:
                            jogador.set_curr_frame(0)
                        if pisca_player % 2 == 0:
                            jogador.set_curr_frame(3) 
                    else:
                        jogador.set_curr_frame(0)

                
                in_game.draw_text("moedas: " + str(lista_contadores[1]),0,280,30,(255,255,255),"Arial",False,False)
            
                if etapa_final_fase == 0:
                    delay_colision += in_game.delta_time()
                    delay_moeda += in_game.delta_time()
                    
                    ## POÇAS
                    EntitieDrawer(in_game, poças,1,-700,0,740,600, fundo_pv[0].y, fundo_grag[0].y, fase, delay_drawer)
                    if delay_colision > 2 and fantasma == 0 and galocha == 0:
                        collision_return = GameObjectsPhysics(jogador, poças, 4, lista_contadores,delay_colision,delay_moeda,Interface_jogo)
                        delay_colision = collision_return[0]
                        pisca_player = collision_return[1]
                        
                    for poça in poças:
                        poça.y += vEntitie * in_game.delta_time()
                    # MOEDAS
                    EntitieDrawer(in_game, moedas, 1, -1000, 100 , 740, in_game.height,fundo_pv[0].y,fundo_grag[0].y, fase, delay_drawer)
                    if delay_moeda > 5:
                        collision_return =  GameObjectsPhysics(jogador, moedas, 1, lista_contadores, delay_colision,delay_moeda, Interface_jogo)
                        #delay_colision = collision_return[0]
                        #pisca_player = collision_return[1]
                        delay_moeda = collision_return[2]
                    for moeda in moedas:
                        moeda.y += vEntitie * in_game.delta_time()
                
                    ## ESTUDANTES                     
                    EntitieDrawer(in_game, estudantes, 4, -300, in_game.width/2, 740, in_game.height, fundo_pv[0].y, fundo_grag[0].y, fase, delay_drawer)
                    if delay_colision > 2 and fantasma == 0:                 
                        collision_return = GameObjectsPhysics(jogador, estudantes, 2, lista_contadores, delay_colision,delay_moeda, Interface_jogo)
                        delay_colision = collision_return[0]
                        pisca_player = collision_return[1]
                    for estudante in estudantes:
                        estudante.y += vEntitie * in_game.delta_time()

                    ## VEICULOS
                    VehicleDrawer(int(tempo), in_game, delay_drawer, veiculos, randint(0,3), in_game.height, -1000)
                    if delay_colision > 2 and fantasma == 0:
                        collision_return = GameObjectsPhysics(jogador, veiculos, 3, lista_contadores, delay_colision,delay_moeda, Interface_jogo)
                        delay_colision = collision_return[0]
                        pisca_player = collision_return[1]
                    for veiculo in veiculos:
                        veiculo.y += vEntitie* 2.5 * in_game.delta_time()
                
                    ## PREDIOS
                    # BuildingDrawer(predios, randint(0,4), in_game.height, -predios[0].height, randint(760,900), tempo)
                    # for predio in predios:
                    #     predio.y += vEntitie * in_game.delta_time()


                    if lista_contadores[4] > 0:
                        vPlayer = 200
                        lista_contadores[4] -= 2*in_game.delta_time()
                    else:
                        vPlayer =  250

                    
                ##DESENHA PLAYER
                jogador.draw()

                ## BANDEJAO PV
                if fase == 1 or fase == 3:
                    if fundo_pv[1].y >= 0:
                        bandejao_pv.draw()
                ## BANDEJAO GRAG
                elif fase == 2 or fase == 4:
                    if fundo_grag[1].y >= 0:
                        bandejao_grag.draw()
                    
                    arvores_grag.x = 0
                    arvores_grag.y = fundo_grag[2].y
                    arvores_grag.draw()
            if fase > 2:
            ##CHUVA
                chover.set_total_duration(500)
                chover.play()
                chover.draw()
                chover.update()

            if estado_pausa == 0 and etapa_final_fase == 0:
                ## INTERFACE
                Interface_num_game = InterfaceNumGame(in_game, cont3)
                if lista_contadores[0] > 0:
                    InterfaceDraw(Interface_jogo)
                else:
                    perdeu = 1
                InterfaceDraw(Interface_num_game)

                ## RELOGIO
                if etapa_final_fase == 0:
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

            ## PONTUACAO
                if etapa_final_fase == 0:
                    unidades_ponto[0] += 1
                for num in pontos:
                    num.draw()
                
                for i in range(6):
                    if unidades_ponto[i] > 9:
                        unidades_ponto[i] = 0
                        unidades_ponto[i+1] += 1

                pontos[0].set_curr_frame(unidades_ponto[0])
                pontos[1].set_curr_frame(unidades_ponto[1])
                pontos[2].set_curr_frame(unidades_ponto[2])
                pontos[3].set_curr_frame(unidades_ponto[3])
                pontos[4].set_curr_frame(unidades_ponto[4])
                pontos[5].set_curr_frame(unidades_ponto[5])

            ## MOEDAS
                num_moedas[0] = lista_contadores[1] - (int(lista_contadores[1]/10)*10)
                num_moedas[1] = int(lista_contadores[1]/10)

                qtd_moedas[0].set_curr_frame(num_moedas[0])
                qtd_moedas[1].set_curr_frame(num_moedas[1])

                for num in qtd_moedas:
                    num.draw()

                if num_moedas[1] == 0:
                    qtd_moedas[1].hide()

            ##FANTASMA

                delay_fantasma += in_game.delta_time()
                delay_fantasma2 += in_game.delta_time()

                if (teclado.key_pressed("1") == 1) and cont3 > 0 and delay_fantasma > 5:
                    cont3 -=1
                    fantasma = 1
                    delay_fantasma = 0

                if delay_fantasma2 > 10:
                    fantasma = 0
                    delay_fantasma2 = 0
            
            #VIDA EXTRA
        


        #PAUSE
            if (teclado.key_pressed("ESC") == 1):
                estado_pausa = 1
            if estado_pausa == 1:
                pausa = Pausa(in_game)
                InterfaceDraw(pausa)
                if(click.is_over_object(pausa[2]) == True ) and (click.is_button_pressed(1)):
                    estado_pausa = 0
                if(click.is_over_object(pausa[3]) == True ) and (click.is_button_pressed(1)):
                    estado_pausa = 0
                    game_status = 0
                    delay_menu = 0
        

        ##DEBUG
        in_game.draw_text("game status:" + str(game_status),0,50,30,(255,255,255),"Arial",False,False)
        in_game.draw_text("vidas:" + str(lista_contadores[0]),0,80,30,(255,255,255),"Arial",False,False)
        in_game.draw_text("TEMPO:" + str(int(tempo)),0,100,30,(255,255,255),"Arial",False,False)

        #print(vPlayer)
        ## FINAL DO JOGO
        if venceu == 1 and prox == 0:            
            InterfaceDraw(fundos)
            InterfaceDraw(interface_vit)
            if(click.is_over_object(interface_vit[3]) == True ) and (click.is_button_pressed(1)):
                prox = 1

        if perdeu == 1 and prox == 0:            
            InterfaceDraw(fundos)
            InterfaceDraw(interface_derrota)
            if(click.is_over_object(interface_derrota[3]) == True ) and (click.is_button_pressed(1)):
                prox = 1

                #game_status = 0

        if (venceu == 1 or perdeu == 1) and prox == 1:
            InterfaceDraw(fundos)
            InterfaceDraw(final)
            pontos = CriaPontos(in_game.width/3 + 40, 306)
            pontos[0].set_curr_frame(unidades_ponto[0])
            pontos[1].set_curr_frame(unidades_ponto[1])
            pontos[2].set_curr_frame(unidades_ponto[2])
            pontos[3].set_curr_frame(unidades_ponto[3])
            pontos[4].set_curr_frame(unidades_ponto[4])
            pontos[5].set_curr_frame(unidades_ponto[5])
            for num in pontos:
                num.draw()
            
            qtd_moedas = CriaMoedas(2*(in_game.width/3) + 40,306)
            num_moedas[0] = lista_contadores[1] - (int(lista_contadores[1]/10)*10)
            num_moedas[1] = int(lista_contadores[1]/10)

            qtd_moedas[0].set_curr_frame(num_moedas[0])
            qtd_moedas[1].set_curr_frame(num_moedas[1])
        
            for num in qtd_moedas:
                num.draw()

            if num_moedas[1] == 0:
                qtd_moedas[1].hide()

            if(click.is_over_object(final[3]) == True ) and (click.is_button_pressed(1)) and prox == 1:
                game_status = 0
                prox = 0
                fase += venceu

    elif game_status == 2:
        lista_contadores[1] = 50
        Interface_num_loja = InterfaceNumLoja(in_game, 0 + cont3, 0 + cont4)
        InterfaceDraw(fundos)
        InterfaceDraw(Interface_loja)
        if sapato == 0:
            Interface_num_loja[0].hide()
        if galocha == 0:
            Interface_num_loja[1].hide()
        InterfaceDraw(Interface_num_loja)
        #Interface_jogo[5].draw()
        qtd_moedas = CriaMoedas(930, 535)
        num_moedas[0] = lista_contadores[1] - (int(lista_contadores[1]/10)*10)
        num_moedas[1] = int(lista_contadores[1]/10)

        qtd_moedas[0].set_curr_frame(num_moedas[0])
        qtd_moedas[1].set_curr_frame(num_moedas[1])

        for num in qtd_moedas:
            num.draw()

        #VOLTA AO MENU
        if (teclado.key_pressed("ESC") == 1):      
            game_status = 0
        if (click.is_over_object(Interface_loja[0]) == True ) and (click.is_button_pressed(1)):
            game_status = 0

        #MUDA O VALOR DA QUANTIDADE DE ITENS COMPRADOS
    
        tempo_recarga += in_game.delta_time()

        if (click.is_over_object(Interface_loja[1]) == True ) and (click.is_button_pressed(1)) and lista_contadores[1] >= 5 and sapato == 0:
            sapato = 1
            galocha = 0
            if comprou_sapato == 0:
                lista_contadores[1] -= 5
            comprou_sapato = 1


        elif (click.is_over_object(Interface_loja[2]) == True ) and (click.is_button_pressed(1)) and lista_contadores[1] >= 5 and galocha == 0:
            galocha = 1
            sapato = 0
            if comprou_galocha == 0:
                lista_contadores[1] -= 5
            comprou_galocha = 1

        elif (click.is_over_object(Interface_loja[3]) == True ) and (click.is_button_pressed(1)) and (tempo_recarga > 0.5) and (cont3 <= 2) and lista_contadores[1] >= 5 :
            cont3 += 1
            tempo_recarga = 0
            lista_contadores[1] -= 5


        elif (click.is_over_object(Interface_loja[4]) == True ) and (click.is_button_pressed(1)) and (tempo_recarga > 0.5) and (cont4 <= 1) and lista_contadores[1] >= 5 :
            cont4 += 1
            tempo_recarga = 0
            lista_contadores[1] -= 5
            lista_contadores[5] = cont4

        # elif (click.is_over_object(Interface_loja[5]) == True ) and (click.is_button_pressed(1)) and (tempo_recarga > 0.5) and (cont5 <= 4) and lista_contadores[1] >= 5 :
        #     cont5 += 1
        #     tempo_recarga = 0
        #     lista_contadores[1] -= 5

    in_game.update()




































    