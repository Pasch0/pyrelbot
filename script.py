#!/usr/bin/python3
import os

# Seleção de cidades
print("\n************************"
      "\n*       Cidades        *"
      "\n* 1 = NOF      2 = TER *"
      "\n* 3 = CAM      4 = ROS *"
      "\n* 5 = MAC      6 = CBU *"
      "\n* 7 = BJD      8 = CPB *"
      "\n* 9 = MRC     10 = NIT *"
      "\n* 11 = QUI    12 = SUM *"
      "\n************************\n")
cidade = input('Digite a cidade: ')


# Seleção de bairros em Nova Friburgo
if cidade == '1':
    citycode = 'NOF'
    print("\n************************"
          "\n*        Áreas         *"
          "\n* 1 = AMP      2 = AVN *"
          "\n* 3 = BEV      4 = BRA *"
          "\n* 5 = CAM      6 = CAS *"
          "\n* 7 = CDA      8 = CEN *"
          "\n* 9 = CHA     10 = COE *"
          "\n* 11 = CON    12 = CPA *"
          "\n* 13 = DBS    14 = DPE *"
          "\n* 15 = FAV    16 = GOS *"
          "\n* 17 = JAD    18 = JCA *"
          "\n* 19 = JOP    20 = LAG *"
          "\n* 21 = LUM    22 = MAR *"
          "\n* 23 = MDC    24 = MRY *"
          "\n* 25 = NBR    26 = NSU *"
          "\n* 27 = OLA    28 = PBE *"
          "\n* 29 = PRF    30 = PSA *"
          "\n* 31 = RBT    32 = SBE *"
          "\n* 33 = SGE    34 = SJO *"
          "\n* 35 = SPE    36 = STU *"
          "\n* 37 = VAM    38 = VAR *"
          "\n* 39 = VIL    40 = VPE *"
          "\n* 41 = VPI    42 = WAL *"
          "\n*       43 = YPU       *"
          "\n************************\n")

# Seleção de bairros em Teresópolis
if cidade == '2':
    citycode = 'TER'
    print("\n************************"
          "\n*        Áreas         *"
          "\n* 44 = SPE    45 = TIJ *"
          "\n* 46 = VAR    47 = BSC *"
          "\n************************\n")

# Seleção de bairros em Campos
if cidade == '3':
    citycode = 'CAM'
    print("\n******************************"
          "\n*           Áreas            *"
          "\n* 48 = CEN001    49 = CEN008 *"
          "\n* 50 = FLA01      51 = FST01 *"
          "\n* 52 = HRT01      53 = HRT02 *"
          "\n* 54 = IMP01      55 = IMP02 *"
          "\n* 56 = IMP03      57 = IMP04 *"
          "\n* 58 = IMP05      59 = JCK03 *"
          "\n* 60 = JOC01      61 = JOC02 *"
          "\n* 62 = NJOC01    63 = NJOC02 *"
          "\n* 64 = NJOC03     65 = PEN01 *"
          "\n* 66 = PEN04      67 = PEN05 *"
          "\n* 68 = PEN08      69 = PQT01 *"
          "\n* 70 = PQT02      71 = VIS01 *"
          "\n******************************\n")

# Seleção de bairros em Rio das Ostras
if cidade == '4':
    citycode = 'ROS'
    print("\n************************"
          "\n*        Áreas         *"
          "\n* 72 = JML    73 = LIB *"
          "\n* 74 = NSP    75 = OPE *"
          "\n*       76 = REC       *"
          "\n************************\n")

# Seleção de bairros em Macaé
if cidade == '5':
    citycode = 'MAC'
    print("\n************************"
          "\n*        Áreas         *"
          "\n*     77 = CENT01      *"
          "\n************************\n")

# Seleção de bairros em Casimiro de Abreu
if cidade == '6':
    citycode = 'CBU'
    print("\n************************"
          "\n*        Áreas         *"
          "\n*      78 = CEN01      *"
          "\n************************\n")

# Seleção de bairros em Bom Jardim
if cidade == '7':
    citycode = 'BJD'
    print("\n************************"
          "\n*        Áreas         *"
          "\n*      79 = CEN01      *"
          "\n************************\n")

# Seleção de bairros em Carapebus
if cidade == '8':
    citycode = 'CPB'
    print("\n************************"
          "\n*        Áreas         *"
          "\n*      80 = CEN01      *"
          "\n************************\n")

# Seleção de bairros em Maricá
if cidade == '9':
    citycode = 'MRC'
    print("\n************************"
          "\n*        Áreas         *"
          "\n*      81 = CEN01      *"
          "\n************************\n")

# Seleção de bairros em Niterói
if cidade == '10':
    citycode = 'NIT'
    print("\n****************************"
          "\n*          Áreas           *"
          "\n* 82 = AVC01    83 = AVC02 *"
          "\n* 84 = EMA01    85 = MAR01 *"
          "\n* 86 = PIR01    87 = PIR03 *"
          "\n* 88 = UBA01    89 = UBA02 *"
          "\n*        90 = VAM01        *"
          "\n****************************\n")

# Seleção de bairros em Quissamã
if cidade == '11':
    citycode = 'QUI'
    print("\n************************"
          "\n*        Áreas         *"
          "\n*      91 = CEN01      *"
          "\n************************\n")

# Seleção de bairros em Sumidouro
if cidade == '12':
    citycode = 'SUM'
    print("\n************************"
          "\n*        Áreas         *"
          "\n*      92 = CEN01      *"
          "\n************************\n")


area = input('Digite a área: ')

rua = input('Digite a rua: ')


# Definição para cada área de NOF
if area == '1':
    areacode = 'AMP036'
elif area == '2':
    areacode = 'AVN046'
elif area == '3':
    areacode = 'BEV010'
elif area == '4':
    areacode = 'BRA028'
elif area == '5':
    areacode = 'CAM026'
elif area == '6':
    areacode = 'CAS013'
elif area == '7':
    areacode = 'CDA041'
elif area == '8':
    areacode = 'CEN'
elif area == '9':
    areacode = 'CHA024'
elif area == '10':
    areacode = 'COE'
elif area == '11':
    areacode = 'CON'
elif area == '12':
    areacode = 'CPA019'
elif area == '13':
    areacode = 'DBS040'
elif area == '14':
    areacode = 'DPE023'
elif area == '15':
    areacode = 'FAV01'
elif area == '16':
    areacode = 'GOS037'
elif area == '17':
    areacode = 'JAD01'
elif area == '18':
    areacode = 'JCA022'
elif area == '19':
    areacode = 'JOP018'
elif area == '20':
    areacode = 'LAG020'
elif area == '21':
    areacode = 'LUM01'
elif area == '22':
    areacode = 'MAR031'
elif area == '23':
    areacode = 'MDC074'
elif area == '24':
    areacode = 'MRY038'
elif area == '25':
    areacode = 'NBR043'
elif area == '26':
    areacode = 'NSU035'
elif area == '27':
    areacode = 'OLA'
elif area == '28':
    areacode = 'PBE01'
elif area == '29':
    areacode = 'PFE01'
elif area == '30':
    areacode = 'PRF027'
elif area == '31':
    areacode = 'PSA033'
elif area == '32':
    areacode = 'SBE044'
elif area == '33':
    areacode = 'SGE045'
elif area == '34':
    areacode = 'SJO021'
elif area == '35':
    areacode = 'SPE01'
elif area == '36':
    areacode = 'STU039'
elif area == '37':
    areacode = 'VAM017'
elif area == '38':
    areacode = 'VAR034'
elif area == '39':
    areacode = 'VIL025'
elif area == '40':
    areacode = 'VPE01'
elif area == '41':
    areacode = 'VPI016'
elif area == '42':
    areacode = 'WAL01'
elif area == '43':
    areacode = 'YPU032'


# Definição para cada área de TER
if area == '44':
    areacode = 'SPE01'
elif area == '45':
    areacode = 'TIJ01'
elif area == '46':
    areacode = 'VAR01'
elif area == '47':
    areacode = 'BSC01'


# Definição para cada área de CAM
if area == '48':
    areacode = 'CEN001'

elif area == '49':
    areacode = 'CEN008'

elif area == '50':
    areacode = 'FLA01'

elif area == '51':
    areacode = 'FST01'

elif area == '52':
    areacode = 'HRT01'

elif area == '53':
    areacode = 'HRT02'

elif area == '54':
    areacode = 'IMP01'

elif area == '55':
    areacode = 'IMP02'

elif area == '56':
    areacode = 'IMP03'

elif area == '57':
    areacode = 'IMP04'

elif area == '58':
    areacode = 'IMP05'

elif area == '59':
    areacode = 'JCK03'

elif area == '60':
    areacode = 'JOC01'

elif area == '61':
    areacode = 'JOC02'

elif area == '62':
    areacode = 'NJOC01'

elif area == '63':
    areacode = 'NJOC02'

elif area == '64':
    areacode = 'NJOC03'

elif area == '65':
    areacode = 'PEN01'

elif area == '66':
    areacode = 'PEN04'

elif area == '67':
    areacode = 'PEN05'

elif area == '68':
    areacode = 'PEN08'

elif area == '69':
    areacode = 'PQT01'

elif area == '70':
    areacode = 'PQT02'

elif area == '71':
    areacode = 'VIS01'


# Definição para cada área de ROS
if area == '72':
    areacode = 'JML006'
if area == '73':
    areacode = 'LIB003'
if area == '74':
    areacode = 'NSP004'
if area == '75':
    areacode = 'OPE002'
if area == '76':
    areacode = 'REC001'


# Definição para cada área de MAC
if area == '77':
    areacode = 'CENT01'


# Definição para cada área de CBU
if area == '78':
    areacode = 'CEN001'


# Definição para cada área de BJD
if area == '79':
    areacode = 'CEN001'


# Definição para cada área de CPB
if area == '80':
    areacode = 'CEN001'


# Definição para cada área de MRC
if area == '81':
    areacode = 'CEN001'


# Definição para cada área de NIT
if area == '82':
    areacode = 'AVC01'
if area == '83':
    areacode = 'AVC02'
if area == '84':
    areacode = 'EMA01'
if area == '85':
    areacode = 'MAR01'
if area == '86':
    areacode = 'PIR01'
if area == '87':
    areacode = 'PIR03'
if area == '88':
    areacode = 'UBA01'
if area == '89':
    areacode = 'UBA02'
if area == '90':
    areacode = 'VAM01'

# Definição para cada área de QUI
if area == '91':
    areacode = 'CEN001'


# Definição para cada área de SUM
if area == '92':
    areacode = 'CEN001'



# Seleção de ocorrência
print("\n*************************"
      "\n*      Ocorrências      *"
      "\n*    1 = Inoperante     *"
      "\n*   2 = Intermitente    *"
      "\n*  3 = Perda/Latência   *"
      "\n*************************\n")
ocorrencia = input('Informe a ocorrência: ')
if ocorrencia == '1':
    defocorrencia = 'inoperante'
if ocorrencia == '2':
    defocorrencia = 'intermitente'
if ocorrencia == '3':
    defocorrencia = 'apresenta perdas/latência alta'

# Seleção de segmento
segmento = input('A partir da célula: ')

# Seleção de monitoramento
#print("\n*************************"
#      "\n*        1 = Sim        *"
#      "\n*        2 = Não        *"
#      "\n*************************\n")

# Caso afete monitoramento
#monitoramento = input('Afeta monitoramento? ')
#if monitoramento == '1':
ponto = input('Qual o monitoramento afetado? ')

# Caso não afete monitoramento
#else:
#    ponto = '0'

# Saídas do monitoramento para slack/viki
if ponto >= '1':
    pontoafetado = "Afeta monitoramento na célula "
    argponto = pontoafetado, ponto
    pontoslack = ponto

else:
    pontoafetado = "Não afeta monitoramento"
    pontoafetado2 = "Não afeta monitoramento."


# Exemplo de saída para viki
print("\n Rede", defocorrencia, "a partir da célula", segmento, "\n", pontoafetado, ponto, "\n", rua,
      "\n Favor verificar.")

# Adicionar protocolo de chamado no viki
protocolo = input('Digite o Protocolo #')

# Saída para o slack
# slack = '\n [' + citycode + '-' + areacode + '-' + ponto + '] Rede ' + defocorrencia + " a partir da célula " + \
# segmento + ' ' + rua + '.' + '\n' + pontoafetado + ponto + '. ' + 'Protocolo #' + protocolo


# Exemplo de saída para slack
slack = f'\n*[{citycode}-{areacode}-{ponto}]* Rede {defocorrencia} a partir da célula {segmento}, {rua}. \n{pontoafetado} {ponto}. Protocolo *#{protocolo}*'
print(slack)

# POST de saída para slack
curl = "curl -X POST -H Content-type: application/json --data '{\"text\":\"" + slack + "\"}' https://hooks.slack.com/services/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"
os.system(curl)
