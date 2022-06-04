import os

def limpa_tela():
    os.system('cls') if os.name == 'nt' else os.system('clear')

def pausa():
    input('\nPressione Enter. . .')
    
def imprime_titulo(titulo: str, tamanho=24):
    linha = (tamanho - len(titulo))
    if linha % 2 == 0:
        linha = int(linha / 2)
        print(('-' * linha) + f'{titulo}' + ('-' * linha))
    else:
        linha = int((linha - 1) / 2)
        print(('-' * linha) + f'{titulo}' + ('-' * (linha + 1)))    

def imprime_linha(tamanho=24):
    print('-' * tamanho)
    
def mensagem_input_invalido(mensagem:str, tamanho_total=24):
    quant_espacos = (tamanho_total - len(mensagem) - 8) 
    if quant_espacos % 2 == 0:
        quant_espacos = int(quant_espacos / 2)
        print(' ' * quant_espacos + f'>>> {mensagem} <<<')
    else:
        quant_espacos = int((quant_espacos - 1) / 2)
        print(' ' * quant_espacos + f'>>> {mensagem} <<<')
    imprime_linha(tamanho_total)
    
def mensagem_erro(titulo:str, entidade:str, operacao:str):
    limpa_tela()
    
    imprime_titulo(titulo, 36)
    print(f'Não foi possível {operacao} o {entidade}!')
    
    pausa()

def mensagem_sucesso(titulo:str, entidade:str, operacao:str):
    limpa_tela()
    
    imprime_titulo(titulo, 36)
    print(f'{entidade} {operacao} com Sucesso!')
    
    pausa()
    