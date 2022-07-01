from random import randint
from PPlay.window import *
from PPlay.sprite import *

def SetObjeto(sprite, pos_x, pos_y):
    objeto = Sprite(sprite[0],sprite[1])
    objeto.x = pos_x - objeto.width/2
    objeto.y = pos_y - objeto.height/2
    return objeto

def InterfaceSet(window):
    #relogio = SetObjeto(["Sprites/GAME/relógio.png",1], window.width/2, window.height/20)
    resist1 = SetObjeto(["Sprites/GAME/ponto_de_resistencia.png", 1], window.width/40, window.height/20)
    resist2 = SetObjeto(["Sprites/GAME/ponto_de_resistencia.png", 1], resist1.width + 20, window.height/20)
    resist3 = SetObjeto(["Sprites/GAME/ponto_de_resistencia.png", 1], resist2.width + 63, window.height/20)
    janela1 = SetObjeto(["Sprites/LOJA/icones.png", 1], window.width/30 + 15, window.height/1.07)
    janela2 = SetObjeto(["Sprites/LOJA/icones.png", 1], window.width/30 + 103, window.height/1.07)
    moeda_icon = SetObjeto(["Sprites/GAME/moeda.png", 1], window.width/1.1, window.height/1.05)

    Interface = [resist1, resist2, resist3, janela1, janela2, moeda_icon]

    return Interface

def InterfaceNumGame(window, frame1, frame2, frame3):
    num_janela1 = SetObjeto(["Sprites/LOJA/numero_pequeno.png", 10], window.width/30 + 14.5, window.height/1.07 + 25)
    num_janela1.set_curr_frame(frame1)
    num_janela2 = SetObjeto(["Sprites/LOJA/numero_pequeno.png", 10], window.width/30 + 102.5, window.height/ 1.07 + 25)
    num_janela2.set_curr_frame(frame2)
    num_moeda = SetObjeto(["Sprites/GAME/numero.png", 10], window.width/1.04 + 10, window.height/ 1.05)
    num_moeda.set_curr_frame(frame3)
    Interface = [ num_janela1, num_janela2, num_moeda]
    return Interface

def InterfaceSair(window):
    sair = SetObjeto(["Saida.png",1], window.width/2, window.height/2)
    sim = SetObjeto(["Saida(sim).png",1], window.width/2.5, window.height/1.8)
    nao = SetObjeto(["Saida(nao).png",1], window.width/1.7, window.height/1.8)

    Interface = [sair, sim, nao]
    return Interface

def InterfaceMenu(window):
    jogar = SetObjeto(["Sprites/MENU/jogar.png",1], window.width/2, window.height/1.7)
    loja = SetObjeto(["Sprites/MENU/loja.png",1], window.width/2, window.height/1.5 + 15)
    creditos = SetObjeto(["Sprites/MENU/creditos.png",1], window.width/2, window.height/1.05)
    controladores = SetObjeto(["Sprites/MENU/controles.png",1], window.width/10, window.height/1.4)
    tecla_a = SetObjeto(["Sprites/MENU/tecla_a.png",1], window.width/10 - 30, window.height/1.3 + 5)
    tecla_d = SetObjeto(["Sprites/MENU/tecla_d.png",1], window.width/10 + 30, window.height/1.3 + 5)
    power_ups = SetObjeto(["Sprites/MENU/power_ups.png",1], window.width/10, window.height/1.15)
    tecla_1 = SetObjeto(["Sprites/MENU/tecla_1.png",1], window.width/10 - 30, window.height/1.1 + 10)
    tecla_2 = SetObjeto(["Sprites/MENU/tecla_2.png",1], window.width/10 + 30, window.height/1.1 + 10)
    bandeco_logo = SetObjeto(["Sprites/MENU/logo_bandeco.png",1], window.width/2, window.height/4)

    Interface = [jogar, loja, creditos, controladores, tecla_a, tecla_d, power_ups, tecla_1, tecla_2, bandeco_logo]

    return Interface

def InterfaceLoja(window):
    voltar = SetObjeto(["Sprites/LOJA/voltar.png",1], window.width/2, window.height/1.05)
    janela1 = SetObjeto(["Sprites/LOJA/icones.png", 1], 120, 310)
    janela2 = SetObjeto(["Sprites/LOJA/icones.png", 1], 220, 310)
    janela3 = SetObjeto(["Sprites/LOJA/icones.png", 1], 450, 310)
    janela4 = SetObjeto(["Sprites/LOJA/icones.png", 1], 550, 310)
    janela5 = SetObjeto(["Sprites/LOJA/icones.png", 1], 840, 310)
    loja = SetObjeto(["Sprites/LOJA/loja.png",1], window.width/2, window.height/7)
    sapatos = SetObjeto(["Sprites/LOJA/sapatos_titulo.png",1], 170, 250)
    power_ups = SetObjeto(["Sprites/LOJA/power_ups_titulo.png",1], window.width/2, 250)
    resist = SetObjeto(["Sprites/LOJA/pontos_de_resistencia_titulo.png",1], 840, 240)


    Interface = [voltar, janela1, janela2, janela3, janela4, janela5, loja, sapatos, power_ups, resist]

    return Interface

def InterfaceNumLoja(window, frame1, frame2, frame3, frame4, frame5):
    num_janela1 = SetObjeto(["Sprites/LOJA/numero_pequeno.png", 10], 120, 337)
    num_janela1.set_curr_frame(frame1)
    num_janela2 = SetObjeto(["Sprites/LOJA/numero_pequeno.png", 10], 220, 337)
    num_janela2.set_curr_frame(frame2)
    num_janela3 = SetObjeto(["Sprites/LOJA/numero_pequeno.png", 10], 450, 337)
    num_janela3.set_curr_frame(frame3)
    num_janela4 = SetObjeto(["Sprites/LOJA/numero_pequeno.png", 10], 550, 337)
    num_janela4.set_curr_frame(frame4)
    num_janela5 = SetObjeto(["Sprites/LOJA/numero_pequeno.png", 10], 840, 337)
    num_janela5.set_curr_frame(frame5)


    Interface = [num_janela1, num_janela2, num_janela3, num_janela4, num_janela5]

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
    menu_botao = SetObjeto(["Sprites/GAME/menu_principal.png",1], window.width/2, 500)
    return [fase, pontuacao, moedas, menu_botao]

def CriaPontos(window):
    pontos = [Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10), Sprite("Sprites/GAME/numero.png",10)]
    pontos[0].x = window.width - pontos[0].width
    pontos[1].x = pontos[0].x - 40
    pontos[2].x = pontos[1].x - 40
    pontos[3].x = pontos[2].x - 40
    pontos[4].x = pontos[3].x - 40
    pontos[5].x = pontos[4].x - 40

    return pontos

def Pausa (window):
    fade = Sprite("Sprites/MENU/fade_bordas.png",1)
    pause_titulo = SetObjeto(["Sprites/GAME/pause.png",1], window.width/2, 50)
    continuar_botao = SetObjeto(["Sprites/GAME/continuar.png",1], window.width/2, 300)
    menu_botao = SetObjeto(["Sprites/GAME/menu_principal.png",1], window.width/2, 350)
    
    return [fade, pause_titulo, continuar_botao, menu_botao]