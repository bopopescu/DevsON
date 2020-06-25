# -*- coding: utf-8 -*-

import autoit
import time
import log
import Tempo
import Variaveis
import Alerta
import Tela
import Tecla




TTecla  = (35.0/100.0)


def ClickGrid():
    Tempo.Click()
    log.EscreverLog('Clica no Centro da Tela')
    autoit.mouse_click("left", 500, 300, 1)


def ClickFinalVenda():
    Tempo.ClickFinalVenda()
    log.EscreverLog('Clica no Centro da Tela')
    autoit.mouse_click("left", 850, 130, 1)


def Crtx():
    Tempo.TelaAcao()
    log.EscreverLog('Entra Funçao Crt X')
    log.EscreverLog('Crt X')
    autoit.send("{CTRLDOWN}x{CTRLUP}")
    Tela.TelaAlertaCrt('Tela Vazia','Sem Alerta')
    log.EscreverLog('Sai Funçao Crt X')



def LimpaTexto():
    Tempo.Dig()
    log.EscreverLog("{HOME}")
    autoit.send("{HOME}")
    Tempo.Dig()
    log.EscreverLog("{SHIFTDOWN}{END}{SHIFTUP}{BACKSPACE}")
    autoit.send("{SHIFTDOWN}{END}{SHIFTUP}{BACKSPACE}")



def F8FinalVenda():
    Tecla.ClickFinalVenda()
    Tempo.F8FinalVenda()
    log.EscreverLog('F8 Final Venda')
    autoit.send("{F8}")


def CrtE():
    Tempo.TeclaAcao()
    log.EscreverLog('Gerenciador De Notas Fiscais Eletronicas')
    autoit.send("{CTRLDOWN}e{CTRLUP}")

def CrtR():
    Tempo.TeclaAcao()
    log.EscreverLog('Tratamento Rejeicao')
    autoit.send("{CTRLDOWN}r{CTRLUP}")


def F8LancamentoVenda():
    log.EscreverLog('Função chama Final Venda(F8LancamentoVenda)')
    Tempo.F8TelaLancamento()
    log.EscreverLog('F8')
    autoit.send("{F8}")
    Tempo.DigProd()
    if Variaveis.DocFiscal == "NFCE":
       Tela.AlertaTelaVenda('Alerta Nfce em Homologação','Não teve Alerta NFCE')
    log.EscreverLog('Sai Função F8')
    if Variaveis.DocFiscal == "NFE":
       Tela.AlertaTelaVenda('Alerta NFE em Homologação','Não teve Alerta NFE')
    Tela.FinalVenda()
    log.EscreverLog('Sai Função F8')
    Tempo.TelaFinalVenda()





def F8():
    Tempo.TeclaAcao()
    log.EscreverLog('F8')
    autoit.send("{F8}")


def F10():
    Tempo.TeclaAcao()
    log.EscreverLog('F10')
    autoit.send("{F10}")


def Esc():
    Tempo.Esc()
    log.EscreverLog("{ESC}")
    autoit.send("{ESC}")


def EnterProduto():
    Tempo.EnterProduto()
    log.EscreverLog('ENTER')
    autoit.send("{ENTER}")


def Enter():
    Tempo.Enter()
    log.EscreverLog('ENTER')
    autoit.send("{ENTER}")




def TempoR():
    log.EscreverLog('Tempo. ' + str(TTecla) + ' segundos')
    time.sleep(TTecla)

def TempoM():
    log.EscreverLog('Tempo. ' + str(3) + ' segundos')
    time.sleep(2)

def TempoL():
    log.EscreverLog('Tempo. ' + str(6) + ' segundos')
    time.sleep(6)

def TempoLL():
    log.EscreverLog('Tempo. ' + str(6) + ' segundos')
    time.sleep(10)

def ContadorVenda(Doc, Tipo, CodCli, Seq):
    Variaveis.Nro += 1
    Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: "+ str(Seq) + " Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
    log.EscreverLog(Teste)
