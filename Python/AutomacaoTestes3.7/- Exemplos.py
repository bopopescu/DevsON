# -*- coding: utf-8 -*-
import os

#Trabalahar com windows
#import win32ui
import easygui

import time
import log
import Variaveis

from login import LogarSistema

import Roteiro

from DAO import FuncoesBD


def main():
    FrontFarma = LogarSistema("FrontFarma")
    #FrontFarma.login()

    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    """
    win32ui.MessageBox(
                        '''
                        A vida e como uma camera.
                        Foque no que e importante,
                        capture bons momentos,
                        desenvolva a vida a partir de negativos. E,
                        se as coisas nao derem certo, tire outra foto.
                        '''
                        , "Tela Ms"
                       )
    """
    #os.system("pause")
    #raw_input("Pressione algo para continuar")

    #easygui.msgbox('modelo','Warning')

    #resultado =  easygui.enterbox('continuat','teste')

    resultado = FuncoesBD.ComDBMaster.Select("select concat(codprod,'|',nomeprod) as produto from produtos limit 10")

    prod = [item[0] for item in resultado]
    #prod.__str__()
    msg ="Relação de produtos?"
    title = "selecione o produto"

    choices = ["1 | TERMONAL","2 - Strawberry", "3 - Rocky Road"]
    ProdutoSeleciona = easygui.choicebox(msg, title, choices )


    sQuery = 'select * from produtos where codprod = %s' % (ProdutoSeleciona[:ProdutoSeleciona.find('|')].strip())


    produtos = FuncoesBD.ComDBMaster.FetchAllAssoc(sQuery)

    print(produtos[0]['NOMEPROD'])


    os.system("pause")
    FuncoesBD.PreparaConfig()

    log.EscreverLog('Timer ' + str(Variaveis.TAlertaL))
    time.sleep(Variaveis.TAlertaL)
    FrontFarma.Crtx()
    Variaveis.BaixaPrev     = 'S'
    Variaveis.BaixaEntrega  = 'S'

    #win32ui.MessageBox('Roteiro 1 passo 99','Tela Msg')

    log.EscreverLog('Timer ' + str(Variaveis.TFinal))
    Roteiro.Roteiro(1,99,1)
    Variaveis.BaixaPrev     = 'N'
    Variaveis.BaixaEntrega  = 'N'

    win32ui.MessageBox('Roteiro 1 Passo 2', 'Tela Msg')
    log.EscreverLog('Timer ' + str(Variaveis.TFinal))
    time.sleep(Variaveis.TFinal)
    Roteiro.Roteiro(1,1,1)

    win32ui.MessageBox('Roteiro 1 Passo 2', 'Tela Msg')
    log.EscreverLog('Timer ' + str(Variaveis.TFinal))
    time.sleep(Variaveis.TFinal)
    Roteiro.Roteiro(1,2,1)




if __name__ == '__main__':
    main()






