# Gerador de Configuradores .json

Esse script foi desenvolvido para gerar automaticamente os arquivos configuradores (.json) do script de gravação a partir de um arquivo .CSV. Este arquivo foi extraído do banco de dados ao filtrar pela seguinte condição: **Produtos com firmware cadastrado**
Segue abaixo algumas amostras do arquivo base:

| Código | Descrição                                                                                         | Descrição Sintética  | Firmware                                                                    |   |
|--------|---------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------|---|
| 16385  | ACIONADOR ELETRONICO INV-136 13622 D2 (13695)                                                     | INV-13622 D2 (13695) | i:\documentos\softwares\atmel\samd09d14a\inv-136\136v22\13622_v1.00_pwm.hex |   |
| 10106  | PAINEL ELETRONICO DE MENSAGENS SLP INV-600 60001 (IHM)                                            | INV-60001 (IHM)      | i:\documentos\softwares\esp32\inv-600\inv600vi9a0a8.bat                     |   |
| 1377   | PLACA DE CIRCUITO IMPRESSO PARA CONTROLADOR DIGITAL DE TEMPERATURA COM TEMPORIZADOR INV-170 17001 | INV-17001            | i:\documentos\softwares\renesas\r5f52316adfm\inv-170\170v01\170v01.rpj      |   |
| 1416   | CONTROLADOR DIGITAL DE TEMPERATURA INV-78 7808/J                                                  | INV-7808/J           | i:\documentos\softwares\stm8\stm8s003f3\inv-78\78v08\78v08_1.70_j.stp       |   |

