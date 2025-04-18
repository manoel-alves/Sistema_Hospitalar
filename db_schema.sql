CREATE TABLE IF NOT EXISTS Hospital (
    cnpj TEXT NOT NULL PRIMARY KEY,
    nome TEXT NOT NULL,
    rua TEXT NOT NULL, 
    bairro TEXT NOT NULL, 
    cidade TEXT NOT NULL, 
    cep TEXT NOT NULL, 
    telefone TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Especialidade (
    id_especialidade INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Medico (
    crm TEXT NOT NULL PRIMARY KEY, 
    cpf TEXT NOT NULL, 
    nome TEXT NOT NULL, 
    rua TEXT NOT NULL, 
    bairro TEXT NOT NULL, 
    cidade TEXT NOT NULL, 
    cep TEXT NOT NULL, 
    fk_especialidade INTEGER NOT NULL, 
    FOREIGN KEY(fk_especialidade) REFERENCES Especialidade(id_especialidade)
);

CREATE TABLE IF NOT EXISTS Telefone (
    id_telefone INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    numero TEXT NOT NULL, 
    crm TEXT NOT NULL, 
    FOREIGN KEY (crm) REFERENCES Medico (crm)
);

CREATE TABLE IF NOT EXISTS Hospital_x_Medico (
    cnpj TEXT NOT NULL,
    crm TEXT NOT NULL,
    PRIMARY KEY (cnpj, crm),
    FOREIGN KEY (cnpj) REFERENCES Hospital (cnpj),
    FOREIGN KEY (crm) REFERENCES Medico (crm)
);

CREATE TABLE IF NOT EXISTS Enfermeira (
    coren TEXT NOT NULL PRIMARY KEY,
    cpf TEXT NOT NULL, 
    nome TEXT NOT NULL, 
    rua TEXT NOT NULL, 
    bairro TEXT NOT NULL, 
    cidade TEXT NOT NULL, 
    cep TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Hospital_x_Enfermeira (
    cnpj TEXT NOT NULL,
    coren TEXT NOT NULL, 
    PRIMARY KEY (cnpj, coren),
    FOREIGN KEY (cnpj) REFERENCES Hospital (cnpj), 
    FOREIGN KEY (coren) REFERENCES Enfermeira (coren)
);

CREATE TABLE IF NOT EXISTS Medico_x_Enfermeira (
    crm TEXT NOT NULL, 
    coren TEXT NOT NULL, 
    PRIMARY KEY (crm, coren), 
    FOREIGN KEY (crm) REFERENCES Medico (crm), 
    FOREIGN KEY (coren) REFERENCES Enfermeira (coren)
);

CREATE TABLE IF NOT EXISTS Paciente (
    cpf TEXT NOT NULL PRIMARY KEY, 
    rg TEXT NOT NULL, 
    nome TEXT NOT NULL, 
    rua TEXT NOT NULL, 
    bairro TEXT NOT NULL, 
    cidade TEXT NOT NULL, 
    cep TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Tratamento (
    id_tratamento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    fk_cpf TEXT NOT NULL, 
    fk_crm TEXT NOT NULL, 
    cid TEXT NOT NULL, 
    data TEXT NOT NULL, 
    FOREIGN KEY (fk_cpf) REFERENCES Paciente (cpf), 
    FOREIGN KEY (fk_crm) REFERENCES Medico (crm)
);

CREATE TABLE IF NOT EXISTS Paciente_x_Tratamento(
    cpf TEXT NOT NULL, 
    id_tratamento INTEGER NOT NULL, 
    PRIMARY KEY (cpf, id_tratamento), 
    FOREIGN KEY (cpf) REFERENCES Paciente (cpf), 
    FOREIGN KEY (id_tratamento) REFERENCES Tratamento (id_tratamento)
);

CREATE TABLE IF NOT EXISTS Medico_x_Paciente (
    crm TEXT NOT NULL,
    cpf TEXT NOT NULL, 
    PRIMARY KEY (crm, cpf), 
    FOREIGN KEY (crm) REFERENCES Medico (crm), 
    FOREIGN KEY (cpf) REFERENCES Paciente (cpf)
);