from random import randint
from PPlay.window import *
from PPlay.sprite import *

def SetObjeto(sprite, pos_x, pos_y):
    objeto = Sprite(sprite[0],sprite[1])
    objeto.x = pos_x - objeto.width/2
    objeto.y = pos_y - objeto.height/2
    return objeto

def InterfaceSet(window):
    relogio = SetObjeto(["relógio.png",1], window.width/2, window.height/20)
    resist = SetObjeto(["ponto_de_resistencia.png", 1], window.width/40, window.height/20)
    power = SetObjeto(["power.png", 1], window.width/30, window.height/1.1)
    qnt_moeda = SetObjeto(["quantidade_moeda.png", 1], window.width/1.04, window.height/1.1)
    moeda_icon = SetObjeto(["moeda.png", 1], window.width/1.1, window.height/1.1)
    pontos = SetObjeto(["pontos.png", 1], window.width/1.15, window.height/20)

    Interface = [relogio, resist, power, qnt_moeda, moeda_icon, pontos]

    return Interface

def InterfaceDraw(interface_objects):
    for objects in interface_objects:
        objects.draw()