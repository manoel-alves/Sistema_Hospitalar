from utils.db_operacoes import inicializa_database
from utils.utils_geral import *
from utils.utils_menus import *
from utils.menu_cruds import *

def main():
    inicializa_database()

    quant_opcoes = 4
    valido = True
    while True:
        limpa_tela()
        
        imprime_menu_principal()
        
        if not valido:
            mensagem_input_invalido('Opcao Invalida!')
            valido = True
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            crud_hospital()
        elif opcao == 2:
            crud_medico()
        elif opcao == 3:
            crud_enfermeiro()
        elif opcao == 4:
            crud_paciente()
        elif opcao == 0:
            break
        else:
            valido = False
    
    mensagem_finalizacao()

def imprime_menu_principal():
    imprime_titulo('MENU PRINCIPAL')
    print('1 - Hospitais')
    print('2 - Medicos')
    print('3 - Enfermeiros')
    print('4 - Pacientes')
    imprime_linha()
    print('0 - Sair')
    imprime_linha()

def mensagem_finalizacao():
    limpa_tela()
    imprime_titulo('SISTEMA HOSPITALAR', 48)
    print("Obrigado por utilizar o programa. Até a próxima!")
    imprime_linha(48)
    pausa()
    limpa_tela()

if __name__ == '__main__':
    main()