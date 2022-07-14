from random import randint
from PPlay.collision import *
from PPlay.window import *
from PPlay.sprite import *

## ENTIDADES:

#### Gerador de entidades:

def EntitieGenerator(objetos, frames, y_inicial, x1, x2):

    lista_objeto = []
    for objeto in objetos:         
        objeto.set_curr_frame(randint(0, frames))
        objeto.x = randint(x1, x2)
        objeto.y = y_inicial
        y_inicial -= 250
        
        lista_objeto.append(objeto)

    return lista_objeto


#### Desenho das entidades:

def EntitieDrawer(in_game, objetos, frames, y_inicial, x1, x2, limite, parada_pv, parada_gra, fase, delay_drawer):
    delay_drawer[0] += in_game.delta_time()
    for objeto in objetos:
        if objeto.y > limite and  delay_drawer[0] > 2:
            objeto.set_curr_frame(randint (0, frames-1))
            #PV
            if fase == 1:
                if parada_pv > -300:
                    x3 = 290
                    x4 = 720
                    objeto.x = randint(x3,x4)
                elif parada_pv < 0:
                    objeto.x = randint(x1,x2)
                if parada_pv < 400:
                    objeto.y = y_inicial
            #GRAG 
            elif fase == 2:
                if parada_gra > -600:
                    x3 = 300
                    x4 = 740
                    objeto.x = randint(x3,x4)
                elif parada_gra < 0:
                    objeto.x = randint(x1,x2)
                if parada_gra < 400:
                    objeto.y = y_inicial
            delay_drawer[0] = 0


        objeto.draw()      


def BuildingGenerator(objetos, frames, pos_inicial, area):
    for objeto in objetos:         
        objeto.set_curr_frame(frames)
        objeto.x = area
        objeto.y = pos_inicial
        pos_inicial -= 200

def BuildingDrawer(predios, frames, limite, pos_inicial, area, tempo):
    for i in range (5,0,-1):
        if predios[i].y > limite and tempo >=12:
            predios[i].x = area
            predios[i].set_curr_frame(frames)
            predios[i].y = pos_inicial
        predios[i].draw()

## VEICULOS:

#### Gerador de veiculos em exatamente duas faixas:

def VehicleGenerator(veiculos, frames, pos_inicial):
    for i in range(0,4):
        if i != 3:
            veiculos[i].set_curr_frame(randint(0, frames))
            aux = randint(1,2)
            if aux == 1:
                veiculos[i].x = -10
            if aux == 2:
                veiculos[i].x = veiculos[i].width + 40
            veiculos[i].y = pos_inicial
            pos_inicial -= 2500
        else:
            veiculos[i].set_curr_frame(0)
            aux = randint(1,2)
            if aux == 1:
                veiculos[i].x = -10
            if aux == 2:
                veiculos[i].x = veiculos[i].width + 40
            veiculos[i].y = pos_inicial
            pos_inicial -= 2500
#### Desenho dos veículos:

def VehicleDrawer(tempo, in_game, delay_drawer, veiculos, frames, limite, nova_pos_inicial):
    delay_drawer[2] += in_game.delta_time()

    for i in range(0,4):
        if i != 3:
            if veiculos[i].y > limite and delay_drawer[2] > 2:
                veiculos[i].set_curr_frame(frames)
                aux = randint(1,2)
                if aux == 1:
                    veiculos[i].x = randint(-50, 80)
                if aux == 2:
                    veiculos[i].x = randint(210,320)
                    
                if tempo >= 12: 
                    veiculos[i].y = nova_pos_inicial
                delay_drawer[2] = 0
        else:
            if veiculos[i].y > limite and delay_drawer[2] > 2:
                veiculos[i].set_curr_frame(0)
                aux = randint(1,2)
                if aux == 1:
                    veiculos[i].x = randint(-50, 80)
                if aux == 2:
                    veiculos[i].x = randint(210,320)
                    
                if tempo >= 12: 
                    veiculos[i].y = nova_pos_inicial
                delay_drawer[2] = 0
        veiculos[i].draw()

# moedas, estudantes, carros, onibus, poça
#   1          2         3       4     5

# lista_contadores[0] -> Pontos de resistência estudantes
# lista_contadores[1] -> Moedas
# lista_contadores[2] -> Pontos de resistência estudantes carros
def GameObjectsPhysics(jogador, colisor, tipo, lista_contadores, delay_colision,delay_moeda, Interface_jogo):
    pisca_player = 0
    if type(colisor) is list:
        for objeto in colisor:
            
            if tipo == 1:   # MOEDA
                if objeto.y > 620:
                    objeto.unhide()
                if Collision.collided_perfect(jogador, objeto) and (jogador.x + jogador.width - 15 > objeto.x) and (jogador.x < objeto.x + objeto.width- 25):
                    lista_contadores[1] += 1
                    objeto.hide()
                    
                    delay_colision = 0
                    pisca_player = pisca_player
                    delay_moeda = 0



            if tipo ==2:  #ESTUDANTES
                if Collision.collided_perfect(jogador, objeto) and (jogador.x + jogador.width - 15 > objeto.x) and (jogador.x < objeto.x + objeto.width-25) and (jogador.y < objeto.y + objeto.width + 5):
                    
                    lista_contadores[0] -= 1
                    #3 VIDAS
                    if lista_contadores[5] == 0:
                        if lista_contadores[0] == 2:
                            Interface_jogo.pop(2)
                        elif lista_contadores[0] == 1:
                            Interface_jogo.pop(1)
                        elif lista_contadores[0] == 0:
                            Interface_jogo.pop(0)
                    #4 VIDAS
                    if lista_contadores[5] == 1:
                        if lista_contadores[0] == 3:
                            Interface_jogo.pop(6)
                        elif lista_contadores[0] == 2:
                            Interface_jogo.pop(2)
                        elif lista_contadores[0] == 1:
                            Interface_jogo.pop(1)
                        elif lista_contadores[0] == 0:
                            Interface_jogo.pop(0)
                    #5 VIDAS
                    if lista_contadores[5] == 2:
                        print("foi2")
                        if lista_contadores[0] == 4:
                            Interface_jogo.pop(7)
                        elif lista_contadores[0] == 3:
                            Interface_jogo.pop(6)
                        elif lista_contadores[0] == 2:
                            Interface_jogo.pop(2)
                        elif lista_contadores[0] == 1:
                            Interface_jogo.pop(1)
                        elif lista_contadores[0] == 0:
                            Interface_jogo.pop(0)
                    delay_colision = 0
                    pisca_player = 200
                    delay_moeda = delay_moeda

            elif tipo == 3: ## CARRO
                if Collision.collided_perfect(jogador, objeto) and (jogador.x + jogador.width - 50> objeto.x) and (jogador.x < objeto.x + objeto.width -50) and (jogador.y + jogador.height > objeto.y) and (jogador.y < objeto.y + 173):
                    print("bateu carro")
                    lista_contadores[0] -= 2

                    if lista_contadores[0] == 1:
                        Interface_jogo[2].hide()
                        Interface_jogo[1].hide()
                    elif lista_contadores[0] == 0:
                        Interface_jogo[0].hide()
                    delay_colision = 0
                    pisca_player = 200
                    delay_moeda = delay_moeda
    
            #elif tipo == 4: ## ONIBUS

            elif tipo == 5: ## POÇA
                if Collision.collided_perfect(jogador, objeto) and (jogador.x + jogador.width - 15 > objeto.x) and (jogador.x < objeto.x + objeto.width):
                    print("poça")
                    lista_contadores[4] = 3
                    delay_colision = 0
                    pisca_player = 200
                    delay_moeda = delay_moeda 

        return [delay_colision, pisca_player, delay_moeda]
            # elif tipo == 5:
            #     if Collision.collided_perfect(jogador, objeto) and (jogador.x + jogador.width - 15 > objeto.x) and (jogador.x < objeto.x + objeto.width):
            #         lista_contadores[2] = 1
