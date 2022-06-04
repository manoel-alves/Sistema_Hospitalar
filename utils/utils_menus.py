from utils.utils_geral import *

def obter_opcao(quant_opcoes):
    try:
        opcao = int(input('Opcao: '))
        
        if opcao < 0 or opcao > quant_opcoes:
            return -1
                
        return opcao
    except ValueError:
        return -1

def imprime_menu_crud(titulo: str):
    imprime_titulo(f'CRUD {titulo}')
    print('1 - Inserir')
    print('2 - Alterar')
    print('3 - Relatorios')
    print('4 - Excluir')
    imprime_linha()
    print('0 - Voltar')
    imprime_linha()

def checa_erro(valido, mensagem):
    if not valido:
        print('>>> ' + mensagem + ' <<<')        
    return True
