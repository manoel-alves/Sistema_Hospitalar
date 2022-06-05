from utils.geral import *
from utils.obtencoes import obter_opcao
from cruds.hospital import insere_hospital, altera_hospital, menu_relatorios_hospital, exclui_hospital
from cruds.medico import insere_medico, altera_medico, menu_relatorios_medico, exclui_medico
from cruds.enfermeira import insere_enfermeira, altera_enfermeira, menu_relatorios_enfermeira, exclui_enfermeira
from cruds.paciente import insere_paciente, altera_paciente, menu_relatorios_paciente, exclui_paciente

def crud_hospital():
    quant_opcoes = 4
    valido = True
    while True:
        limpa_tela()
        
        imprime_menu_crud("Hospital")
        
        if not valido:
            mensagem_input_invalido('Opcao Invalida!')
            valido = True
            
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            insere_hospital()
        elif opcao == 2:
            altera_hospital()
        elif opcao == 3:
            menu_relatorios_hospital()
        elif opcao == 4:
            exclui_hospital()
        elif opcao == 0:
            break
        else:
            valido = False

def crud_medico():
    quant_opcoes = 4
    valido = True
    while True:
        limpa_tela()
        
        imprime_menu_crud("Medico")
        
        if not valido:
            mensagem_input_invalido('Opcao Invalida!')
            valido = True
            
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            insere_medico()
        elif opcao == 2:
            altera_medico()
        elif opcao == 3:
            menu_relatorios_medico()
        elif opcao == 4:
            exclui_medico()
        elif opcao == 0:
            break
        else:
            valido = False

def crud_enfermeira():
    quant_opcoes = 4
    valido = True
    while True:
        limpa_tela()
        
        imprime_menu_crud("Enfermeira")
        
        if not valido:
            mensagem_input_invalido('Opcao Invalida!')
            valido = True
            
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            insere_enfermeira()
        elif opcao == 2:
            altera_enfermeira()
        elif opcao == 3:
            menu_relatorios_enfermeira()
        elif opcao == 4:
            exclui_enfermeira()
        elif opcao == 0:
            break
        else:
            valido = False

def crud_paciente():
    quant_opcoes = 4
    valido = True
    while True:
        limpa_tela()
        
        imprime_menu_crud("Paciente")
        
        if not valido:
            mensagem_input_invalido('Opcao Invalida!')
            valido = True
            
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            insere_paciente()
        elif opcao == 2:
            altera_paciente()
        elif opcao == 3:
            menu_relatorios_paciente()
        elif opcao == 4:
            exclui_paciente()
        elif opcao == 0:
            break
        else:
            valido = False
            
def imprime_menu_crud(titulo: str):
    imprime_titulo(f'CRUD {titulo}')
    print('1 - Inserir')
    print('2 - Alterar')
    print('3 - Relatorios')
    print('4 - Excluir')
    imprime_linha()
    print('0 - Voltar')
    imprime_linha()