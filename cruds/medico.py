from utils.db_operacoes import altera_db, pega_info_db
from classes import *
from utils.geral import *
from utils.obtencoes import *
from utils.validacoes import *

def insere_medico():
    titulo = 'INSERIR MEDICO'
    
    while True:
        nome = obter_nome(titulo)
        if not nome: break
        
        cpf = obter_cpf(titulo)
        if not cpf: break
        
        crm = obter_crm(titulo)
        if not crm: break
        
        endereco = obter_endereco(titulo)
        if not endereco: break
        
        especialidade = obter_especialidade(titulo)
        if not especialidade: break
        
        medico = Medico(crm, cpf, nome, endereco, especialidade)
        
        if confirma_dados(titulo, medico):
            comando = '''INSERT INTO Medico (crm, cpf, nome, rua, bairro, cidade, cep, fk_especialidade) 
                        VALUES (:crm, :cpf, :nome, :rua, :bairro, :cidade, :cep, :especialidade);'''
            dados = {"crm": medico.crm,
                     "cpf": medico.cpf,
                     "nome": medico.nome,
                     "rua": medico.endereco.rua,
                     "bairro": medico.endereco.bairro,
                     "cidade": medico.endereco.cidade,
                     "cep": medico.endereco.cep,
                     "especialidade": medico.especialidade[0]}
            
            medico_inserido = altera_db(comando, dados)
            
            if medico_inserido:
                mensagem_sucesso(titulo, 'Medico', 'Inserido')
                break
            else:
                mensagem_erro(titulo, 'Medico', 'Inserir')
                break

def confirma_dados(titulo:str, medico:Medico):
    tam_linha = 36
    
    valido = True
    while True:
        limpa_tela()
        
        imprime_titulo(titulo, tam_linha)
        print(f'Nome: {medico.nome}')
        print(f'CPF: {medico.cpf}')
        print(f'CRM: {medico.crm}')
        print('Endereco:')
        print(f'         Rua: {medico.endereco.rua}')
        print(f'         Bairro: {medico.endereco.bairro}')
        print(f'         Cidade: {medico.endereco.cidade}')
        print(f'         CEP: {medico.endereco.cep}')
        print(f'Especialidade: {medico.especialidade[1]}')
        imprime_linha(tam_linha)
        
        if not valido:
            mensagem_input_invalido('Opcao Inválida!', tam_linha)
            valido = True
            
        confirma = input('Os dados estão corretos? (s/n): ').upper()
        
        if confirma in ['S', 'N']:
            return True if confirma == 'S' else False
        else:
            valido = False

def associa_medico_hospital():
    titulo = 'MEDICO X HOSPITAL'
    
    comando = '''SELECT crm, nome FROM Medico'''
    medicos = pega_info_db(comando)
    
    comando = '''SELECT cnpj, nome FROM Hospital'''
    hospitais = pega_info_db(comando)
    
    qnt_medicos = len(medicos)
    qnt_hospitais = len(hospitais)
    
    if qnt_medicos != 0 and qnt_hospitais != 0:
        valido = True
        alterna = 0
        while True:
            limpa_tela()
            
            imprime_titulo(titulo)
            if alterna == 0:
                print('Qual Medico?')
                for i, medico in enumerate(medicos):
                    print(f'{i + 1} - {medico[1]}')
            else:
                print('Trabalha em qual Hospital?')
                for i, hospital in enumerate(hospitais):
                    print(f'{i + 1} - {hospital[1]}')
            imprime_linha()
            print('0 - Voltar')
            imprime_linha()
            
            if not valido:
                mensagem_input_invalido('Opcao Invalida!')
                valido = True
            
            if alterna == 0:
                opcao = obter_opcao(qnt_medicos)
            else:
                opcao = obter_opcao(qnt_hospitais)
            
            if opcao == -1:
                valido = False
            else:
                if alterna == 0:
                    crm_medico = medicos[opcao - 1][0]
                    alterna += 1
                else:
                    cnpj_hospital = hospitais[opcao - 1][0]
                    break
        
        if opcao != 0:
            print(crm_medico)
            print(cnpj_hospital)
            pausa()
            comando = '''INSERT INTO Hospital_x_Medico (cnpj, crm) VALUES (:cnpj, :crm)'''
            associa = altera_db(comando, {'cnpj':cnpj_hospital,'crm':crm_medico})
            
            if associa:
                mensagem_sucesso(titulo, 'Medico', 'Associado')
            else:
                mensagem_erro(titulo, 'Medico', 'Associar')
    else:
        if qnt_hospitais == 0 and qnt_medicos == 0:
            mensagem = 'Ainda não há Medicos e Hospitais Cadastrados!'
        elif qnt_medicos == 0:
            mensagem = 'Ainda não há Medicos Cadastrados!'
        else:
            mensagem = 'Ainda não há Hospitais Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)

#------------------------------------------------------

def altera_medico():
    pass

#------------------------------------------------------

def menu_relatorios_medico():
    pass

def lista_medicos():
    pass

def lista_hospitais_medico():
    pass

def lista_enfermeiras_medico():
    pass

def lista_pacientes_medico():
    pass

def lista_telefones_medico():
    pass

#------------------------------------------------------

def exclui_medico():
    titulo = 'EXCLUIR MEDICO'
    
    comando = '''SELECT crm, nome FROM Medico'''
    medicos = pega_info_db(comando)
    
    qnt_medicos = len(medicos)
    
    if qnt_medicos != 0:
        valido = True
        while True:
            limpa_tela()
            
            imprime_titulo(titulo)
            for i, medico in enumerate(medicos):
                print(f'{i + 1} - {medico[1]}')
            imprime_linha()
            print('0 - Voltar')
            imprime_linha()
            
            if not valido:
                mensagem_input_invalido('Opcao Invalida!')
                valido = True
            
            opcao = obter_opcao(qnt_medicos)
            
            if opcao == -1:
                valido = False
            else:
                crm_medico = medicos[opcao - 1][0]
                break
        
        if opcao != 0:
            
            comando = '''DELETE FROM Hospital_x_Medico WHERE crm=:crm'''
            altera_db(comando, {'crm':crm_medico})
            
            comando = '''DELETE FROM Medico WHERE crm=:crm'''
            excluido = altera_db(comando, {'crm':crm_medico})
            
            if excluido:
                mensagem_sucesso(titulo, 'Medico', 'Excluido')
            else:
                mensagem_erro(titulo, 'Medico', 'Excluir')
    else:
        mensagem = 'Ainda não há Medicos Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)