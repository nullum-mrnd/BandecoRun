from random import randint
from PPlay.collision import *
from PPlay.window import *
from PPlay.sprite import *

## ENTIDADES:

#### Gerador de entidades:

def EntitieGenerator(objetos, frames, pos_inicial, area):
    for objeto in objetos:
        objeto.set_curr_frame(frames)
        objeto.x = area
        objeto.y = pos_inicial
        pos_inicial -= 200


#### Desenho das entidades:

def EntitieDrawer(objetos, frames, limite, pos_inicial, area):
    for objeto in objetos:
        if objeto.y > limite:
            objeto.x = area
            objeto.set_curr_frame(frames)
            objeto.y = pos_inicial
        objeto.draw()

def BuildingDrawer(predios, frames, limite, pos_inicial, area):
    for i in range (5,0,-1):
        if predios[i].y > limite:
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

# lista_contadores[0] -> Pontos de resistência
# lista_contadores[1] -> Moedas
# lista_contadores[2] -> Lentidão?
def GameObjectsPhysics(jogador, colisor, tipo, lista_contadores, janela, ultimo_colidido):
    index_colisor = ""
    if type(colisor) is list:
        for objeto in colisor:
                if tipo == 1:   # MOEDA
                    if Collision.collided_perfect(jogador, objeto):
                        ultimo_colidido = colisor.index(objeto)
                        lista_contadores[1] += 1
                        print("moedas:")
                        print(lista_contadores[1])
                elif tipo == 2: # ESTUDANTE
                    if Collision.collided_perfect(jogador, objeto) and colisor.index(objeto) != ultimo_colidido[0]:
                            lista_contadores[0] -= 1
                            print("vida:")
                            print(lista_contadores[0])
                            print(ultimo_colidido)
                            print(colisor.index(objeto))
                            ultimo_colidido[0] = colisor.index(objeto)
                elif tipo == 3:
                    if Collision.collided_perfect(jogador, objeto):
                        index_colisor = colisor.index(objeto)
                        lista_contadores[0] -= 2
                        print("vida:")
                        print(lista_contadores[0])
                # elif tipo == 4:
                #     if Collision.collided_perfect(jogador, objeto):
                #         index_colisor = colisor.index(objeto)
                #         lista_contadores[0] -= 3
                # elif tipo == 5:
                #     if Collision.collided_perfect(jogador, objeto):
                #         index_colisor = colisor.index(objeto)
                #         lista_contadores[2] = 1

    return [lista_contadores, ultimo_colidido]