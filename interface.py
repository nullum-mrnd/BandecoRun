from random import randint
from re import X
from turtle import width
from PPlay import sprite
from PPlay.window import *
from PPlay.sprite import *

def InterfaceSet(window):
    relogio = Sprite("relógio.png", 1)
    relogio.x = window.width/2 - relogio.width/2
    relogio.y = window.height/20 - relogio.height/2

    resist1 = Sprite("ponto_de_resistencia.png", 1)
    resist1.x = window.width/40 - resist1.width/2
    resist1.y = window.height/20 - resist1.height/2

    resist2 = Sprite("ponto_de_resistencia.png", 1)
    resist2.x = window.width/14 - resist2.width/2
    resist2.y = window.height/20 - resist2.height/2

    resist3 = Sprite("ponto_de_resistencia.png", 1)
    resist3.x = window.width/8.4 - resist3.width/2
    resist3.y = window.height/20 - resist3.height/2

    power1 = Sprite("power.png", 1)
    power1.x = window.width/30 - power1.width/2
    power1.y = window.height/1.1 - power1.height/2

    power2 = Sprite("power.png", 1)
    power2.x = window.width/10 - power2.width/2
    power2.y = window.height/1.1 - power2.height/2

    power3 = Sprite("power.png", 1)
    power3.x = window.width/6 - power3.width/2
    power3.y = window.height/1.1 - power3.height/2

    quant_moeda = Sprite("quantidade_moeda.png", 1)
    quant_moeda.x = window.width/1.04 - quant_moeda.width/2
    quant_moeda.y = window.height/1.1 - quant_moeda.height/2

    moeda2 = Sprite("moeda.png", 1)
    moeda2.x = window.width/1.1 - moeda2.width/2
    moeda2.y = window.height/1.1 - moeda2.height/2

    pontos = Sprite("pontos.png", 1)
    pontos.x = window.width/1.15 - pontos.width/2
    pontos.y = window.height/20 - pontos.height/2

    return relogio, resist1, resist2, resist3, power1, power2, power3, quant_moeda, moeda2, pontos 

def InterfaceDraw(interface_objects):
    for objects in interface_objects:
        objects.draw()