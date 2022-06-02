from utils.db_operacoes import altera_db, pega_info_db
from classes import Endereco, Hospital
from utils.utils_geral import *
from utils.validacoes import *

TITULO_INSERCAO = 'INSERIR HOSPITAL'

def insere_hospital():
    while True:
        nome = obter_nome()
        
        cnpj = obter_cnpj()
        
        endereco = obter_endereco()
        
        telefone = obter_telefone()
        
        hospital = Hospital(cnpj, nome, endereco, telefone)
        
        if confirma_dados(hospital):
            comando = '''INSERT INTO Hospital (cnpj, nome, rua, bairro, cidade, cep, telefone) 
                        VALUES (:cnpj, :nome, :rua, :bairro, :cidade, :cep, :telefone);'''
            dados = {"cnpj": hospital.cnpj,
                     "nome": hospital.nome,
                     "rua": hospital.endereco.rua,
                     "bairro": hospital.endereco.bairro,
                     "cidade": hospital.endereco.cidade,
                     "cep": hospital.endereco.cep,
                     "telefone": hospital.telefone}
            
            if altera_db(comando, dados):
                mensagem_sucesso()
                break
            else:
                mensagem_erro()
                break

def obter_nome():
    valido = True
    while True:
        limpa_tela()
        
        imprime_titulo(TITULO_INSERCAO)
        if not valido:
            mensagem_input_invalido('Nome Inválido!')
            valido = True
        nome = input('Insira o Nome: ').strip().title()
        
        if valida_nome(nome):
            return nome
        else:
            valido = False

def obter_cnpj():
    valido = True
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        imprime_titulo(TITULO_INSERCAO, 36)
        if not valido:
            mensagem_input_invalido('CNPJ Inválido!', 36)
            valido = True
        if ja_cadastrado:
            mensagem_input_invalido('CNPJ Ja Cadastrado!', 36)
            ja_cadastrado = False
        cnpj = input('Insira o CNPJ (XX.XXX.XXX/YYYY-ZZ): ').strip()
        
        if valida_cnpj(cnpj):
            ja_cadastrado = dado_ja_cadastrado('Hospital', 'cnpj', cnpj)
            if not ja_cadastrado:
                return cnpj
        else:
            valido = False

def obter_telefone():
    valido = True
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        imprime_titulo(TITULO_INSERCAO, 36)
        if not valido:
            mensagem_input_invalido('Telefone Inválido!', 36)
            valido = True
        if ja_cadastrado:
            mensagem_input_invalido('Telefone Ja Cadastrado!', 36)
            ja_cadastrado = False
        telefone = input('Insira o Telefone (XXXXX-XXXX): ').strip()
        
        if valida_telefone(telefone):
            ja_cadastrado = dado_ja_cadastrado('Hospital', 'telefone', telefone)
            if not ja_cadastrado:
                return telefone
        else:
            valido = False

def obter_endereco():
    valido = True
    while True:
        limpa_tela()
        
        imprime_titulo(TITULO_INSERCAO)
        if not valido:
            mensagem_input_invalido('Rua Inválida!')
            valido = True
        rua = input('Insira a rua (endereco): ').strip().title()
        
        if valida_nome(rua):
            break
        else:
            valido = False
            
    while True:
        limpa_tela()
        
        imprime_titulo(TITULO_INSERCAO)
        if not valido:
            mensagem_input_invalido('Bairro Inválido!')
            valido = True
        bairro = input('Insira o bairro (endereco): ').strip().title()
        
        if valida_nome(bairro):
            break
        else:
            valido = False
            
    while True:
        limpa_tela()
        
        imprime_titulo(TITULO_INSERCAO)
        if not valido:
            mensagem_input_invalido('Cidade Inválida!')
            valido = True
        cidade = input('Insira a Cidade (endereco): ').strip().title()
        
        if valida_nome(cidade):
            break
        else:
            valido = False
    
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        imprime_titulo(TITULO_INSERCAO)
        if not valido:
            mensagem_input_invalido('CEP Inválido!')
            valido = True
        if ja_cadastrado:
            mensagem_input_invalido('CEP Ja Registrado!')
            
        cep = input('Insira o CEP (XXXXX-XXX): ').strip()
        
        if valida_cep(cep.strip()):
            ja_cadastrado = dado_ja_cadastrado('Hospital', 'cep', cep)
            if not ja_cadastrado:
                break
        else:
            valido = False        
    
    return Endereco(rua, bairro, cidade, cep)

def confirma_dados(hospital:Hospital):
    tam_linha = 36
    valido = True
    while True:
        limpa_tela()
        
        imprime_titulo(TITULO_INSERCAO, tam_linha)
        print(f'Nome: {hospital.nome}')
        print(f'CNPJ: {hospital.cnpj}')
        print('Endereco:')
        print(f'         Rua: {hospital.endereco.rua}')
        print(f'         Bairro: {hospital.endereco.bairro}')
        print(f'         Cidade: {hospital.endereco.cidade}')
        print(f'         CEP: {hospital.endereco.cep}')
        print(f'Telefone: {hospital.telefone}')
        imprime_linha(tam_linha)
        
        if not valido:
            mensagem_input_invalido('Opcao Inválida!', tam_linha)
            valido = True
            
        confirma = input('Os dados estão corretos? (s/n): ').upper()
        
        if confirma in ['S', 'N']:
            return True if confirma == 'S' else False
        else:
            valido = False
    
def mensagem_erro():
    limpa_tela()
    
    imprime_titulo(TITULO_INSERCAO, 36)
    print('Não foi possível Cadastrar o Hospital!')
    
    pausa()

def mensagem_sucesso():
    limpa_tela()
    
    imprime_titulo(TITULO_INSERCAO, 36)
    print('Hospital Cadastrado com Sucesso!')
    
    pausa()

#------------------------------------------------------

def menu_relatorios_hospital():
    pass

def lista_hospitais():
    pass
    
#------------------------------------------------------

def altera_hospital():
    pass

#------------------------------------------------------

def exclui_hospital():
    pass

