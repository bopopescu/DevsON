# -*- coding: utf-8 -*-

import sys

#Trabalahar com windows2
#import win32ui

import easygui

import log
import Variaveis
import Roteiro_Lanc
import Tecla
import Paramentros

from login import LogarSistema


def main():
    FrontFarma = LogarSistema("FrontFarma")
    #FrontFarma.login()

    msg = "Add Tempo ADD"
    title = "VSM - Automação"
    fieldNames = ["Informao Tempo Adicional"]
    fieldValues = easygui.multenterbox(msg, title, fieldNames)
    if fieldValues == None:
        sAdd = 0
        sys.exit()
    else:
        sAdd = int(''.join(fieldValues))  # Converte Vetor para String

    Variaveis.TempoAdd = sAdd

    msg = "Repetir precesso"
    title = "VSM - Automação"
    fieldNames = ["Quantas vezes deseja repetir o processo"]
    fieldValues = easygui.multenterbox(msg, title, fieldNames)

    if fieldValues == None:
        sQtd = 0
        sys.exit()
    else:
        sQtd = int(''.join(fieldValues))  # Converte Vetor para String
    Variaveis.NVezes = (sQtd)

    Paramentros.Parametros()

    if Variaveis.CodLoja != '0':
        for x in range(0,3):
            Tecla.Esc()
        Tecla.ClickGrid()
        Tecla.Crtx()
        if Variaveis.DocFiscal != '':
            Roteiro_Lanc.Roteiro()
    else:
        log.EscreverLog("Nao foi definido a loja para os testes")
        sys.exit(1)

if __name__ == '__main__':
    main()

"""
class App(object):

    def __int__(self):
        pass

    def AbriApp(self):
        pass
        #iniciar aplicativo
    def AppLogin(self):
        pass
        #relação ao login


class TestesFrontFarma(object):

    def __int__(self):
        pass


def main():

    app = App()
    if app.AbriApp('ourofarma'):
        app.AppLogin()

"""
