import sqlite3 as sqlite

from utils.geral import *

DB = 'database.db'
DB_SCHEMA = 'db_schema.sql'

def inicializa_database():
    conexao = None
    cursor = None
    try:
        conexao = sqlite.connect(DB)
        conexao.execute('PRAGMA foreign_keys = on')
        cursor = conexao.cursor()

        try:
            with open(DB_SCHEMA, 'r', encoding='utf-8') as arquivo_comandos:
                sql_script = arquivo_comandos.read()
                cursor.executescript(sql_script)
        except FileNotFoundError as erro1:
            print(f'ERRO: {erro1}')
            
        conexao.commit()        
    except sqlite.DatabaseError as erro:
        print(f'ERRO: {erro}')
        pausa()
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
            
def altera_db(comando:str, dados={}):
    conexao = None
    cursor = None
    resultado = True
    try:
        conexao = sqlite.connect(DB)
        cursor = conexao.cursor()
        
        cursor.execute(comando, dados)
        
        conexao.commit()
        
        resultado = True
    except sqlite.IntegrityError as erro:
        limpa_tela()
        print(f'Dado já cadastrado: {erro}')
        pausa()
        resultado = False
    except sqlite.DatabaseError as erro:
        limpa_tela()
        print(f'Erro Inesperado: {erro}')
        pausa()
        resultado = False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
        return resultado

def pega_info_db(comando:str, dados={}):
    conexao = None
    cursor = None
    registros = []
    try:
        conexao = sqlite.connect(DB)
        cursor = conexao.cursor()
        
        if dados == {}:
            cursor.execute(comando)
        else:
            cursor.execute(comando, dados)
        
        registros = cursor.fetchall()
        
    except sqlite.DatabaseError as erro:
        print(erro)
        pausa()
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
        return registros
