from utils.db_operacoes import altera_db, pega_info_db
from classes import Endereco, Hospital
from utils.geral import *
from utils.validacoes import *
from utils.obtencoes import *

def insere_hospital():
    titulo = 'INSERIR HOSPITAL'
    while True:
        nome = obter_nome(titulo)
        if not nome: break
          
        cnpj = obter_cnpj(titulo)
        if not cnpj: break
        
        endereco = obter_endereco(titulo)
        if not endereco: break
        
        telefone = obter_telefone(titulo)
        if not telefone: break
        
        hospital = Hospital(cnpj, nome, endereco, telefone)
        
        if confirma_dados(titulo, hospital):
            comando = '''INSERT INTO Hospital (cnpj, nome, rua, bairro, cidade, cep, telefone) 
                        VALUES (:cnpj, :nome, :rua, :bairro, :cidade, :cep, :telefone);'''
            dados = {"cnpj": hospital.cnpj,
                     "nome": hospital.nome,
                     "rua": hospital.endereco.rua,
                     "bairro": hospital.endereco.bairro,
                     "cidade": hospital.endereco.cidade,
                     "cep": hospital.endereco.cep,
                     "telefone": hospital.telefone}
            
            inserido = altera_db(comando, dados)
            if inserido:
                mensagem_sucesso(titulo, 'Hospital', 'Inserido')
                break
            else:
                mensagem_erro(titulo, 'Hospital', 'Inserir')
                break

def confirma_dados(titulo:str, hospital:Hospital):
    tam_linha = 36
    valido = True
    while True:
        limpa_tela()
        
        imprime_titulo(titulo, tam_linha)
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
    quant_opcoes = 3
    qnt_linhas = 36
    valido = True
    while True:
        limpa_tela()
        
        imprime_titulo('RELATORIOS HOSPITAL', qnt_linhas)
        print('1 - Listar Hospitais')
        print('2 - Listar Medicos do Hospital')
        print('3 - Listar Enfermeiras do Hospital')
        imprime_linha(qnt_linhas)
        print('0 - Voltar')
        imprime_linha(qnt_linhas)
        
        if not valido:
            mensagem_input_invalido('Opcao Invalida!', qnt_linhas)
           
        opcao = obter_opcao(quant_opcoes)
            
        if opcao == 1:
            lista_hospitais()
        elif opcao == 2:
            lista_Medicos_Hospital()
        elif opcao == 3:
            lista_Enfermeiras_Hospital()
        elif opcao == 0:
            break
        else:
            valido = False

def lista_hospitais():
    titulo = 'LISTA DE HOSPITAIS'
    
    comando = '''SELECT * FROM Hospital'''
    hospitais = pega_info_db(comando)
    
    qnt_linhas = 36
    if len(hospitais) != 0:
        limpa_tela()
        imprime_titulo(titulo, qnt_linhas)
        for hospital in hospitais:
            print(f'Nome: {hospital[1]}')
            print(f'CNPJ: {hospital[0]}')
            print('Endereco:')
            print(f'         Rua: {hospital[2]}')
            print(f'         Bairro: {hospital[3]}')
            print(f'         Cidade: {hospital[4]}')
            print(f'         CEP: {hospital[5]}')
            print(f'Telefone: {hospital[6]}')
            imprime_linha(qnt_linhas)
        pausa()  
    else:
        mensagem = 'Ainda não há Hospitais Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)
        
def lista_Medicos_Hospital():
    titulo = 'HOSPITAL X MEDICOS'
    tam_linha = 36
    
    comando = '''SELECT * FROM Hospital'''
    hospitais = pega_info_db(comando)
    
    if len(hospitais) != 0:
        valido = True
        while True:
            limpa_tela()
            
            imprime_titulo(titulo, tam_linha)
            for i, hospital in enumerate(hospitais):
                print(f'{i + 1} - {hospital[1]}')
            imprime_linha(tam_linha)
            print('0 - Voltar')
            imprime_linha(tam_linha)
            
            if not valido:
                mensagem_input_invalido('Opcao Invalida!')
                valido = True
            
            opcao = obter_opcao(len(hospitais))
            
            if opcao == -1:
                valido = False
            else:
                break
        
        if opcao != 0:
            comando = '''SELECT Medico.crm, Medico.nome FROM Medico JOIN Hospital_x_Medico h_m ON Medico.crm = h_m.crm WHERE h_m.cnpj = :cnpj;'''
            medicos = pega_info_db(comando, {"cnpj": hospitais[opcao - 1][0]})
            
            if medicos != []:
                limpa_tela()
                imprime_titulo(titulo, tam_linha)
                for medico in medicos:
                    print(f'Nome: {medico[1]}')
                    print(f'CRM: {medico[0]}')
                    imprime_linha(tam_linha)
                pausa()
            else:
                mensagem = 'Ainda não há Medicos Cadastrados neste Hospital!'
                mensagem_query_vazia(titulo, mensagem)
    else:
        mensagem = 'Ainda não há Hospitais Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)

def lista_Enfermeiras_Hospital():
    titulo = 'HOSPITAL X ENFERMEIRAS'
    tam_linha = 36
    
    comando = '''SELECT * FROM Hospital'''
    hospitais = pega_info_db(comando)
    
    if len(hospitais) != 0:
        valido = True
        while True:
            limpa_tela()
            
            imprime_titulo(titulo, tam_linha)
            for i, hospital in enumerate(hospitais):
                print(f'{i + 1} - {hospital[1]}')
            imprime_linha(tam_linha)
            print('0 - Voltar')
            imprime_linha(tam_linha)
            
            if not valido:
                mensagem_input_invalido('Opcao Invalida!')
                valido = True
            
            opcao = obter_opcao(len(hospitais))
            
            if opcao == -1:
                valido = False
            else:
                cnpj_hospital = hospitais[opcao - 1][0]
                break
        
        if opcao != 0:
            comando = '''SELECT e.coren, e.nome FROM Enfermeira e JOIN Hospital_x_Enfermeira h_e ON e.coren = h_e.coren WHERE h_e.cnpj = :cnpj;'''
            enfermeiras = pega_info_db(comando, {"cnpj": cnpj_hospital})
            
            if enfermeiras != []:
                limpa_tela()
                imprime_titulo(titulo, tam_linha)
                for enfermeira in enfermeiras:
                    print(f'Nome: {enfermeira[1]}')
                    print(f'COREN: {enfermeira[0]}')
                    imprime_linha(tam_linha)
                pausa()
            else:
                mensagem = 'Ainda não há Enfermeiras Cadastradas neste Hospital!'
                mensagem_query_vazia(titulo, mensagem)
    else:
        mensagem = 'Ainda não há Hospitais Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)

#------------------------------------------------------

def altera_hospital():
    titulo = 'ALTERA HOSPITAL'
    
    comando = '''SELECT * FROM Hospital'''
    hospitais = pega_info_db(comando)
    
    qnt_hospitais = len(hospitais)
    
    if qnt_hospitais != 0:
        valido = True
        chave_hospital = ''
        while True: # obtem hospital
            limpa_tela()
            
            imprime_titulo(titulo)
            for i, hospital in enumerate(hospitais):
                print(f'{i + 1} - {hospital[1]}')
            imprime_linha()
            print('0 - Voltar')
            imprime_linha()
            
            if not valido:
                mensagem_input_invalido('Opcao Invalida!')
                valido = True
            
            opcao = obter_opcao(qnt_hospitais)
            
            if opcao == 0:
                break
            
            if opcao == -1:
                valido = False
            else:
                chave_hospital = hospitais[opcao - 1][0]
                nome_hospital = hospitais[opcao - 1][1]
                rua_hospital = hospitais[opcao - 1][2]
                bairro_hospital = hospitais[opcao - 1][3]
                cidade_hospital = hospitais[opcao - 1][4]
                cep_hospital = hospitais[opcao - 1][5]
                telefone_hospital = hospitais[opcao - 1][6]
                break
        
        if opcao != 0:
            tipo_dado = ''
            dado = ''
            while True: # obtem dado
                limpa_tela()
                
                imprime_titulo(titulo)
                print('Qual dado deseja alterar?')
                imprime_linha()
                print(f'1 - Nome ({nome_hospital})')
                print('2 - Endereco')
                print(f'3 - Telefone ({telefone_hospital})')
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
                        valido = True
                        while True:
                            limpa_tela()
                            
                            imprime_titulo(titulo)
                            print('Qual dado do Endereco?')
                            imprime_linha()
                            print(f'1 - Rua ({rua_hospital})')
                            print(f'2 - Bairro ({bairro_hospital})')
                            print(f'3 - Cidade ({cidade_hospital})')
                            print(f'4 - CEP ({cep_hospital})')
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
                    elif opcao == 3:
                        tipo_dado = 'telefone'
                        dado = obter_telefone(titulo)
                        break
                    elif opcao == 0:
                        break
                    else:
                        valido = False
            
            if dado != 0 and opcao != 0:
                comando = '''UPDATE Hospital SET {coluna} = :dado WHERE cnpj = :cnpj'''.format(coluna=tipo_dado)
                dados = {'cnpj': chave_hospital, 'dado': dado}
                
                atualizado = altera_db(comando, dados)
                if atualizado:
                    mensagem_sucesso(titulo, 'Hospital', 'Alterado')
                else:
                    mensagem_erro(titulo, 'Hospital', 'Alterar')
    else:
        mensagem = 'Ainda não há Hospitais Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)

#------------------------------------------------------

def exclui_hospital():
    titulo = 'EXCLUIR HOSPITAL'
    
    comando = '''SELECT * FROM Hospital'''
    hospitais = pega_info_db(comando)
    
    qnt_hospitais = len(hospitais)
    
    if qnt_hospitais != 0:
        valido = True
        while True:
            limpa_tela()
            
            imprime_titulo(titulo)
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
                cnpj_hospital = hospitais[opcao - 1][0]
                break
        
        if opcao != 0:
            comando = '''DELETE FROM Hospital WHERE cnpj=:cnpj'''
            excluido = altera_db(comando, {'cnpj':cnpj_hospital})
            
            if excluido:
                mensagem_sucesso(titulo, 'Hospital', 'Excluido')
            else:
                mensagem_erro(titulo, 'Hospital', 'Excluir')
    else:
        mensagem = 'Ainda não há Hospitais Cadastrados!'
        mensagem_query_vazia(titulo, mensagem)

def exclui_dependencias():
    pass
   
#------------------------------------------------------