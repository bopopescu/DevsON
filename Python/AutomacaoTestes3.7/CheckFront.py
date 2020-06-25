import autoit
import os
import sys
import time
import log


def Checkfront():
    while True:
        time.sleep(3)
        log.EscreverLog('Mata checkfront')
        os.system("taskkill /F /im CHECKFRONT.exe")
        time.sleep(1)
        log.EscreverLog('Abre checkfront')
        autoit.run("c:\ourofarma\CHECKFRONT.exe")
