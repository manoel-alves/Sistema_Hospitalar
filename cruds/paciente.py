from utils.db_operacoes import altera_db, pega_info_db
from classes import Endereco, Paciente
from utils.geral import *
from utils.obtencoes import *
from utils.validacoes import *

def insere_paciente():
    titulo = 'INSERIR Paciente'
    
    while True:
        nome = obter_nome(titulo)
        if not nome: break
        
        cpf = obter_cpf(titulo)
        if not cpf: break
        
        rg = obter_rg(titulo)
        if not rg: break
        
        endereco = obter_endereco(titulo)
        if not endereco: break
        
        paciente = Paciente(cpf, rg, nome, endereco)
        
        if confirma_dados(titulo, paciente):
            comando = '''INSERT INTO Paciente (cpf, rg, nome, rua, bairro, cidade, cep) 
                        VALUES (:cpf, :rg, :nome, :rua, :bairro, :cidade, :cep);'''
            dados = {"cpf": paciente.cpf,
                     'rg': paciente.rg,
                     "nome": paciente.nome,
                     "rua": paciente.endereco.rua,
                     "bairro": paciente.endereco.bairro,
                     "cidade": paciente.endereco.cidade,
                     "cep": paciente.endereco.cep}
            
            paciente_inserida = altera_db(comando, dados)
            
            if paciente_inserida:
                mensagem_sucesso(titulo, 'Paciente', 'Inserido')
                break
            else:
                mensagem_erro(titulo, 'Paciente', 'Inserir')
                break

def confirma_dados(titulo:str, paciente:Paciente):
    tam_linha = 36
    
    valido = True
    while True:
        limpa_tela()
        
        imprime_titulo(titulo, tam_linha)
        print(f'Nome: {paciente.nome}')
        print(f'CPF: {paciente.cpf}')
        print(f'RG: {paciente.rg}')
        print('Endereco:')
        print(f'         Rua: {paciente.endereco.rua}')
        print(f'         Bairro: {paciente.endereco.bairro}')
        print(f'         Cidade: {paciente.endereco.cidade}')
        print(f'         CEP: {paciente.endereco.cep}')
        imprime_linha(tam_linha)
        
        if not valido:
            mensagem_input_invalido('Opcao Inválida!', tam_linha)
            valido = True
            
        confirma = input('Os dados estão corretos? (s/n): ').upper()
        
        if confirma in ['S', 'N']:
            return True if confirma == 'S' else False
        else:
            valido = False

def adiciona_tratamento():
    pass

#------------------------------------------------------

def altera_paciente():
    titulo = 'ALTERA PACIENTE'
    
    comando = '''SELECT * FROM Paciente'''
    pacientes = pega_info_db(comando)
    
    qnt_pacientes = len(pacientes)
    
    if qnt_pacientes != 0:
        valido = True
        cpf_paciente = ''
        while True:
            limpa_tela()
            
            imprime_titulo(titulo)
            for i, paciente in enumerate(pacientes):
                print(f'{i + 1} - {paciente[2]}')
            imprime_linha()
            print('0 - Voltar')
            imprime_linha()
            
            if not valido:
                mensagem_input_invalido('Opcao Invalida!')
                valido = True
            
            opcao = obter_opcao(qnt_pacientes)
            
            if opcao == 0:
                break
            
            if opcao == -1:
                valido = False
            else:
                cpf_paciente = pacientes[opcao - 1][0]
                rg_paciente = pacientes[opcao - 1][1]
                nome_paciente = pacientes[opcao - 1][2]
                rua_paciente = pacientes[opcao - 1][3]
                bairro_paciente = pacientes[opcao - 1][4]
                cidade_paciente = pacientes[opcao - 1][5]
                cep_paciente = pacientes[opcao - 1][6]
                break
        
        if opcao != 0:
            tipo_dado = ''
            dado = ''
            while True: # obtem dado
                limpa_tela()
                
                imprime_titulo(titulo)
                print('Qual dado deseja alterar?')
                imprime_linha()
                print(f'1 - Nome ({nome_paciente})')
                print(f'2 - CPF ({cpf_paciente})')
                print(f'3 - RG ({rg_paciente})')
                print('4 - Endereco')
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
                        tipo_dado = 'rg'
                        dado = obter_rg(titulo)
                        break
                    elif opcao == 4:
                        valido = True
                        while True:
                            limpa_tela()
                            
                            imprime_titulo(titulo)
                            print('Qual dado do Endereco?')
                            imprime_linha()
                            print(f'1 - Rua ({rua_paciente})')
                            print(f'2 - Bairro ({bairro_paciente})')
                            print(f'3 - Cidade ({cidade_paciente})')
                            print(f'4 - CEP ({cep_paciente})')
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
                    elif opcao == 0:
                        break
                    else:
                        valido = False
            
            if dado != 0 and opcao != 0:
                comando = '''UPDATE Paciente SET {coluna} = :dado WHERE cpf = :cpf'''.format(coluna=tipo_dado)
                dados = {'cpf': cpf_paciente, 'dado': dado}
                    
                atualizado = altera_db(comando, dados)
                if atualizado:
                    mensagem_sucesso(titulo, 'Paciente', 'Alterado')
                else:
                    mensagem_erro(titulo, 'Paciente', 'Alterar')
    else:
        mensagem = 'Ainda não há Pacientes Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)

#------------------------------------------------------

def menu_relatorios_paciente():
    quant_opcoes = 3
    qnt_linhas = 34
    
    valido = True
    while True:
        limpa_tela()
        
        imprime_titulo('RELATORIOS PACIENTE', qnt_linhas)
        print('1 - Listar Pacientes')
        print('2 - Listar Tratamentos do Paciente')
        print('3 - Listar Medicos do Paciente')
        imprime_linha(qnt_linhas)
        print('0 - Voltar')
        imprime_linha(qnt_linhas)
        
        if not valido:
            mensagem_input_invalido('Opcao Invalida!', qnt_linhas)
           
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            lista_pacientes()
        elif opcao == 2:
            lista_tratamentos()
        elif opcao == 3:
            lista_medicos_paciente()
        elif opcao == 0:
            break
        else:
            valido = False

def lista_pacientes():
    titulo = 'LISTA DE PACIENTES'
    qnt_linhas = 36
    
    comando = '''SELECT * FROM Paciente'''
    pacientes = pega_info_db(comando)
    
    if len(pacientes) != 0:
        limpa_tela()
        imprime_titulo(titulo, qnt_linhas)
        for paciente in pacientes:
            print(f'Nome: {paciente[2]}')
            print(f'RG: {paciente[1]}')
            print(f'CPF: {paciente[0]}')
            print('Endereco:')
            print(f'         Rua: {paciente[3]}')
            print(f'         Bairro: {paciente[4]}')
            print(f'         Cidade: {paciente[5]}')
            print(f'         CEP: {paciente[6]}')
            imprime_linha(qnt_linhas)
        pausa()  
    else:
        mensagem = 'Ainda não ha Pacientes Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)

def lista_tratamentos():
    pass

def lista_medicos_paciente():
    pass

#------------------------------------------------------

def exclui_paciente():
    titulo = 'EXCLUIR PACIENTE'
    
    comando = '''SELECT cpf, nome FROM Paciente'''
    pacientes = pega_info_db(comando)
    
    qnt_pacientes = len(pacientes)
    
    if qnt_pacientes != 0:
        valido = True
        while True:
            limpa_tela()
            
            imprime_titulo(titulo)
            for i, paciente in enumerate(pacientes):
                print(f'{i + 1} - {paciente[1]} ({paciente[0]})')
            imprime_linha()
            print('0 - Voltar')
            imprime_linha()
            
            if not valido:
                mensagem_input_invalido('Opcao Invalida!')
                valido = True
            
            opcao = obter_opcao(qnt_pacientes)
            
            if opcao == -1:
                valido = False
            else:
                cpf_paciente = pacientes[opcao - 1][0]
                break
        
        if opcao != 0:

            exclui_dependencias()
                        
            comando = '''DELETE FROM Paciente WHERE cpf=:cpf'''
            excluido = altera_db(comando, {'cpf':cpf_paciente})
            
            if excluido:
                mensagem_sucesso(titulo, 'Paciente', 'Excluido')
            else:
                mensagem_erro(titulo, 'Paciente', 'Excluir')
    else:
        mensagem = 'Ainda não há Pacientes Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)

def exclui_dependencias():
    pass

#------------------------------------------------------