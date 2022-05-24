from random import randint
from re import X
from turtle import width
from PPlay import sprite
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

menu = Window(1000, 600)
menu.set_title("BandecoRun")
fundo = GameImage("Background_1.png")
click = Window.get_mouse()
teclado = Window.get_keyboard()

#Limites calçada:
#cima:
#esquerda: menu.width/2
#direita: 740
#baixo:


## PLAYER
jogador = Sprite("jogador.png", 1)
jogador.x = menu.width/2
jogador.y = menu.height/1.1 - jogador.height/2


## OBSTÁCULOS

estudante_vet = [Sprite("estudantes.png",5),Sprite("estudantes.png",5),Sprite("estudantes.png",5),Sprite("estudantes.png",5),Sprite("estudantes.png",5),Sprite("estudantes.png",5),Sprite("estudantes.png",5),Sprite("estudantes.png",5)]

veiculos_vet = [Sprite("veiculos.png",5),Sprite("veiculos.png",5),Sprite("veiculos.png",5),Sprite("veiculos.png",5),Sprite("veiculos.png",5)]


moeda1 = Sprite("moeda.png", 1)
moeda1.x = menu.width/1.7
moeda1.y = menu.height/4 - moeda1.height/2

## INTERFACE

relogio = Sprite("relógio.png", 1)
relogio.x = menu.width/2 - relogio.width/2
relogio.y = menu.height/20 - relogio.height/2

resist1 = Sprite("ponto_de_resistencia.png", 1)
resist1.x = menu.width/40 - resist1.width/2
resist1.y = menu.height/20 - resist1.height/2

resist2 = Sprite("ponto_de_resistencia.png", 1)
resist2.x = menu.width/14 - resist2.width/2
resist2.y = menu.height/20 - resist2.height/2

resist3 = Sprite("ponto_de_resistencia.png", 1)
resist3.x = menu.width/8.4 - resist3.width/2
resist3.y = menu.height/20 - resist3.height/2

power1 = Sprite("power.png", 1)
power1.x = menu.width/30 - power1.width/2
power1.y = menu.height/1.1 - power1.height/2

power2 = Sprite("power.png", 1)
power2.x = menu.width/10 - power2.width/2
power2.y = menu.height/1.1 - power2.height/2

power3 = Sprite("power.png", 1)
power3.x = menu.width/6 - power3.width/2
power3.y = menu.height/1.1 - power3.height/2

quant_moeda = Sprite("quantidade_moeda.png", 1)
quant_moeda.x = menu.width/1.04 - quant_moeda.width/2
quant_moeda.y = menu.height/1.1 - quant_moeda.height/2

moeda2 = Sprite("moeda.png", 1)
moeda2.x = menu.width/1.1 - moeda2.width/2
moeda2.y = menu.height/1.1 - moeda2.height/2

pontos = Sprite("pontos.png", 1)
pontos.x = menu.width/1.15 - pontos.width/2
pontos.y = menu.height/20 - pontos.height/2


vEntitie = 100  #velocidade das entidades

##Posições iniciais dos primeiros objetos gerados
ini = menu.height-332
ini_veic = menu.height-400

## Gerador de estudantes:
for estudante in estudante_vet:
    estudante.set_curr_frame(randint(0,4))
    estudante.x = randint(menu.width/2, 740)
    estudante.y = ini
    ini -= 168

## Gerador de veiculos:
#for veiculo in veiculos_vet:
#    veiculo.set_curr_frame(randint(1,4))
#    veiculo.x = randint(0,menu.width/2 - veiculo.width)
#    veiculo.y = ini_veic
#    ini_veic -= 400

## Gerador de veiculos em exatamente duas faixas:

for veiculo in veiculos_vet:
    veiculo.set_curr_frame(randint(1,4))
    i = 1
    aux = i
    if aux == 1:
        veiculo.x = -10
    if aux == 2:
        veiculo.x = veiculo.width +40
    veiculo.y = ini_veic
    ini_veic -= 200
    i=i+1
    

while True:

## Movimento do player
    if teclado.key_pressed("LEFT") and jogador.x > 0:
        jogador.x -= vEntitie * menu.delta_time()
    if teclado.key_pressed("RIGHT") and jogador.x < 740:
        jogador.x += vEntitie * menu.delta_time()
    if teclado.key_pressed("UP") and jogador.y > 0:
        jogador.y -= vEntitie * menu.delta_time()
    if teclado.key_pressed("DOWN") and jogador.y < 600-jogador.height:
        jogador.y += vEntitie * menu.delta_time()


## Desenho
    fundo.draw()
    jogador.draw()

    for estudante in estudante_vet:
        if estudante.y > menu.height:
            estudante.x = randint(menu.width/2, 740)
            estudante.y = -168
        estudante.draw()

    #for veiculo in veiculos_vet:
    #    if veiculo.y > menu.height:
    #        veiculo.x = randint(0,menu.width/2 - veiculo.width)
    #        veiculo.y = -800
    #    veiculo.draw()


    for veiculo in veiculos_vet:
        i = 1
        if veiculo.y > menu.height:
            aux = i
            if aux == 1:
                veiculo.x = -10
            if aux == 2:
                veiculo.x = veiculo.width +40
            if aux == 3:
                veiculo.x = veiculo.width +80
            veiculo.y = -800
        i=i+1
        veiculo.draw()


    relogio.draw()
    resist1.draw()
    resist2.draw()
    resist3.draw()
    power1.draw()
    power2.draw()
    power3.draw()
    moeda1.draw()
    moeda2.draw()
    quant_moeda.draw()
    pontos.draw()

    for estudante in estudante_vet:
        estudante.y += vEntitie * menu.delta_time()

    #for veiculo in veiculos_vet:
    #    veiculo.y += vEntitie * menu.delta_time()

    menu.update()