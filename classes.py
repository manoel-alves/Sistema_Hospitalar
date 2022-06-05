class Endereco():
    def __init__(self, rua:str, bairro:str, cidade:str, cep:str):
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

class Hospital():
    def __init__(self, cnpj:str, nome:str, endereco:Endereco, telefone:str):
        self.cnpj = cnpj
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

class Medico():
    def __init__(self, crm:str, cpf:str, nome:str, endereco:Endereco, especialidade:list):
        self.crm = crm
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.especialidade = especialidade

class Enfermeira():
    def __init__(self):
        pass    
    
class Paciente():
    def __init__(self):
        pass

class Tratamento():
    def __init__(self):
        pass