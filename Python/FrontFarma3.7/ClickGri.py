# -*- coding: utf-8 -*-
import autoit
import time
import log


def ClickGrid():
    log.EscreverLog('Tempo. : 3 segundos')
    time.sleep(3)
    log.EscreverLog('Clica no Centro da Tela')
    autoit.mouse_click("left", 500, 300, 1)
