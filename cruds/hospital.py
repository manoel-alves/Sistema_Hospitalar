from utils.db_operacoes import altera_db, pega_info_db
from classes import Endereco, Hospital
from utils.utils_geral import *
from utils.utils_menus import *
from utils.validacoes import *

TITULO_INSERCAO = 'INSERIR HOSPITAL'
TITULO_EXCLUSAO = 'EXCLUIR HOSPITAL'

def insere_hospital():
    while True:
        nome = obter_nome()
        if not nome: break
          
        cnpj = obter_cnpj()
        if not cnpj: break
        
        endereco = obter_endereco()
        if not endereco: break
        
        telefone = obter_telefone()
        if not telefone: break
        
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
                mensagem_sucesso('Hospital', 'Inserido')
                break
            else:
                mensagem_erro('Hospital', 'Inserir')
                break

def obter_nome():
    valido = True
    while True:
        limpa_tela()
        
        titulo_obtencao()
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
        
def obter_cnpj():
    valido = True
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        titulo_obtencao(36)
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

def obter_telefone():
    valido = True
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        titulo_obtencao(36)
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

def obter_endereco():
    valido = True
    while True:
        limpa_tela()
        
        titulo_obtencao()
        if not valido:
            mensagem_input_invalido('Rua Inválida!')
            valido = True
        rua = input('Insira a rua (endereco): ').strip().title()
        
        if rua != '0':
            if valida_nome(rua):
                break
            else:
                valido = False
        else:
            return False
            
    while True:
        limpa_tela()
        
        titulo_obtencao()
        if not valido:
            mensagem_input_invalido('Bairro Inválido!')
            valido = True
        bairro = input('Insira o bairro (endereco): ').strip().title()
        
        if bairro != '0':
            if valida_nome(bairro):
                break
            else:
                valido = False
        else:
            return False  
          
    while True:
        limpa_tela()
        
        titulo_obtencao()
        if not valido:
            mensagem_input_invalido('Cidade Inválida!')
            valido = True
        cidade = input('Insira a Cidade (endereco): ').strip().title()
        
        if cidade != '0':
            if valida_nome(cidade):
                break
            else:
                valido = False
        else:
            return False
        
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        titulo_obtencao()
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
                    break
            else:
                valido = False        
        else:
            return False
    
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
    comando = '''SELECT * FROM Hospital'''
    hospitais = pega_info_db(comando)
    
    qnt_hospitais = 0
    for _ in hospitais:
        qnt_hospitais += 1
    
    if qnt_hospitais != 0:
        valido = True
        while True:
            limpa_tela()
            
            imprime_titulo(TITULO_EXCLUSAO)
            for i, hospital in enumerate(hospitais):
                print(f'{i + 1} - {hospital[1]}')
            imprime_linha()
            print('0 - Voltar')
            imprime_linha()
            
            if not valido:
                mensagem_input_invalido('Opcao Invalida!')
                valido = True
            
            opcao = obter_opcao(qnt_hospitais)
            
            if opcao == -1:
                valido = False
            else:
                break
        
        if opcao != 0:
            comando = '''DELETE FROM Hospital WHERE cnpj=:cnpj'''
            if altera_db(comando, {'cnpj':hospitais[opcao - 1][0]}):
                mensagem_sucesso('Hospital', 'Excluido')
            else:
                mensagem_erro('Hospital', 'Excluir')
    else:
        limpa_tela()
        imprime_titulo(TITULO_EXCLUSAO, 36)
        print('Ainda não há Hospitais Cadastrados!')
        pausa()
        
#------------------------------------------------------

def titulo_obtencao(tam=24):
    imprime_titulo(TITULO_INSERCAO, tam)
    print('0 - Cancelar')
    imprime_linha(tam)

def mensagem_erro(entidade:str, operacao:str):
    limpa_tela()
    
    imprime_titulo(TITULO_INSERCAO, 36)
    print(f'Não foi possível {operacao} o {entidade}!')
    
    pausa()

def mensagem_sucesso(entidade:str, operacao:str):
    limpa_tela()
    
    imprime_titulo(TITULO_INSERCAO, 36)
    print(f'{entidade} {operacao} com Sucesso!')
    
    pausa()