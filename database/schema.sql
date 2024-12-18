CREATE TABLE professores (
    id BIGINT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(15) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    data_nascimento DATE NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE alunos (
    id BIGINT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    senha VARCHAR(15) NOT NULL,
    data_nascimento DATE NOT NULL,
    ano_matricula YEAR NOT NULL,
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
    PRIMARY KEY (id)
);

CREATE TABLE coordenadores (
    id BIGINT NOT NULL,
    nome VARCHAR (30) NOT NULL,
    email VARCHAR (20) NOT NULL,
    nascimento DATE NOT NULL,
    senha VARCHAR (15) NOT NULL,
    PRIMARY KEY (id)
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