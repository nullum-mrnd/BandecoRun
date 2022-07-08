from random import randint
from PPlay.collision import *
from PPlay.window import *
from PPlay.sprite import *

## ENTIDADES:

#### Gerador de entidades:

def EntitieGenerator(objetos, frames, y_inicial, x1, x2, delay):

    lista_objeto = []
    for objeto in objetos:         
        objeto.set_curr_frame(randint(0, frames))
        objeto.x = randint(x1, x2)
        objeto.y = y_inicial
        y_inicial -= 500
        
        lista_objeto.append(objeto)

    return lista_objeto


#### Desenho das entidades:

def EntitieDrawer(objetos, frames, y_inicial, x1, x2, limite):
    for objeto in objetos:
        if objeto.y > limite:
            objeto.set_curr_frame(randint (0, frames))
            objeto.x = randint(x1,x2)
            objeto.y = y_inicial
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


# moedas, estudantes, carros, onibus, poça
#   1          2         3       4     5

# lista_contadores[0] -> Pontos de resistência estudantes
# lista_contadores[1] -> Moedas
# lista_contadores[2] -> Pontos de resistência estudantes carros
def GameObjectsPhysics(jogador, colisor, tipo, lista_contadores, ultimo_colidido, Interface_jogo, moedas):
    if type(colisor) is list:
        for objeto in colisor:
            if tipo == 1:   # MOEDA
                    if Collision.collided_perfect(jogador, objeto) and colisor.index(objeto) != ultimo_colidido[0] and (objeto.x + 30 > jogador.x) and (objeto.y + 40 > jogador.y):
                        ultimo_colidido[0] = colisor.index(objeto)
                        lista_contadores[1] += 1


            if tipo ==2:  #ESTUDANTES

                if Collision.collided_perfect(jogador, objeto) and colisor.index(objeto) != ultimo_colidido[0] and (objeto.x + 75 > jogador.x) and (objeto.y + 50 > jogador.y):
                    lista_contadores[0] -= 1
                    ultimo_colidido[0] = colisor.index(objeto)
                            
                    if lista_contadores[0] == 2:
                        Interface_jogo.pop(2)
                    elif lista_contadores[0] == 1:
                        Interface_jogo.pop(1)
                    elif lista_contadores[0] == 0:
                        Interface_jogo.pop(0)

            elif tipo == 3:
                if Collision.collided_perfect(jogador, objeto) and colisor.index(objeto) != ultimo_colidido[0] and (objeto.x + 100 > jogador.x) and (objeto.y + 200 > jogador.y):
                    print("bateu carro")
                    lista_contadores[0] -= 2
                    ultimo_colidido[0] = colisor.index(objeto)

                    lista_contadores[0] -= 2
                    if lista_contadores[0] == 3:
                        Interface_jogo[2].hide()
                        Interface_jogo[1].hide()
                    elif lista_contadores[0] == 2:
                        Interface_jogo[1].hide()
                        Interface_jogo[0].hide()
                    elif lista_contadores[0] == 1:
                        Interface_jogo[0].hide()
    
                # elif tipo == 4:
                #     if Collision.collided_perfect(jogador, objeto):
                #         index_colisor = colisor.index(objeto)
                #         lista_contadores[0] -= 3
                # elif tipo == 5:
                #     if Collision.collided_perfect(jogador, objeto):
                #         index_colisor = colisor.index(objeto)
                #         lista_contadores[2] = 1


