from classes import Endereco
from utils.geral import *
from utils.validacoes import *

def obter_opcao(quant_opcoes):
    try:
        opcao = int(input('Opcao: '))
        
        if opcao < 0 or opcao > quant_opcoes:
            return -1
                
        return opcao
    except ValueError:
        return -1

def titulo_obtencao(titulo, tam=24):
    imprime_titulo(titulo, tam)
    print('0 - Cancelar')
    imprime_linha(tam)

def obter_rua(titulo:str):
    valido = True
    while True:
        limpa_tela()
        
        titulo_obtencao(titulo)
        if not valido:
            mensagem_input_invalido('Rua Inválida!')
            valido = True
        rua = input('Insira a rua (endereco): ').strip().title()
        
        if rua != '0':
            if valida_nome(rua):
                return rua
            else:
                valido = False
        else:
            return False

def obter_bairro(titulo:str):
    valido = True
    while True:
        limpa_tela()
        
        titulo_obtencao(titulo)
        if not valido:
            mensagem_input_invalido('Bairro Inválido!')
            valido = True
        bairro = input('Insira o bairro (endereco): ').strip().title()
        
        if bairro != '0':
            if valida_nome(bairro):
                return bairro
            else:
                valido = False
        else:
            return False  

def obter_cidade(titulo:str):
    valido = True
    while True:
        limpa_tela()
        
        titulo_obtencao(titulo)
        if not valido:
            mensagem_input_invalido('Cidade Inválida!')
            valido = True
        cidade = input('Insira a Cidade (endereco): ').strip().title()
        
        if cidade != '0':
            if valida_nome(cidade):
                return cidade
            else:
                valido = False
        else:
            return False

def obter_cep(titulo:str):
    valido = True
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        titulo_obtencao(titulo)
        if not valido:
            mensagem_input_invalido('CEP Inválido!')
            valido = True
        if ja_cadastrado:
            mensagem_input_invalido('CEP Ja Registrado!')
            
        cep = input('Insira o CEP (XXXXX-XXX): ').strip()
        
        if cep != '0':
            if valida_cep(cep.strip()):
                ja_cadastrado = dado_ja_cadastrado('Hospital', 'cep', cep)
                if not ja_cadastrado:
                    return cep
            else:
                valido = False        
        else:
            return False

def obter_nome(titulo:str):
    valido = True
    while True:
        limpa_tela()
        
        titulo_obtencao(titulo)
        if not valido:
            mensagem_input_invalido('Nome Invalido!')
            valido = True
        nome = input('Insira o Nome: ').strip().title()
        
        if nome != '0':
            if valida_nome(nome):
                return nome
            else:
                valido = False
        else:
            return False
        
def obter_cnpj(titulo:str):
    valido = True
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        titulo_obtencao(titulo, tam=36)
        if not valido:
            mensagem_input_invalido('CNPJ Inválido!', 36)
            valido = True
        if ja_cadastrado:
            mensagem_input_invalido('CNPJ Ja Cadastrado!', 36)
            ja_cadastrado = False
        cnpj = input('Insira o CNPJ (XX.XXX.XXX/YYYY-ZZ): ').strip()
        
        if cnpj != '0':
            if valida_cnpj(cnpj):
                ja_cadastrado = dado_ja_cadastrado('Hospital', 'cnpj', cnpj)
                if not ja_cadastrado:
                    return cnpj
            else:
                valido = False
        else:
            return False

def obter_telefone(titulo:str):
    valido = True
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        titulo_obtencao(titulo, tam=36)
        if not valido:
            mensagem_input_invalido('Telefone Inválido!', 36)
            valido = True
        if ja_cadastrado:
            mensagem_input_invalido('Telefone Ja Cadastrado!', 36)
            ja_cadastrado = False
        telefone = input('Insira o Telefone (XXXXX-XXXX): ').strip()
        
        if telefone != '0':
            if valida_telefone(telefone):
                ja_cadastrado = dado_ja_cadastrado('Hospital', 'telefone', telefone)
                if not ja_cadastrado:
                    return telefone
            else:
                valido = False
        else:
            return False

def obter_endereco(titulo:str):
    rua = obter_rua(titulo)
    if not rua: return False
    
    bairro = obter_bairro(titulo)
    if not bairro: return False
          
    cidade = obter_cidade(titulo)
    if not cidade: return False
        
    cep = obter_cep(titulo)
    if not cep: return False
    
    return Endereco(rua, bairro, cidade, cep)
