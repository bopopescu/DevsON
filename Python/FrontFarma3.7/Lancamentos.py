# -*- coding: utf-8 -*-
import autoit
import os
import time

import Variaveis
import log
import Documento
import Desconto
import Venda
import VendaPromocao
import VendaAltw
import VendaAltwPromocao
import VendaLote

import F8
import Cliente
import DadosOrcamento
import Vendedor
import FinalizaVenda
import Entrega
import DadosEntrega
import TrocoEntrega
import FechaDadosEntrega

import Funcao
import Tempo
import Tecla
import Tela

def Lancamentos(Doc,Tipo,CodCli,Seq):
    log.EscreverLog('Rotina Lançamentos')
    Tempo.TelaAcao()

    # 1 - Sem entrega, sem desconto e sem arredondamento
    if (Seq == "1" or Seq == "0"):
        Funcao.ContadorVenda(Doc, Tipo, CodCli, 1)

        Documento.Documento(Doc)

        Venda.Venda()

        Tecla.F8LancamentoVenda()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)

        if CodCli == "0" and Doc == "ORC":
            Tempo.TelaFinalVenda()
            Tecla.Enter()
            DadosOrcamento.DadosOrcamento()
            
        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"


        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 2 - Sem entrega, sem desconto e com arredondamento
    if (Seq == "2" or Seq == "0") and Tipo == "V":
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 2 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)

        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)
        Desconto.Desconto("0","1,00")

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"
        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 3 - Sem entrega, com desconto e sem arredondamento
    if (Seq == "3" or Seq == "0") and Tipo == "V":
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 3 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)

        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)
        Desconto.Desconto("10", "0")

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 4 - Sem entrega, com desconto e com arredondamento
    if (Seq == "4" or Seq == "0") and Tipo == "V":
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 4 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)

        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)
        Desconto.Desconto("10", "1,00")

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"
        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 5 - Sem entrega, com promoção, Sem desconto e sem arredondamento
    if (Seq == "5" or Seq == "0"):
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 5 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)

        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.5")

    # 6 - Sem entrega, com promoção, Sem desconto e com arredondamento
    if (Seq == "6" or Seq == "0") and Tipo == "V":
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 6 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()
        
        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)
            
        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)
        Desconto.Desconto("0", "1,00")
        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"
        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 7 - Sem entrega, com promoção, Com desconto e sem arredondamento
    if (Seq == "7" or Seq == "0") and Tipo == "V":
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 7 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()
        
        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)
            
        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)
        Desconto.Desconto("10", "0")

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 8 - Sem entrega, com promoção, Com desconto e com arredondamento
    if (Seq == "8" or Seq == "0") and Tipo == "V":
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 8 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()
        
        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)

        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)
        Desconto.Desconto("10", "1,00")

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC":
            Rec = "S"
        else:
            Rec = "N"

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 9 Sem entrega, com alt+w, Sem desconto e sem arredondamento
    if (Seq == "9" or Seq == "0"):
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 9 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()
        
        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)
        
        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"
            
        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 10 Sem entrega, com alt+w, Sem desconto e com arredondamento
    if (Seq == "10" or Seq == "0") and Tipo == "V":
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 10 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()
        
        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)
        
        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)
        Desconto.Desconto("0", "1")

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 11 Sem entrega, com alt+w, Com desconto e sem arredondamento
    if (Seq == "11" or Seq == "0") and Tipo == "V":
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 11 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()
        
        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)
        
        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)
        Desconto.Desconto("10", "0")

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.11")

    # 12 Sem entrega, com alt+w, Com desconto e com arredondamento
    if (Seq == "12" or Seq == "0") and Tipo == "V":
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 12 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)  # 12')
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)

        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)
        Desconto.Desconto("10", "1")

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.12")

    # 13 Sem entrega,com promoção, com alt+w, Sem desconto e sem arredondamento
    if (Seq == "13" or Seq == "0"):
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 13 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)  # 13')
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)

        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

    # 14 Sem entrega,com promoção, com alt+w, Sem desconto e com arredondamento
    if (Seq == "14" or Seq == "0") and Tipo == "V":
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 14 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)

        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)
        Desconto.Desconto("0", "1")

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.14")

    # 15 Sem entrega,com promoção, com alt+w, Com desconto e sem arredondamento
    if (Seq == "15" or Seq == "0") and Tipo == "V":
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 15 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()
            time.sleep(Variaveis.TEnterL)
        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)
        Desconto.Desconto("10", "0")
        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"
        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.15")

    # 16 Sem entrega,com promoção, com alt+w, Com desconto e com arredondamento
    if (Seq == "16" or Seq == "0") and Tipo == "V":
        Variaveis.Nro += 1
        Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 16 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
        log.EscreverLog(Teste)
        Documento.Documento(Doc)
        Venda.Venda()
        F8.F8()

        if CodCli != "0":
            Cliente.Cliente(Tipo, CodCli)
        if CodCli == "0" and Doc == "ORC":
            time.sleep(Variaveis.TTela)
            time.sleep(Variaveis.TDig)
            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            DadosOrcamento.DadosOrcamento()

        time.sleep(Variaveis.TEnterL)
        if Variaveis.VendedorAutomatico == 'N':
            Vendedor.Vendedor(Doc, Tipo)
        Desconto.Desconto("10", "1")

        if (Tipo == "E" or Tipo == "V") and Variaveis.DocFiscal != "ORC" and Variaveis.DocFiscal != "PREV":
            Rec = "S"
        else:
            Rec = "N"

        FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.16")

    if (Doc != "ORC"):
        # 17 Com entrega, Sem desconto e Sem arredondamento
        if (Seq == "17" or Seq == "0"):
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 17 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()

            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            
            FechaDadosEntrega.FechaDadosEntrega()
            
            Rec = "N"

            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.17")

        # 18 Com entrega, sem desconto e com arredondamento
        if (Seq == "18" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 18 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 18')
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("0", "1")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.18")

        # 19 Com entrega, com desconto e sem arredondamento
        if (Seq == "19" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 19 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "0")

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

        # 20 Com entrega, com desconto e com arredondamento
        if (Seq == "20" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 20 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()

            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "1")

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

        # 21 Com entrega, com promoção, sem desconto e sem arredondamento
        if (Seq == "21" or Seq == "0"):
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 21 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()

            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

        # 22 Com entrega, com promoção, Sem desconto e com arredondamento
        if (Seq == "22" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 22 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("0", "1")

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

        # 23 Com entrega, com promoção, Com desconto e sem arredondamento
        if (Seq == "23" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 23 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()

            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "0")

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

        # 24 Com entrega, com promoção, Com desconto e com arredondamento
        if (Seq == "24" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 24 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 24')
            Venda.Venda()
            F8.F8()

            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "1")

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

        # 25 Com entrega, com alt+w, sem desconto e sem arredondamento
        if (Seq == "25" or Seq == "0"):
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 25 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.25")

        # 26 Com entrega, com alt+w, sem desconto e com arredondamento
        if (Seq == "26" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 26 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 26')

            Venda.Venda()
            F8.F8()

            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("0", "1")

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.26")

        # 27 Com entrega, com alt+w, Com desconto e sem arredondamento
        if (Seq == "27" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 27 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()

            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("1", "0")

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.27")

        # 28 Com entrega, com alt+w, Com desconto e com arredondamento
        if (Seq == "28" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 28 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 28')
            Venda.Venda()
            F8.F8()

            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "1")

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.28")

        # 29 Com entrega, com promoção com alt+w, sem desconto e sem arredondamento
        if (Seq == "29" or Seq == "0"):
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 29 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 29')
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

        # 30 Com entrega, com promoção com alt+w, sem desconto e com arredondamento
        if (Seq == "30" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 30 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("0", "1")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.30")

        # 31 Com entrega, com promoção com alt+w, Com desconto e sem arredondamento
        if (Seq == "31" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 31 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 31')
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("1", "0")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.31")

        # 32 Com entrega, com promoção com alt+w, Com desconto e com arredondamento
        if (Seq == "32" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 32 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "1")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)

        # 33 Com entrega, com troco, sem desconto e sem arredondamento
        if (Seq == "33" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 33 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 33')
            Venda.Venda()
            F8.F8()

            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            TrocoEntrega.TrocoEntrega("1100")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.33")

        # 34 Com Entrega.Entrega, com troco, sem desconto e com arredondamento
        if (Seq == "34" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 34 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("0", "1")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.34")

        # 35 Com Entrega.Entrega, com troco,  com desconto e sem arredondamento
        if (Seq == "35" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 35 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "0")

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.35")

        # 36 Com Entrega.Entrega, com troco,  com desconto e com arredondamento
        if (Seq == "36" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 36 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 36')
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "1")

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.36")

        # 37 Com Entrega.Entrega, com troco, com promoção, sem desconto e sem arredondamento
        if (Seq == "37" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 37 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()

            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()

            Rec = "N"

            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.37")

        # 38 Com Entrega.Entrega, com troco,  com promoção, sem desconto e com arredondamento
        if (Seq == "38" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 38 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 38')
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("0", "1")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.38")

        # 39 Com Entrega.Entrega, com troco,  com promoção, Com desconto e sem arredondamento
        if (Seq == "39" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 39 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "0")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.39")

        # 40 Com Entrega.Entrega, com troco,  com promoção, Com desconto e com arredondamento
        if (Seq == "40" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 40 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 40')

            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "1")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.40")

        # 41 Com Entrega.Entrega, com troco,  com alt+w, sem desconto e sem arredondamento
        if (Seq == "41" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 41 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 41')

            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.41")

        # 42 Com Entrega.Entrega, com troco,  com alt+w, sem desconto e com arredondamento
        if (Seq == "42" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 42 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 42')
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("0", "1")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.42")

        # 43 Com Entrega.Entrega, com troco,  com alt+w, Com desconto e sem arredondamento
        if (Seq == "43" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 43 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 43')
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "0")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.43")

        # 44 Com Entrega.Entrega, com troco,  com alt+w, sem desconto e sem arredondamento
        if (Seq == "44" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 44 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 44')
            Venda.Venda()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "1")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.44")

        # 45 Com Entrega.Entrega, com troco,  com promoção com alt+w, sem desconto e sem arredondamento
        if (Seq == "45" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 45 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 45')
            VendaAltwPromocao.VendaAltwPromocao()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.45")

        # 46 Com Entrega.Entrega, com troco,  com promoção com alt+w, sem desconto e com arredondamento
        if (Seq == "46" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 46 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 46')
            VendaAltwPromocao.VendaAltwPromocao()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("0", "1")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.46")

        # 47 Com Entrega.Entrega, com troco,  com promoção com alt+w, Com desconto e sem arredondamento
        if (Seq == "47" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 47 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)  # 47')
            VendaAltwPromocao.VendaAltwPromocao()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "0")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.47")

        # 48 Com Entrega.Entrega, com troco,  com promoção com alt+w, sem desconto e sem arredondamento
        if (Seq == "48" or Seq == "0") and Tipo == "V":
            Variaveis.Nro += 1
            Teste = "Venda: " + str(Variaveis.Nro) + " Teste Seq: 48 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            VendaAltwPromocao.VendaAltwPromocao()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)
            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)
            Desconto.Desconto("10", "1")
            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()
            TrocoEntrega.TrocoEntrega("1200")
            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)  # "1.1.1.48")


        # Teste lotes Refazer depois



        # 1.1.1.49 Com Entrega.Entrega, Sem desconto e Sem arredondamento
        if (Seq == "49" or Seq == "0"):
            Variaveis.Nro += 1
            Teste = "Nro: " + str(Variaveis.Nro) + " Teste Seq: 49 " + "Doc: " + str(Doc) + " Cliente: " + str(CodCli) + " Tipo Venda: " + str(Tipo)
            log.EscreverLog(Teste)
            Documento.Documento(Doc)
            VendaLote.VendaLote()
            F8.F8()
            if CodCli != "0":
                Cliente.Cliente(Tipo, CodCli)

            if Variaveis.VendedorAutomatico == 'N':
                Vendedor.Vendedor(Doc, Tipo)

            if CodCli != "0":
                Entrega.Entrega()
            else:
                DadosEntrega.DadosEntrega()

            FechaDadosEntrega.FechaDadosEntrega()
            Rec = "N"
            FinalizaVenda.FinalizaVenda(Doc, Tipo, Rec)