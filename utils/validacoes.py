from utils.db_operacoes import pega_info_db

def valida_nome(nome:str):
    for letra in nome:
        if not letra.isalpha() and not letra.isspace():
            return False
    return True

def valida_cpf(cpf:str):
    # xxx.xxx.xxx-xx
    if len(cpf) != 14:
        return False
    
    for i in range(len(cpf)):
        if i not in [3, 7, 11]:
            if not cpf[i].isdigit():
                return False
        elif i in [3, 7] and cpf[i] != '.':
            return False
        elif i == 10 and cpf[i] != '-':
            return False
    
    return True

def valida_cnpj(cnpj:str):
    # xx.xxx.xxx/xxxx-xx
    if len(cnpj) != 18:
        return False

    for i in range(len(cnpj)):
        if i not in [2, 6, 10, 15]:
            if not cnpj[i].isdigit():
                return False
        elif i in [2, 6] and cnpj[i] != '.':
            return False
        elif i == 10 and cnpj[i] != '/':
            return False
        elif i == 15 and cnpj[i] != '-':
            return False
    
    return True

def valida_telefone(telefone:str):
    # XXXXX-XXXX
    if len(telefone) != 10:
        return False

    for i in range(len(telefone)):
        if i == 5 :
            if telefone[i] != '-':
                return False
        else:
            if not telefone[i].isdigit():
                return False
    
    return True

def valida_cep(cep:str):
    # xxxxx-xxx
    if len(cep) != 9:
        return False

    for i in range(len(cep)):
        if i == 5:
            if cep[i] != '-':
                return False
        else:
            if not cep[i].isdigit:
                return False
    
    return True

def valida_crm(crm:str):
    # xxxx/UF
    if len(crm) != 7:
        return False

    for i in range(len(crm)):
        if i < 4 and not crm[i].isdigit():
            return False
        if i == 4 and crm[i] != '/':
            return False
        if i > 4 and not crm[i].isalpha():
            return False
        
    if not valida_uf(f'{crm[5]}{crm[6]}'):
        return False
    
    return True

def valida_rg(rg:str):
    # x.xxx.xxx-x
    if len(rg) != 11:
        return False
    
    for i in range(len(rg)):
        if i not in [1, 5, 9]:
            if not rg[i].isdigit():
                return False
        elif i in [1, 5] and rg[i] != '.':
            return False
        elif i == 9 and rg[i] != '-':
            return False
    
    return True

def valida_coren(coren:str):
    # xxx.xxx.xxx
    if len(coren) != 11:
        return False
    
    for i in range(len(coren)):
        if i in [3, 7]:
            if coren[i] != '.':
                return False
        else:
            if not coren[i].isdigit():
                return False
    
    return True
    
def valida_cid(cid:str):
    if len(cid) != 3:
        return False

    if not cid[0].isalpha():
        return False
    
    if not cid[1].isdigit() or not cid[2].isdigit():
        return False
    
    return True

def valida_uf(uf:str):
    estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE',
               'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 
               'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 
               'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 
               'SE', 'TO', 'DF']
    
    return uf.upper() in estados

def dado_ja_cadastrado(tabela:str, nome_dado:str, dado):
    comando = f'SELECT {nome_dado} FROM {tabela}'
    registros = pega_info_db(comando)
    
    cadastrados = []
    for registro in registros:
        cadastrados.append(registro[0])  
    
    return True if dado in cadastrados else False