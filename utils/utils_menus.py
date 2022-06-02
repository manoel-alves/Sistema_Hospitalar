from utils.utils_geral import *

def obter_opcao(quant_opcoes):
    try:
        opcao = int(input('Opcao: '))
        
        if opcao <= 0 or opcao > quant_opcoes:
            return 0
                
        return opcao
    except ValueError:
        return 0

def imprime_menu_crud(titulo: str):
    imprime_titulo(f'CRUD {titulo}')
    print('1 - Inserir')
    print('2 - Alterar')
    print('3 - Relatorios')
    print('4 - Excluir')
    print('5 - Voltar')
    imprime_linha()

def checa_erro(valido, mensagem):
    if not valido:
        print('>>> ' + mensagem + ' <<<')        
    return True