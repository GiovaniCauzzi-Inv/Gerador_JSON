- [Overview](#overview)
  - [Progresso da criação das bibliotecas para gravar os diversos microcontroladores](#progresso-da-criação-das-bibliotecas-para-gravar-os-diversos-microcontroladores)
  - [Progresso da geração dos .json](#progresso-da-geração-dos-json)
- [Gerador de Configuradores .json](#gerador-de-configuradores-json)
  - [Geral](#geral)
  - [Relação da geração dos .json](#relação-da-geração-dos-json)

<br>

# Overview

Esse projeto se baseia em duas grandes ações:
- Criar o código (JS) para gravar os microcontroladores que atualmente o script não suporta;
- Gerar os arquivos .json para todos os produtos que ainda não estão implementados.


## Progresso da criação das bibliotecas para gravar os diversos microcontroladores

- [x] Renesas
- [x] STM8
- [ ] ESP32
- [x] Freescale
- [x] Microchip PIC
- [x] NXP
- [ ] ATMEL SAMD09D14A
- [ ] Texas Instrument MSP430 

## Progresso da geração dos .json

- [x] Renesas
- [x] STM8
- [ ] ESP32
- [x] Freescale
- [x] Microchip PIC
- [x] NXP
- [ ] ATMEL SAMD09D14A
- [ ] Texas Instrument MSP430 


# Gerador de Configuradores .json

## Geral 
O **script.py** foi desenvolvido para gerar automaticamente os arquivos configuradores (.json) do script de gravação a partir de um arquivo .CSV. Este arquivo foi extraído do banco de dados ao filtrar pela seguinte condição: **Produtos com firmware cadastrado**
<br>
Segue abaixo algumas amostras do arquivo base:

| Código | Descrição                                                                                         | Descrição Sintética  | Firmware                                                                    |   |
|--------|---------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------|---|
| 16385  | ACIONADOR ELETRONICO INV-136 13622 D2 (13695)                                                     | INV-13622 D2 (13695) | i:\documentos\softwares\atmel\samd09d14a\inv-136\136v22\13622_v1.00_pwm.hex |   |
| 10106  | PAINEL ELETRONICO DE MENSAGENS SLP INV-600 60001 (IHM)                                            | INV-60001 (IHM)      | i:\documentos\softwares\esp32\inv-600\inv600vi9a0a8.bat                     |   |
| 1377   | PLACA DE CIRCUITO IMPRESSO PARA CONTROLADOR DIGITAL DE TEMPERATURA COM TEMPORIZADOR INV-170 17001 | INV-17001            | i:\documentos\softwares\renesas\r5f52316adfm\inv-170\170v01\170v01.rpj      |   |
| 1416   | CONTROLADOR DIGITAL DE TEMPERATURA INV-78 7808/J                                                  | INV-7808/J           | i:\documentos\softwares\stm8\stm8s003f3\inv-78\78v08\78v08_1.70_j.stp       |   |

## Relação da geração dos .json
Nessa pasta há uma planilha **Relação_JSON_gerados.ods** com a mesma lista dos produtos do .CSV porém estão marcado com cores, indicando o progresso sobre a criação do .json:
![](./Imagens/Readme/relação.png)

- Branco: .json não gerado ainda
- Cinza: .json gerado
- Vermelho: não precisa gerar







