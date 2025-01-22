INSERT INTO escolas 

INSERT INTO professores (id, nome, email, senha, uf, data_nascimento) VALUES (1, 'Ana Silva Souza', 'ana.silva@gmail.com', 'anass123', 'CE', '01-01-1995');
INSERT INTO professores (id, nome, email, senha, uf, data_nascimento) VALUES (2, 'Roberto Gonçalves', 'roberto.goncalves@gmail.com', '12345678', 'CE', '20-04-1998');

INSERT INTO coordenadores (id, nome, email, nascimento, senha) VALUES (1, 'Gabriel', 'gabriel@gmail.com', '04-05-1989', '12345678');

INSERT INTO gestores (id, nome, email, nascimento, senha) VALUES (1, 'Gabriela', 'gabriela@gmail.com', '04-05-1989', '12345678');

INSERT INTO alunos (id, nome, senha, data_nascimento, ano_matricula) VALUES (1, 'Matheus Soares do Nascimento', '12345678', '02-10-2004', '2010');
INSERT INTO alunos (id, nome, senha, data_nascimento, ano_matricula) VALUES (2, 'Suyane Oliveira da Silva', 'abcdefgh', '08-10-2003', '2008');
INSERT INTO alunos (id, nome, senha, data_nascimento, ano_matricula) VALUES (3, 'Taislene da Silva Gonçalves', 'abcdefgh', '03-10-2004', '2010');
INSERT INTO alunos (id, nome, senha, data_nascimento, ano_matricula) VALUES (4, 'Rozane Raquel da Silva Gonçalves', 'abcdefgh', '10-06-2002', '2007');

INSERT INTO turmas (id, serie, letra) VALUES (1, 1, 'A');
INSERT INTO turmas (id, serie, letra) VALUES (2, 1, 'B');

INSERT INTO materias (id, nome) VALUES (1, 'Português');
INSERT INTO materias (id, nome) VALUES (2, 'Matematica');
INSERT INTO materias (id, nome) VALUES (3, 'Ciencias');
INSERT INTO materias (id, nome) VALUES (4, 'Historia');
INSERT INTO materias (id, nome) VALUES (5, 'Geografia');

INSERT INTO turmas_alunos (turmas_id, alunos_id) VALUES (1, 2);
INSERT INTO turmas_alunos (turmas_id, alunos_id) VALUES (1, 1);
INSERT INTO turmas_alunos (turmas_id, alunos_id) VALUES (2, 3);
INSERT INTO turmas_alunos (turmas_id, alunos_id) VALUES (2, 4);

INSERT INTO ufs (id, nome, sigla) VALUES
(1, 'Acre', 'AC'),
(2, 'Alagoas', 'AL'),
(3, 'Amapá', 'AP'),
(4, 'Amazonas', 'AM'),
(5, 'Bahia', 'BA'),
(6, 'Ceará', 'CE'),
(7, 'Distrito Federal', 'DF'),
(8, 'Espírito Santo', 'ES'),
(9, 'Goiás', 'GO'),
(10, 'Maranhão', 'MA'),
(11, 'Mato Grosso', 'MT'),
(12, 'Mato Grosso do Sul', 'MS'),
(13, 'Minas Gerais', 'MG'),
(14, 'Pará', 'PA'),
(15, 'Paraíba', 'PB'),
(16, 'Paraná', 'PR'),
(17, 'Pernambuco', 'PE'),
(18, 'Piauí', 'PI'),
(19, 'Rio de Janeiro', 'RJ'),
(20, 'Rio Grande do Norte', 'RN'),
(21, 'Rio Grande do Sul', 'RS'),
(22, 'Rondônia', 'RO'),
(23, 'Roraima', 'RR'),
(24, 'Santa Catarina', 'SC'),
(25, 'São Paulo', 'SP'),
(26, 'Sergipe', 'SE'),
(27, 'Tocantins', 'TO');

INSERT INTO professores_turmas_materias (professores_id, turmas_id, materias_id) VALUES 
(1, 1, 1),
(1, 1, 2),
(1, 1, 3),
(1, 1, 4),
(1, 1, 5),
(2, 2, 1),
(2, 2, 2),
(2, 2, 3),
(2, 2, 4),
(2, 2, 5);

INSERT INTO avaliacoes (id, serie, bimestre, data_aplicacao) VALUES
(1, 5, 2, '20-06-2024'),
(2, 6, 4, '20-06-2024')
