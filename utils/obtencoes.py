from utils.db_operacoes import altera_db, pega_info_db
from classes import Endereco
from utils.geral import *
from utils.validacoes import *

def obter_opcao(quant_opcoes):
    try:
        opcao = input('Opcao: ')
        
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao < 0 or opcao > quant_opcoes:
                return -1
        elif opcao == '+':
            return opcao
        else:
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
    while True:
        limpa_tela()
        
        titulo_obtencao(titulo)
        if not valido:
            mensagem_input_invalido('CEP Inválido!')
            valido = True
            
        cep = input('Insira o CEP (XXXXX-XXX): ').strip()
        
        if cep != '0':
            if valida_cep(cep.strip()):
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

def obter_crm(titulo:str):
    valido = True
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        titulo_obtencao(titulo, tam=36)
        if not valido:
            mensagem_input_invalido('CRM Inválido!', 36)
            valido = True
        if ja_cadastrado:
            mensagem_input_invalido('CRM Ja Cadastrado!', 36)
            ja_cadastrado = False
        crm = input('Insira o CRM (XXXX/UF): ').strip().upper()
        
        if crm != '0':
            if valida_crm(crm):
                ja_cadastrado = dado_ja_cadastrado('Medico', 'crm', crm)
                if not ja_cadastrado:
                    return crm
            else:
                valido = False
        else:
            return False

def obter_cpf(titulo:str):
    entidades = ['Medico', 'Enfermeira', 'Paciente']
    
    valido = True
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        titulo_obtencao(titulo, tam=36)
        
        if not valido:
            mensagem_input_invalido('CPF Inválido!', 36)
            valido = True
        if ja_cadastrado:
            mensagem_input_invalido('CPF Ja Cadastrado!', 36)
            ja_cadastrado = False
            
        cpf = input('Insira o CPF (xxx.xxx.xxx-xx): ').strip()
        
        if cpf != '0':
            if valida_cpf(cpf):
                
                for entidade in entidades:
                    if dado_ja_cadastrado(entidade, 'cpf', cpf):
                        ja_cadastrado = True
                        break
                
                if not ja_cadastrado:
                    return cpf
            else:
                valido = False
        else:
            return False

def obter_especialidade(titulo:str):
    valido = True
    checar = True
    while True:
        if checar:
            comando = '''SELECT * FROM Especialidade'''
            especialidades = pega_info_db(comando)
            
            qnt_especialidades = len(especialidades)
            
            if qnt_especialidades == 0:
                inserido = cadastrar_especialidade()
                if not inserido: return False
            checar = False
        
        limpa_tela()
        
        imprime_titulo(titulo, 36)
        print('Qual a especialidade do Medico?')
        imprime_linha(36)
        for i, espec in enumerate(especialidades):
            print(f'{i + 1} - {espec[1]}')
        imprime_linha(36)
        print('+ - Cadastrar Especialidade')
        print('0 - Cancelar')
        imprime_linha(36)
        
        if not valido:
            mensagem_input_invalido('Opcao Invalida!', 36)
            valido = True
        opcao = obter_opcao(qnt_especialidades)
        
        if opcao == 0:
            return False
        
        if opcao == '+':
            inserido = cadastrar_especialidade()
            if not inserido: return False
            checar = True
        else:
            if opcao != -1:
                especialidade = especialidades[opcao - 1][1]
                print(especialidade)
                pausa()
                break 
            else:
                valido = False
    
    comando = '''SELECT * FROM Especialidade e WHERE e.titulo = :titulo'''
    especialidade = list(pega_info_db(comando, {'titulo': especialidade})[0])
    
    return especialidade

def cadastrar_especialidade():
    titulo_op = 'CADASTRAR ESPECIALIDADE'
    
    valido = True
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        titulo_obtencao(titulo_op, 36)
        
        if not valido:
            mensagem_input_invalido('Titulo Invalido!', 36)
            valido = True
        if ja_cadastrado:
            mensagem_input_invalido('Especialidade Ja Cadastrada!', 36)
            ja_cadastrado = False
        
        especialidade = input('Insira o Titulo: ').strip().title()
        
        if especialidade != '0':
            if valida_nome(especialidade):
                ja_cadastrado = dado_ja_cadastrado('Especialidade', 'titulo', especialidade)
                if not ja_cadastrado:
                    comando = '''INSERT INTO Especialidade (titulo) VALUES (:titulo)'''
                    inserido = altera_db(comando, {'titulo': especialidade})
                    if inserido:
                        mensagem_sucesso(titulo_op, 'Especialidade', 'Inserida')
                        return True
                    else:
                        mensagem_erro(titulo_op, 'Especialidade', 'Inserir')
                        return False

            else:
                valido = False
        else:
            return False

def obter_telefone(titulo_op:str):
    valido = True
    ja_cadastrado = False
    while True:
        limpa_tela()
        
        titulo_obtencao(titulo_op, tam=36)
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

def obter_endereco(titulo_op:str):
    rua = obter_rua(titulo_op)
    if not rua: return False
    
    bairro = obter_bairro(titulo_op)
    if not bairro: return False
          
    cidade = obter_cidade(titulo_op)
    if not cidade: return False
        
    cep = obter_cep(titulo_op)
    if not cep: return False
    
    return Endereco(rua, bairro, cidade, cep)
