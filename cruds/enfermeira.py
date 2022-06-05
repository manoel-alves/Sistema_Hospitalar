from utils.db_operacoes import altera_db, pega_info_db
from classes import Endereco, Enfermeira
from utils.geral import *
from utils.obtencoes import *
from utils.validacoes import *

def insere_enfermeira():
    titulo = 'INSERIR ENFERMEIRA'
    
    while True:
        nome = obter_nome(titulo)
        if not nome: break
        
        cpf = obter_cpf(titulo)
        if not cpf: break
        
        coren = obter_coren(titulo)
        if not coren: break
        
        endereco = obter_endereco(titulo)
        if not endereco: break
        
        enfermeira = Enfermeira(coren, cpf, nome, endereco)
        
        if confirma_dados(titulo, enfermeira):
            comando = '''INSERT INTO Enfermeira (coren, cpf, nome, rua, bairro, cidade, cep) 
                        VALUES (:coren, :cpf, :nome, :rua, :bairro, :cidade, :cep);'''
            dados = {"coren": enfermeira.coren,
                     "cpf": enfermeira.cpf,
                     "nome": enfermeira.nome,
                     "rua": enfermeira.endereco.rua,
                     "bairro": enfermeira.endereco.bairro,
                     "cidade": enfermeira.endereco.cidade,
                     "cep": enfermeira.endereco.cep}
            
            enfermeira_inserida = altera_db(comando, dados)
            
            if enfermeira_inserida:
                mensagem_sucesso(titulo, 'Enfermeira', 'Inserida')
                break
            else:
                mensagem_erro(titulo, 'Enfermeira', 'Inserir')
                break

def confirma_dados(titulo:str, enfermeira:Enfermeira):
    tam_linha = 36
    
    valido = True
    while True:
        limpa_tela()
        
        imprime_titulo(titulo, tam_linha)
        print(f'Nome: {enfermeira.nome}')
        print(f'CPF: {enfermeira.cpf}')
        print(f'COREN: {enfermeira.coren}')
        print('Endereco:')
        print(f'         Rua: {enfermeira.endereco.rua}')
        print(f'         Bairro: {enfermeira.endereco.bairro}')
        print(f'         Cidade: {enfermeira.endereco.cidade}')
        print(f'         CEP: {enfermeira.endereco.cep}')
        imprime_linha(tam_linha)
        
        if not valido:
            mensagem_input_invalido('Opcao Inválida!', tam_linha)
            valido = True
            
        confirma = input('Os dados estão corretos? (s/n): ').upper()
        
        if confirma in ['S', 'N']:
            return True if confirma == 'S' else False
        else:
            valido = False

def associa_enfermeira_medico():
    pass

def associa_enfermeira_hospital():
    pass

#------------------------------------------------------

def altera_enfermeira():
    titulo = 'ALTERA ENFERMEIRA'
    
    comando = '''SELECT * FROM Enfermeira'''
    enfermeiras = pega_info_db(comando)
    
    qnt_enfermeiras = len(enfermeiras)
    
    if qnt_enfermeiras != 0:
        valido = True
        coren_enfermeira = ''
        while True:
            limpa_tela()
            
            imprime_titulo(titulo)
            for i, enfermeira in enumerate(enfermeiras):
                print(f'{i + 1} - {enfermeira[2]}')
            imprime_linha()
            print('0 - Voltar')
            imprime_linha()
            
            if not valido:
                mensagem_input_invalido('Opcao Invalida!')
                valido = True
            
            opcao = obter_opcao(qnt_enfermeiras)
            
            if opcao == 0:
                break
            
            if opcao == -1:
                valido = False
            else:
                coren_enfermeira = enfermeiras[opcao - 1][0]
                cpf_enfermeira = enfermeiras[opcao - 1][1]
                nome_enfermeira = enfermeiras[opcao - 1][2]
                rua_enfermeira = enfermeiras[opcao - 1][3]
                bairro_enfermeira = enfermeiras[opcao - 1][4]
                cidade_enfermeira = enfermeiras[opcao - 1][5]
                cep_enfermeira = enfermeiras[opcao - 1][6]
                break
        
        if opcao != 0:
            tipo_dado = ''
            dado = ''
            while True: # obtem dado
                limpa_tela()
                
                imprime_titulo(titulo)
                print('Qual dado deseja alterar?')
                imprime_linha()
                print(f'1 - Nome ({nome_enfermeira})')
                print(f'2 - CPF ({cpf_enfermeira})')
                print('3 - Endereco')
                imprime_linha()
                print('0 - Voltar')
                imprime_linha()
                
                if not valido:
                    mensagem_input_invalido('Opcao Invalida!')
                    valido = True
                
                opcao = obter_opcao(3)
                
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
                            print(f'1 - Rua ({rua_enfermeira})')
                            print(f'2 - Bairro ({bairro_enfermeira})')
                            print(f'3 - Cidade ({cidade_enfermeira})')
                            print(f'4 - CEP ({cep_enfermeira})')
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
                comando = '''UPDATE Enfermeira SET {coluna} = :dado WHERE coren = :coren'''.format(coluna=tipo_dado)
                dados = {'coren': coren_enfermeira, 'dado': dado}
                    
                atualizado = altera_db(comando, dados)
                if atualizado:
                    mensagem_sucesso(titulo, 'Enfermeira', 'Alterada')
                else:
                    mensagem_erro(titulo, 'Enfermeira', 'Alterar')
    else:
        mensagem = 'Ainda não há Enfermeiras Cadastradas!'
        mensagem_query_vazia(titulo, mensagem)

#------------------------------------------------------

def menu_relatorios_enfermeira():
    quant_opcoes = 3
    qnt_linhas = 46
    
    valido = True
    while True:
        limpa_tela()
        
        imprime_titulo('RELATORIOS ENFERMEIRA', qnt_linhas)
        print('1 - Listar Enfermeiras')
        print('2 - Listar Hospitais que a Enfermeira trabalha')
        print('3 - Listar Medicos que a Enfermeira auxilia')
        imprime_linha(qnt_linhas)
        print('0 - Voltar')
        imprime_linha(qnt_linhas)
        
        if not valido:
            mensagem_input_invalido('Opcao Invalida!', qnt_linhas)
           
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            lista_enfermeiras()
        elif opcao == 2:
            lista_hospitais_enfermeira()
        elif opcao == 3:
            lista_medicos_enfermeira()
        elif opcao == 0:
            break
        else:
            valido = False

def lista_enfermeiras():
    titulo = 'LISTA DE ENFERMEIRAS'
    qnt_linhas = 36
    
    comando = '''SELECT * FROM Enfermeira'''
    Enfermeira = pega_info_db(comando)
    
    if len(Enfermeira) != 0:
        limpa_tela()
        imprime_titulo(titulo, qnt_linhas)
        for enfermeira in Enfermeira:
            print(f'Nome: {enfermeira[2]}')
            print(f'CPF: {enfermeira[1]}')
            print(f'COREN: {enfermeira[0]}')
            print('Endereco:')
            print(f'         Rua: {enfermeira[3]}')
            print(f'         Bairro: {enfermeira[4]}')
            print(f'         Cidade: {enfermeira[5]}')
            print(f'         CEP: {enfermeira[6]}')
            imprime_linha(qnt_linhas)
        pausa()  
    else:
        mensagem = 'Ainda não ha Enfermeira Cadastradas!'
        mensagem_query_vazia(titulo, mensagem)

def lista_hospitais_enfermeira():
    pass

def lista_medicos_enfermeira():
    pass

#------------------------------------------------------

def exclui_enfermeira():
    titulo = 'EXCLUIR ENFERMEIRA'
    
    comando = '''SELECT coren, nome FROM Enfermeira'''
    enfermeiras = pega_info_db(comando)
    
    qnt_enfermeiras = len(enfermeiras)
    
    if qnt_enfermeiras != 0:
        valido = True
        while True:
            limpa_tela()
            
            imprime_titulo(titulo)
            for i, enfermeira in enumerate(enfermeiras):
                print(f'{i + 1} - {enfermeira[1]}')
            imprime_linha()
            print('0 - Voltar')
            imprime_linha()
            
            if not valido:
                mensagem_input_invalido('Opcao Invalida!')
                valido = True
            
            opcao = obter_opcao(qnt_enfermeiras)
            
            if opcao == -1:
                valido = False
            else:
                coren_enfermeira = enfermeiras[opcao - 1][0]
                break
        
        if opcao != 0:

            exclui_dependencias()
                        
            comando = '''DELETE FROM Enfermeira WHERE coren=:coren'''
            excluido = altera_db(comando, {'coren':coren_enfermeira})
            
            if excluido:
                mensagem_sucesso(titulo, 'Enfermeira', 'Excluida')
            else:
                mensagem_erro(titulo, 'Enfermeira', 'Excluir')
    else:
        mensagem = 'Ainda não há Enfermeira Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)

def exclui_dependencias():
    pass

#------------------------------------------------------