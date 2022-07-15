from random import randint
from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *

def SetObjeto(sprite, pos_x, pos_y):
    objeto = Sprite(sprite[0],sprite[1])
    objeto.x = pos_x - objeto.width/2
    objeto.y = pos_y - objeto.height/2
    return objeto

def InterfaceSet(window, cont4, galocha, sapato):
    if sapato == 1: 
        janela1 = SetObjeto(["Sprites/LOJA/sapato.png", 1], window.width/30 + 15, window.height/1.07)
    elif galocha == 1:
        janela1 = SetObjeto(["Sprites/LOJA/galocha.png", 1], window.width/30 + 15, window.height/1.07)
    else:
        janela1 = SetObjeto(["Sprites/LOJA/icones.png", 1], window.width/30 + 15, window.height/1.07)
    janela2 = SetObjeto(["Sprites/LOJA/fantasma.png", 1], window.width/30 + 103, window.height/1.07)
    moeda_icon = SetObjeto(["Sprites/GAME/moeda.png", 1], 880, window.height/1.05)

    resist1 = SetObjeto(["Sprites/GAME/ponto_de_resistencia.png", 1], window.width/40, window.height/20)
    resist2 = SetObjeto(["Sprites/GAME/ponto_de_resistencia.png", 1], resist1.width + 20, window.height/20)
    resist3 = SetObjeto(["Sprites/GAME/ponto_de_resistencia.png", 1], resist2.width + 63, window.height/20)
    resist4 = SetObjeto(["Sprites/GAME/ponto_de_resistencia.png", 1], resist3.width + 106, window.height/20)
    resist5 = SetObjeto(["Sprites/GAME/ponto_de_resistencia.png", 1], resist4.width + 149, window.height/20)
    
    if cont4 == 0:
        Interface = [janela1, janela2, moeda_icon, resist1, resist2, resist3,]
    elif cont4 == 1:
        Interface = [janela1, janela2, moeda_icon, resist1, resist2, resist3, resist4]
    elif cont4 == 2:
        Interface = [janela1, janela2, moeda_icon, resist1, resist2, resist3, resist4, resist5]

    return Interface

def InterfaceNumGame(window, frame1):
    num_janela1 = SetObjeto(["Sprites/LOJA/numero_pequeno.png", 10], window.width/30 + 102.5, window.height/ 1.07 + 25)
    num_janela1.set_curr_frame(frame1)
    Interface = [num_janela1]
    return Interface

def CriaMoedas(pos_x_ini, pos_y):
    moedas = [Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10)]
    moedas[0].x = pos_x_ini
    moedas[1].x = moedas[0].x - 40
    for num in moedas:
        num.y = pos_y
    return moedas


def InterfaceMenu(window):
    jogar = SetObjeto(["Sprites/MENU/jogar.png",1], window.width/2, window.height/1.7)
    loja = SetObjeto(["Sprites/MENU/loja.png",1], window.width/2, window.height/1.5 + 15)
    creditos = SetObjeto(["Sprites/MENU/creditos.png",1], window.width/2, window.height/1.05)
    controladores = SetObjeto(["Sprites/MENU/controles.png",1], window.width/10, window.height/1.4)
    tecla_a = SetObjeto(["Sprites/MENU/tecla_a.png",1], window.width/10 - 30, window.height/1.3 + 5)
    tecla_d = SetObjeto(["Sprites/MENU/tecla_d.png",1], window.width/10 + 30, window.height/1.3 + 5)
    power_ups = SetObjeto(["Sprites/MENU/power_ups.png",1], window.width/10, window.height/1.15)
    tecla_1 = SetObjeto(["Sprites/MENU/tecla_1.png",1], window.width/10 , window.height/1.1 + 10)
    #tecla_2 = SetObjeto(["Sprites/MENU/tecla_2.png",1], window.width/10 + 30, window.height/1.1 + 10)
    bandeco_logo = SetObjeto(["Sprites/MENU/logo_bandeco.png",1], window.width/2, window.height/4)
    ranking = SetObjeto(["Sprites/MENU/ranking.png",1], window.width/2, window.height/1.26 )

    Interface = [jogar, loja, creditos, controladores, tecla_a, tecla_d, power_ups, tecla_1, bandeco_logo, ranking]

    return Interface

def InterfaceLoja(window):
    voltar = SetObjeto(["Sprites/LOJA/voltar.png",1], window.width/2, window.height/1.05)
    janela1 = SetObjeto(["Sprites/LOJA/sapato.png", 1], 120, 310)
    janela2 = SetObjeto(["Sprites/LOJA/galocha.png", 1], 220, 310)
    janela3 = SetObjeto(["Sprites/LOJA/fantasma.png", 1], window.width/2, 310)
    #janela4 = SetObjeto(["Sprites/LOJA/icones.png", 1], 550, 310)
    janela5 = SetObjeto(["Sprites/LOJA/pdr.png", 1], 840, 310)
    loja = SetObjeto(["Sprites/LOJA/loja.png",1], window.width/2, window.height/7)
    sapatos = SetObjeto(["Sprites/LOJA/sapatos_titulo.png",1], 170, 250)
    power_ups = SetObjeto(["Sprites/LOJA/power_ups_titulo.png",1], window.width/2, 250)
    resist = SetObjeto(["Sprites/LOJA/pontos_de_resistencia_titulo.png",1], 840, 240)
    moeda_icon = SetObjeto(["Sprites/GAME/moeda.png", 1], 880, window.height/1.05)
    valor =SetObjeto(["Sprites/LOJA/valor.png", 1], window.width/2, window.height/4)

    Interface = [voltar, janela1, janela2, janela3, janela5, loja, sapatos, power_ups, resist, moeda_icon, valor]

    return Interface

def InterfaceDescr_loja(window):
    desc_janela1 = SetObjeto(["Sprites/LOJA/allstar_desc.png",1], window.width/2, 310)
    desc_janela2 = SetObjeto(["Sprites/LOJA/galochas_desc.png",1], window.width/2, 310)
    desc_janela3 = SetObjeto(["Sprites/LOJA/fantasma_desc.png",1], window.width/2, 310)
    desc_janela4 = SetObjeto(["Sprites/LOJA/pdr_desc.png",1],  window.width/2, 310)

    Interface = [desc_janela1, desc_janela2, desc_janela3, desc_janela4]

    return Interface



def InterfaceNumLoja(window, frame3, frame5):
    check1 = SetObjeto(["Sprites/LOJA/check.png", 1], 120, 337)
    check2 = SetObjeto(["Sprites/LOJA/check.png", 1], 220, 337)
    num_janela3 = SetObjeto(["Sprites/LOJA/numero_pequeno.png", 10], window.width/2 - 2, 337)
    num_janela3.set_curr_frame(frame3)
    
    num_janela5 = SetObjeto(["Sprites/LOJA/numero_pequeno.png", 10], 840, 337)
    num_janela5.set_curr_frame(frame5)


    Interface = [check1, check2, num_janela3, num_janela5]

    return Interface

def InterfaceDraw(interface_objects):
    for objects in interface_objects:
        objects.draw()

def CriaRelogio(window):
    relogio = [Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10),Sprite("Sprites/GAME/dois_pontos.png",1), Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10)]
    relogio[0].x = 532
    relogio[1].x = relogio[0].x - 40

    relogio[2].x = window.width/2 - relogio[2].width/2 - 2
    relogio[2].y = 25

    relogio[3].x = relogio[1].x - 50
    relogio[4].x = relogio[3].x - 40
    return relogio

def InterfaceVitoria(window):
    fade = Sprite("Sprites/MENU/fade_bordas.png",1)
    vitoria = SetObjeto(["Sprites/GAME/vitoria.png",1], window.width/2, 50)
    vitoria_text = SetObjeto(["Sprites/GAME/texto_vitoria1.png",1], window.width/2, 350)
    proximo = SetObjeto(["Sprites/GAME/proximo.png",1], window.width/2, 550)
    return [fade, vitoria, vitoria_text, proximo]

def InterfaceDerrota(window):
    fade = Sprite("Sprites/MENU/fade_bordas.png",1)
    derrota = SetObjeto(["Sprites/GAME/derrota.png",1], window.width/2, 50)
    derrota_text = SetObjeto(["Sprites/GAME/texto_derrota.png",1], window.width/2, 350)
    proximo = SetObjeto(["Sprites/GAME/proximo.png",1], window.width/2, 550)
    
    return [fade, derrota, derrota_text, proximo]

def Final_da_fase(window):

    fase = SetObjeto(["Sprites/GAME/fase.png",1], window.width/2, 200)
    pontuacao = SetObjeto(["Sprites/GAME/sua_pontuacao.png",1], window.width/4, 300)
    moedas = SetObjeto(["Sprites/GAME/moedas_recolhidas.png",1], 3*(window.width/4), 300)
    menu_botao = SetObjeto(["Sprites/GAME/menu_principal.png",1], window.width/2, 550)
    return [fase, pontuacao, moedas, menu_botao]

def CriaPontos(pos_x_ini, pos_y):
    pontos = [Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10)]
    pontos[5].x = pos_x_ini - pontos[0].width
    pontos[4].x = pontos[5].x - 40
    pontos[3].x = pontos[4].x - 40
    pontos[2].x = pontos[3].x - 40
    pontos[1].x = pontos[2].x - 40
    pontos[0].x = pontos[1].x - 40
    for ponto in pontos:
        ponto.y = pos_y

    return pontos

def Pausa (window):
    fade = Sprite("Sprites/MENU/fade_bordas.png",1)
    pause_titulo = SetObjeto(["Sprites/GAME/pause.png",1], window.width/2, 50)
    continuar_botao = SetObjeto(["Sprites/GAME/continuar.png",1], window.width/2, 300)
    menu_botao = SetObjeto(["Sprites/GAME/menu_principal.png",1], window.width/2, 350)
    
    return [fade, pause_titulo, continuar_botao, menu_botao]


def Audio():
    opening = Sound("Audio/Opening.OGG")
    opening.set_volume(50)
    click_som = Sound("Audio/click.OGG")
    click_som.set_volume(100)
    moeda_som = Sound("Audio/Moeda.OGG")
    moeda_som.set_volume(100)
    jogador_estudante = Sound("Audio/Batida_jogador.ogg")
    jogador_estudante.set_volume(100)
    jogador_veiculo = Sound("Audio/Jogador_veiculo.ogg")
    jogador_veiculo.set_volume(70)
    poca = Sound("Audio/Poca.ogg")
    poca.set_volume(80)
    lista = [opening, click_som, moeda_som, jogador_estudante, jogador_veiculo, poca]

    return lista