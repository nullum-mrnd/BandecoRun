from random import randint
from PPlay.collision import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

#SONS


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
            objeto.set_curr_frame(randint(0, frames))
            #PV
            if fase == 1 or fase == 3:
                if parada_pv > -300:
                    x3 = 290
                    x4 = 720
                    objeto.x = randint(x3,x4)
                elif parada_pv < 0:
                    objeto.x = randint(x1,x2)
                if parada_pv < 400:
                    objeto.y = y_inicial
            #GRAG 
            elif fase == 2 or fase == 4:
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

## VEICULOS:

#### Gerador de veiculos em exatamente duas faixas:

def VehicleGenerator(veiculos, frames, pos_inicial):
    for i in range(0,4):
        if i != 3:
            veiculos[i].set_curr_frame(randint(0, frames-1))
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
                    
                if tempo >= 15: 
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
                    
                if tempo >= 15: 
                    veiculos[i].y = nova_pos_inicial
                delay_drawer[2] = 0
        veiculos[i].draw()

# moedas, estudantes, carros, onibus, poça
#   1          2         3       4     5

# lista_contadores[0] -> Pontos de resistência estudantes
# lista_contadores[1] -> Moedas
# lista_contadores[2] -> Pontos de resistência estudantes carros
def GameObjectsPhysics(jogador, colisor, tipo, lista_contadores, delay_colision,delay_moeda, Interface_jogo, indice_vida_col, som, score):
    pisca_player = 0
    if type(colisor) is list:
        for objeto in colisor:
            
            if tipo == 1:   # MOEDA
                if objeto.y > -1000:
                    objeto.unhide()
                if Collision.collided_perfect(jogador, objeto) and (jogador.x + jogador.width - 15 > objeto.x) and (jogador.x < objeto.x + objeto.width- 25):
                    som[2].play()
                    lista_contadores[1] += 1
                    objeto.hide()
                    score += 50
                    delay_colision = 0
                    pisca_player = pisca_player
                    delay_moeda = 0



            if tipo ==2:  #ESTUDANTES
                if Collision.collided_perfect(jogador, objeto) and (jogador.x + jogador.width - 15 > objeto.x) and (jogador.x < objeto.x + objeto.width-25) and (jogador.y < objeto.y + objeto.width + 5):
                    som[3].play()
                    score -= 24
                    lista_contadores[0] -= 1
                    if indice_vida_col <= len(Interface_jogo) - 3:
                        Interface_jogo[-indice_vida_col].hide()
                        indice_vida_col += 1
                    delay_colision = 0
                    pisca_player = 200
                    delay_moeda = delay_moeda

            elif tipo == 3: ## CARRO
                if Collision.collided_perfect(jogador, objeto) and (jogador.x + jogador.width - 50> objeto.x) and (jogador.x < objeto.x + objeto.width -50) and (jogador.y + jogador.height > objeto.y) and (jogador.y < objeto.y + 173):
                    som[4].play()
                    if objeto.height == 173:
                        score -= 37
                        lista_contadores[0] -= 2
                        if indice_vida_col <= len(Interface_jogo) - 3:
                            for i in range(indice_vida_col,indice_vida_col + 2):
                                Interface_jogo[-i].hide()
                                indice_vida_col += 1
                        delay_colision = 0
                        pisca_player = 200
                        delay_moeda = delay_moeda
                    if objeto.height == 365:
                        score -= 157
                        lista_contadores[0] -= 3
                        if indice_vida_col <= len(Interface_jogo) - 3:
                            for i in range(indice_vida_col,indice_vida_col + 3):
                                Interface_jogo[-i].hide()
                                indice_vida_col += 1
                        delay_colision = 0
                        pisca_player = 200
                        delay_moeda = delay_moeda

            elif tipo == 5: ## POÇA
                if Collision.collided_perfect(jogador, objeto) and (jogador.x + jogador.width - 15 > objeto.x) and (jogador.x < objeto.x + objeto.width):
                    som[5].play()
                    lista_contadores[4] = 5
                    delay_colision = 0
                    pisca_player = 0
                    delay_moeda = delay_moeda 

        return [delay_colision, pisca_player, delay_moeda, indice_vida_col, score]
