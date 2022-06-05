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

def Adiciona_Telefone(): 
    pass
#------------------------------------------------------

def altera_medico():
    titulo = 'ALTERA MEDICO'
    
    comando = '''SELECT * FROM Medico'''
    medicos = pega_info_db(comando)
    
    qnt_medicos = len(medicos)
    
    if qnt_medicos != 0:
        valido = True
        crm_medico = ''
        while True: # obtem medico
            limpa_tela()
            
            imprime_titulo(titulo)
            for i, medico in enumerate(medicos):
                print(f'{i + 1} - {medico[2]}')
            imprime_linha()
            print('0 - Voltar')
            imprime_linha()
            
            if not valido:
                mensagem_input_invalido('Opcao Invalida!')
                valido = True
            
            opcao = obter_opcao(qnt_medicos)
            
            if opcao == 0:
                break
            
            if opcao == -1:
                valido = False
            else:
                crm_medico = medicos[opcao - 1][0]
                cpf_medico = medicos[opcao - 1][1]
                nome_medico = medicos[opcao - 1][2]
                rua_medico = medicos[opcao - 1][3]
                bairro_medico = medicos[opcao - 1][4]
                cidade_medico = medicos[opcao - 1][5]
                cep_medico = medicos[opcao - 1][6]
                especialidade_id = medicos[opcao - 1][7]
                comando = '''SELECT titulo FROM Especialidade WHERE id_Especialidade = :id'''
                especialidade_nome = pega_info_db(comando, {'id':especialidade_id})[0][0]
                break
        
        if opcao != 0:
            tipo_dado = ''
            dado = ''
            while True: # obtem dado
                limpa_tela()
                
                imprime_titulo(titulo)
                print('Qual dado deseja alterar?')
                imprime_linha()
                print(f'1 - Nome ({nome_medico})')
                print(f'2 - CPF ({cpf_medico})')
                print('3 - Endereco')
                print(f'4 - Especialidade ({especialidade_nome})')
                imprime_linha()
                print('0 - Voltar')
                imprime_linha()
                
                if not valido:
                    mensagem_input_invalido('Opcao Invalida!')
                    valido = True
                
                opcao = obter_opcao(4)
                
                if opcao == -1:
                    valido = False
                else:
                    if opcao == 1:
                        tipo_dado = 'nome'
                        dado = obter_nome(titulo)
                        break
                    elif opcao == 2:
                        tipo_dado = 'cpf'
                        dado = obter_cpf(titulo)
                        break
                    elif opcao == 3:
                        valido = True
                        while True:
                            limpa_tela()
                            
                            imprime_titulo(titulo)
                            print('Qual dado do Endereco?')
                            imprime_linha()
                            print(f'1 - Rua ({rua_medico})')
                            print(f'2 - Bairro ({bairro_medico})')
                            print(f'3 - Cidade ({cidade_medico})')
                            print(f'4 - CEP ({cep_medico})')
                            imprime_linha()
                            print('0 - Voltar')
                            imprime_linha()
                            
                            if not valido:
                                mensagem_input_invalido('Opcao Invalida!')
                                valido = True
                            
                            opcao = obter_opcao(4)
                            
                            if opcao == -1:
                                valido = False
                            else:
                                if opcao == 1:
                                    tipo_dado = 'rua'
                                    dado = obter_rua(titulo)
                                    break
                                elif opcao == 2:
                                    tipo_dado = 'bairro'
                                    dado = obter_bairro(titulo)
                                    break
                                elif opcao == 3:
                                    tipo_dado = 'cidade'
                                    dado = obter_cidade(titulo)
                                    break
                                elif opcao == 4:
                                    tipo_dado = 'cep'
                                    dado = obter_cep(titulo)
                                    break
                                elif opcao == 0:
                                    break
                                else:
                                    valido = False
                        
                        break
                    elif opcao == 4:
                        tipo_dado = 'fk_especialidade'
                        dado = obter_especialidade(titulo)
                        break
                    elif opcao == 0:
                        break
                    else:
                        valido = False
            
            if dado != 0 and opcao != 0:
                comando = '''UPDATE Medico SET {coluna} = :dado WHERE crm = :crm'''.format(coluna=tipo_dado)
                dados = {'crm': crm_medico, 'dado': dado}
                    
                atualizado = altera_db(comando, dados)
                if atualizado:
                    mensagem_sucesso(titulo, 'Medico', 'Alterado')
                else:
                    mensagem_erro(titulo, 'Medico', 'Alterar')
    else:
        mensagem = 'Ainda não há Medicos Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)

#------------------------------------------------------

def menu_relatorios_medico():
    quant_opcoes = 5
    qnt_linhas = 44
    
    valido = True
    while True:
        limpa_tela()
        
        imprime_titulo('RELATORIOS MEDICO', qnt_linhas)
        print('1 - Listar Medicos')
        print('2 - Listar Hospitais que o medico trabalha')
        print('3 - Listar Enfermeiras que auxiliam o medico')
        print('4 - Listar Pacientes do medico')
        print('5 - Listar Telefones do medico')
        imprime_linha(qnt_linhas)
        print('0 - Voltar')
        imprime_linha(qnt_linhas)
        
        if not valido:
            mensagem_input_invalido('Opcao Invalida!', qnt_linhas)
           
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            lista_medicos()
        elif opcao == 2:
            lista_hospitais_medico()
        elif opcao == 3:
            lista_enfermeiras_medico()
        elif opcao == 4:
            lista_pacientes_medico()
        elif opcao == 5:
            lista_telefones_medico()
        elif opcao == 0:
            break
        else:
            valido = False

def lista_medicos():
    titulo = 'LISTA DE MEDICOS'
    
    comando = '''SELECT * FROM Medico'''
    medicos = pega_info_db(comando)
    
    qnt_linhas = 36
    if len(medicos) != 0:
        limpa_tela()
        imprime_titulo(titulo, qnt_linhas)
        for medico in medicos:
            print(f'Nome: {medico[2]}')
            print(f'CRM: {medico[0]}')
            print(f'CPF: {medico[1]}')
            print('Endereco:')
            print(f'         Rua: {medico[3]}')
            print(f'         Bairro: {medico[4]}')
            print(f'         Cidade: {medico[5]}')
            print(f'         CEP: {medico[6]}')
            comando = '''SELECT titulo FROM Especialidade WHERE id_Especialidade = :id'''
            especialidade = pega_info_db(comando, {'id':medico[7]})[0][0]
            print(f'Especialidade: {especialidade}')
            imprime_linha(qnt_linhas)
        pausa()  
    else:
        mensagem = 'Ainda não ha Medicos Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)

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