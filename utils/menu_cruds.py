from utils.utils_geral import *
from utils.utils_menus import *
from cruds.hospital import insere_hospital, altera_hospital, menu_relatorios_hospital, exclui_hospital
from cruds.medico import insere_medico, altera_medico, menu_relatorios_medico, exclui_medico
from cruds.enfermeiro import insere_enfermeiro, altera_enfermeiro, menu_relatorios_enfermeiro, exclui_enfermeiro
from cruds.paciente import insere_paciente, altera_paciente, menu_relatorios_paciente, exclui_paciente

def crud_hospital():
    quant_opcoes = 5
    valido = True
    while True:
        limpa_tela()
        
        imprime_menu_crud("Hospital")
        
        valido = checa_erro(valido, 'Opcao Invalida!')
            
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            insere_hospital()
        elif opcao == 2:
            altera_hospital()
        elif opcao == 3:
            menu_relatorios_hospital()
        elif opcao == 4:
            exclui_hospital()
        elif opcao == 5:
            break
        else:
            valido = False

def crud_medico():
    quant_opcoes = 5
    valido = True
    while True:
        limpa_tela()
        
        imprime_menu_crud("Medico")
        
        valido = checa_erro(valido, 'Opcao Invalida!')
            
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            insere_medico()
        elif opcao == 2:
            altera_medico()
        elif opcao == 3:
            menu_relatorios_medico()
        elif opcao == 4:
            exclui_medico()
        elif opcao == 5:
            break
        else:
            valido = False

def crud_enfermeiro():
    quant_opcoes = 5
    valido = True
    while True:
        limpa_tela()
        
        imprime_menu_crud("Hospital")
        
        valido = checa_erro(valido, 'Opcao Invalida!')
            
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            insere_enfermeiro()
        elif opcao == 2:
            altera_enfermeiro()
        elif opcao == 3:
            menu_relatorios_enfermeiro()
        elif opcao == 4:
            exclui_enfermeiro()
        elif opcao == 5:
            break
        else:
            valido = False

def crud_paciente():
    quant_opcoes = 5
    valido = True
    while True:
        limpa_tela()
        
        imprime_menu_crud("Hospital")
        
        valido = checa_erro(valido, 'Opcao Invalida!')
            
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            insere_paciente()
        elif opcao == 2:
            altera_paciente()
        elif opcao == 3:
            menu_relatorios_paciente()
        elif opcao == 4:
            exclui_paciente()
        elif opcao == 5:
            break
        else:
            valido = False