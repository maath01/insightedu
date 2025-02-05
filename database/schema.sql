CREATE TABLE professores (
    id BIGINT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(15) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    data_nascimento DATE NOT NULL,
    cpf VARCHAR(15) NOT NULL,
    idade int NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE alunos (
    id BIGINT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    senha VARCHAR(15) NOT NULL,
    data_nascimento DATE NOT NULL,
    ano_matricula YEAR NOT NULL,
    cpf VARCHAR(15) NOT NULL,
    idade int NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE turmas (
    id BIGINT NOT NULL,
    serie int NOT NULL,
    letra VARCHAR(1),
    PRIMARY KEY(id)
);

CREATE TABLE materias (
    id int NOT NULL,
    nome VARCHAR(1),
    PRIMARY KEY(id)
);

CREATE TABLE ufs (
    id int NOT NULL,
    nome VARCHAR(20),
    sigla VARCHAR(2)
);

CREATE TABLE escolas(
    id BIGINT NOT NULL,
    nome VARCHAR (30) NOT NULL,
    cidade VARCHAR (30) NOT NULL,
    uf VARCHAR (3) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE gestores (
    id BIGINT NOT NULL,
    nome VARCHAR (30) NOT NULL,
    email VARCHAR (20) NOT NULL,
    nascimento DATE NOT NULL,
    senha VARCHAR (15) NOT NULL,
    cpf VARCHAR(15) NOT NULL,
    idade int NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE coordenadores (
    id BIGINT NOT NULL,
    nome VARCHAR (30) NOT NULL,
    email VARCHAR (20) NOT NULL,
    nascimento DATE NOT NULL,
    senha VARCHAR (15) NOT NULL,
    cpf VARCHAR(15) NOT NULL,
    idade int NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE avaliacoes (
    id BIGINT NOT NULL,
    serie int NOT NULL,
    bimestre int NOT NULL,
    professor_id BIGINT NOT NULL,
    turma_id BIGINT NOT NULL,
    data_aplicacao DATE,
    PRIMARY KEY(id)
);

CREATE TABLE notas (
    id BIGINT NOT NULL,
    aluno_id BIGINT NOT NULL,
    avaliacao_id BIGINT NOT NULL,
    nota REAL NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE descritores_port (
    id int NOT NULL,
    habilidade VARCHAR(100) NOT NULL,
    serie int NOT NULL,
    numero int NOT NULL,
    materia VARCHAR(15) DEFAULT 'Português',
    PRIMARY KEY(id)
);

CREATE TABLE descritores_mat (
    id INTEGER PRIMARY KEY,
    habilidade VARCHAR (100) NOT NULL,
    serie INT NOT NULL,
    numero INT NOT NULL,
    materia VARCHAR (25) DEFAULT 'Matemática'
);

CREATE TABLE questoes (
    id BIGINT NOT NULL,
    enunciado VARCHAR(150) NOT NULL,
    serie int NOT NULL,
    materia int NOT NULL,
    assunto int NOT NULL,
    PRIMARY KEY(id)
);

-- Tabelas de conexão
CREATE TABLE turmas_alunos (
    turmas_id BIGINT NOT NULL,
    alunos_id BIGINT NOT NULL
);

CREATE TABLE professores_turmas_materias (
    professores_id BIGINT NOT NULL,
    turmas_id BIGINT NOT NULL,
    materias_id BIGINT NOT NULL
);

CREATE TABLE escolas_gestores(
    escolas_id BIGINT NOT NULL,
    gestores_id BIGINT NOT NULL
);

CREATE TABLE escolas_turmas(
    escolas_id BIGINT NOT NULL,
    turmas_id BIGINT NOT NULL
);

CREATE TABLE escolas_coordenadores(
    escolas_id BIGINT NOT NULL,
    coordenadores_id BIGINT NOT NULL
);

CREATE TABLE escolas_professores(
    escolas_id BIGINT NOT NULL,
    professores_id BIGINT NOT NULL
);

CREATE TABLE escolas_alunos(
    escolas_id BIGINT NOT NULL,
    alunos_id BIGINT NOT NULL
);

CREATE TABLE coordenadores_turmas (
    coordenadores_id BIGINT NOT NULL,
    turmas_id BIGINT NOT NULL
);

CREATE TABLE materias_avaliacoes (
    materias_id int NOT NULL,
    avaliacoes_id BIGINT NOT NULL
);

-- Tabela de domínio de descritores para português
CREATE TABLE dominio_descritores_port ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,        
    aluno_id INT NOT NULL,                    
    descritor_1 INT NOT NULL,                          
    descritor_2 INT NOT NULL,                          
    descritor_3 INT NOT NULL,                           
    descritor_4 INT NOT NULL,                           
    descritor_5 INT NOT NULL,                           
    descritor_6 INT NOT NULL,                           
    descritor_7 INT NOT NULL,                           
    descritor_8 INT NOT NULL,                           
    descritor_9 INT NOT NULL,                           
    descritor_10 INT NOT NULL,                         
    descritor_11 INT NOT NULL,                          
    descritor_12 INT NOT NULL,                           
    descritor_13 INT NOT NULL,                        
    descritor_14 INT NOT NULL,                          
    descritor_15 INT NOT NULL,                          
    descritor_16 INT NOT NULL,                           
    descritor_17 INT NOT NULL,                          
    descritor_18 INT NOT NULL,                          
    descritor_19 INT NOT NULL,                           
    descritor_20 INT NOT NULL,                          
    descritor_21 INT NOT NULL,                         
    descritor_22 INT NOT NULL,                           
    descritor_23 INT NOT NULL,                          
    descritor_24 INT NOT NULL,                        
    descritor_25 INT NOT NULL,                        
    descritor_26 INT NOT NULL,                          
    descritor_27 INT NOT NULL,                          
    descritor_28 INT NOT NULL,                       
    descritor_29 INT NOT NULL                           
);

-- Tabela de domínio de descritores para matemática
CREATE TABLE dominio_descritores_mat (
    id INTEGER PRIMARY KEY AUTOINCREMENT,        
    aluno_id INT NOT NULL,                    
    descritor_1 INT NOT NULL,                          
    descritor_2 INT NOT NULL,                          
    descritor_3 INT NOT NULL,                           
    descritor_4 INT NOT NULL,                           
    descritor_5 INT NOT NULL,                           
    descritor_6 INT NOT NULL,                           
    descritor_7 INT NOT NULL,                           
    descritor_8 INT NOT NULL,                           
    descritor_9 INT NOT NULL,                           
    descritor_10 INT NOT NULL,                         
    descritor_11 INT NOT NULL,                          
    descritor_12 INT NOT NULL,                           
    descritor_13 INT NOT NULL,                        
    descritor_14 INT NOT NULL,                          
    descritor_15 INT NOT NULL,                          
    descritor_16 INT NOT NULL,                           
    descritor_17 INT NOT NULL,                          
    descritor_18 INT NOT NULL,                          
    descritor_19 INT NOT NULL,                           
    descritor_20 INT NOT NULL,                          
    descritor_21 INT NOT NULL,                         
    descritor_22 INT NOT NULL,                           
    descritor_23 INT NOT NULL,                          
    descritor_24 INT NOT NULL,                        
    descritor_25 INT NOT NULL,                        
    descritor_26 INT NOT NULL,                          
    descritor_27 INT NOT NULL,                          
    descritor_28 INT NOT NULL,                       
    descritor_29 INT NOT NULL, 
    descritor_30 INT NOT NULL, 
    descritor_31 INT NOT NULL 
);