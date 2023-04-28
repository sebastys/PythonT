import os
import platform

info = platform.uname()#Windows
#info = os.uname()#Unix - Linux

print(info.system)#Windows
print(info.processor)#Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
print(info.node)#DESKTOP-BFR18FR


retorno = os.system('"C:/Program Files/Google/Chrome/Application/chrome.exe" https://www.lavozdegalicia.es/')
print(retorno)