import csv
import requests
from os.path import dirname, realpath, isfile
from json import dump
import json
import time

class JsonManager:
    def __init__(self):
        self.path = dirname(realpath(__file__)) + '/'

    def create_json(self, file, dataInput):
        path_data_json = self.path + file

        if not isfile(path_data_json):
            with open(path_data_json, 'w') as f:
                dump(dataInput, f, indent=2, separators=(',', ': '))
            return True
        else:
            return False

def str_to_raw(s):
    raw_map = {8: r'\b', 7: r'\a', 12: r'\f',
               10: r'\n', 13: r'\r', 9: r'\t', 11: r'\v'}
    return r''.join(i if ord(i) > 32 else raw_map.get(ord(i), i) for i in s)

contagemGeral = 0
contagemRenesas = 0
contagemESP32 = 0
contagemStm8 = 0
contagemStm8s003f3 = 0
contagemStm8af52a = 0
contagemStm8af52a8tdx = 0
contagemFreescale = 0
contagemMicrochip = 0

#start = time.time()

with open('produtos_sintetico_barra.csv') as arquivo:
    leituraArquivo = csv.reader(arquivo, delimiter=',')

    for linha in leituraArquivo:
        contagemGeral += 1
        codigo = linha[0]
        descricaoSintetica = linha[2]
        firmware = linha[3].lower()

        if firmware.find("renesas") > 0:  # ____________________RENESAS____________________
            contagemRenesas += 1
            dadosJsonObj = {
                "Produto": ""+str(descricaoSintetica)+"",
                "CodProduto": ""+str(codigo)+"",
                "Gravador": "Renesas E2 Lite",
                "Img_Gravador": "Renesas E2 Lite.png",
                "BsGravacao": "NA",
                "SupGravacao": "NA",
                "Rastreamento": "true",
                "Tst_State": {
                    "1": "SetupInicial",
                    "2": "ScamGravador",
                    "3": "StartRastreamento",
                    "4": "GravaFirmware"
                }
            }
            # print(str(dadosJsonObj))
            # print(dadosJsonObj['CodProduto'])
            if __name__ == '__main__':
                jmanager = JsonManager()
                jmanager.create_json('JSON_Gerados/renesas/'+codigo+'.json', dadosJsonObj)

        if firmware.find("esp32") > 0:  # ____________________ESP32____________________
            contagemESP32 += 1
            dadosJsonObj = {
                "Produto": ""+str(descricaoSintetica)+"",
                "CodProduto": ""+str(codigo)+"",
                "Gravador": "ESP32",
                "Img_Gravador": "FTDI.png",
                "BsGravacao": "NA",
                "SupGravacao": "NA",
                "Rastreamento": "true",
                "Tst_State": {
                    "1": "SetupInicial",
                    "2": "ScamGravador",
                    "3": "StartRastreamento",
                    "4": "GravaFirmware"
                }
            }
            # print(str(dadosJsonObj))
            # print(dadosJsonObj['CodProduto'])
            if __name__ == '__main__':
                jmanager = JsonManager()
                jmanager.create_json('JSON_Gerados/ESP32/'+codigo+'.json', dadosJsonObj)

        if firmware.find("stm8") > 0:  # ____________________STM8____________________
            contagemStm8 += 1
            if firmware.find("stm8s003f3") > 0:
                contagemStm8s003f3 += 1
                dadosJsonObj = {
                    "Produto": ""+str(descricaoSintetica)+"",
                    "CodProduto": ""+str(codigo)+"",
                    "Gravador": "ST-LINK/V2",
                    "Img_Gravador": "ST Link V2 ISOL.png",
                    "Rastreamento": "true",
                    "BsGravacao": "NA",
                    "SupGravacao": "NA",
                    "Micro": "STM8S003F3",
                    "Tst_State": {
                        "1": "SetupInicial",
                        "2": "ScamGravador",
                        "3": "StartRastreamento",
                        "4": "GravaFirmware"
                    }
                }
                # print(str(dadosJsonObj))
                # print(dadosJsonObj['CodProduto'])
                if __name__ == '__main__':
                    jmanager = JsonManager()
                    jmanager.create_json(
                        'JSON_Gerados/STM8S003F3/'+codigo+'.json', dadosJsonObj)

            # 134m2 = stm8af52a8tdx
            if firmware.find("stm8af52a") > 0 or firmware.find("stm8\134m2") > 0:
                contagemStm8af52a += 1
                dadosJsonObj = {
                    "Produto": ""+str(descricaoSintetica)+"",
                    "CodProduto": ""+str(codigo)+"",
                    "Gravador": "ST-LINK/V2",
                    "Img_Gravador": "ST Link V2 ISOL.png",
                    "Rastreamento": "true",
                    "BsGravacao": "NA",
                    "SupGravacao": "NA",
                    "Micro": "STM8AF52A",
                    "Tst_State": {
                        "1": "SetupInicial",
                        "2": "ScamGravador",
                        "3": "StartRastreamento",
                        "4": "GravaFirmware"
                    }
                }
                # print(str(dadosJsonObj))
                # print(dadosJsonObj['CodProduto'])
                if __name__ == '__main__':
                    jmanager = JsonManager()
                    jmanager.create_json('JSON_Gerados/STM8AF52A/'+codigo+'.json', dadosJsonObj)
            
        if firmware.find("freescale") > 0 or firmware.find("nxp") > 0 or firmware.find("daq") > 0: # ____________________FREESCALE____________________
            contagemFreescale += 1
            dadosJsonObj = {
                "Produto": ""+str(descricaoSintetica)+"",
                "CodProduto": ""+str(codigo)+"",
                "Gravador": "Cyclone",
                "Img_Gravador": "Cyclone.png",
                "BsGravacao": "NA",
                "SupGravacao": "NA",
                "Rastreamento": "true",
                "Tst_State": {
                    "1": "SetupInicial",
                    "2": "ScamGravador",
                    "3": "StartRastreamento",
                    "4": "GravaFirmware"
                }
            }
            # print(str(dadosJsonObj))
            # print(dadosJsonObj['CodProduto'])
            if __name__ == '__main__':
                jmanager = JsonManager()
                jmanager.create_json('JSON_Gerados/Freescale/'+codigo+'.json', dadosJsonObj)
        
        if firmware.find("microchip") > 0:# ____________________MICROCHIP____________________
            contagemMicrochip += 1
            micro = firmware.split("/")
            micro = micro[4].upper()
            dadosJsonObj = {
                "Produto": ""+str(descricaoSintetica)+"",
                "CodProduto": ""+str(codigo)+"",
                "Gravador": "MPLAB PM3",
                "Img_Gravador": "MPLAB_PM3.png",
                "BsGravacao": "NA",
                "SupGravacao": "NA",
                "Rastreamento": "true",
                "Pic": ""+str(micro)+"",
                "Tst_State": {
                    "1": "SetupInicial",
                    "2": "ScamGravador",
                    "3": "StartRastreamento",
                    "4": "GravaFirmware"
                }
            }
            # print(str(dadosJsonObj))
            # print(dadosJsonObj['CodProduto'])
            if __name__ == '__main__':
                jmanager = JsonManager()
                jmanager.create_json('JSON_Gerados/Microchip/'+codigo+'.json', dadosJsonObj)


print("Contagem geral = " + str(contagemGeral))
print("Contagem Renesas = " + str(contagemRenesas))
print("Contagem ESP32 = " + str(contagemESP32))
print("Contagem STM8 = " + str(contagemStm8))
print("Contagem STM8S003F3 = " + str(contagemStm8s003f3))
print("Contagem Stm8af52a = " + str(contagemStm8af52a))
print("Contagem Freescale = " + str(contagemFreescale))
print("Contagem Microchip = " + str(contagemMicrochip))
#nd = time.time()
#print("Elapsed time: " + str(end - start) + "s")