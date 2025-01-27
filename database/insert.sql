INSERT INTO escolas (id, nome, cidade, uf) VALUES
(68921, 'IFCE', 'Crato', 'CE'),
(60932, 'Maria Violeta Arraes', 'Crato', 'CE');

INSERT INTO professores (id, nome, email, senha, uf, data_nascimento, cpf, idade) VALUES
(199568921436, 'Ana Silva Souza', 'ana.silva@gmail.com', 'anass123', 'CE', '01-01-1995', '058.942.809-21', 39),
(199868921543, 'Roberto Gonçalves', 'roberto.goncalves@gmail.com', '12345678', 'CE', '20-04-1998', '921.748.910-21', 36),
(199260932821, 'Diego Morais', 'diego.morais@gmail.com', '12345678', 'CE', '07-08-1992', '735.891.318-97', 42);

INSERT INTO escolas_professores (escolas_id, professores_id) VALUES (68921, 199568921436), (68921, 199868921543), (60932, 199260932821);

INSERT INTO coordenadores (id, nome, email, nascimento, senha, cpf, idade) VALUES (198968921329, 'Gabriel', 'gabriel@gmail.com', '04-05-1989', '12345678', '892.309.280-91', 36);
INSERT INTO escolas_coordenadores (escolas_id, coordenadores_id) VALUES (68921, 198968921329);

INSERT INTO gestores (id, nome, email, nascimento, senha, cpf, idade) VALUES (198968921543, 'Gabriela', 'gabriela@gmail.com', '04-05-1989', '12345678', '738.927.121-65', 36);
INSERT INTO escolas_gestores (escolas_id, gestores_id) VALUES (68921, 198968921543);

INSERT INTO alunos (id, nome, senha, data_nascimento, ano_matricula, cpf, idade) VALUES 
(2010689216742, 'Matheus Soares do Nascimento', '12345678', '02-10-2004', '2010', '192.281.218-21', 20),
(2008689215321, 'Suyane Oliveira da Silva', 'abcdefgh', '08-10-2003', '2008', '213.312.653-98', 21),
(2010689215413, 'Taislene da Silva Gonçalves', 'abcdefgh', '03-10-2004', '2010', '812.391.823-32', 20),
(2007689216223, 'Rozane Raquel da Silva Gonçalves', 'abcdefgh', '10-06-2002', '2007', '307.823.029.80', 22);

INSERT INTO turmas (id, serie, letra) VALUES (689211426, 1, 'A'), (689211832, 1, 'B');
INSERT INTO turmas_alunos (turmas_id, alunos_id) VALUES 
(689211426, 2010689216742),
(689211426, 2008689215321),
(689211832, 2010689215413),
(689211832, 2007689216223);
INSERT INTO escolas_turmas (escolas_id, turmas_id) VALUES (68921, 689211426), (68921, 689211832);
INSERT INTO escolas_alunos (escolas_id, alunos_id) VALUES
(68921, 2010689216742),
(68921, 2008689215321),
(68921, 2010689215413),
(68921, 2007689216223);

INSERT INTO materias (id, nome) VALUES 
(1, 'Português'),
(2, 'Matematica'),
(3, 'Ciencias'),
(4, 'Historia'),
(5, 'Geografia');

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
(199568921436, 689211426, 1),
(199568921436, 689211426, 2),
(199568921436, 689211426, 3),
(199568921436, 689211426, 4),
(199568921436, 689211426, 5),
(199868921543, 689211832, 1),
(199868921543, 689211832, 3),
(199868921543, 689211832, 4),
(199868921543, 689211832, 5);

INSERT INTO avaliacoes (id, serie, bimestre, professor_id, turma_id, data_aplicacao) VALUES
(12393742, 1, 2, 199568921436, 689211426, '20-06-2024'),
(14174829, 1, 4, 199868921543, 689211832, '20-06-2024');
INSERT INTO materias_avaliacoes (materias_id, avaliacoes_id) VALUES (3, 12393742), (1, 14174829);

INSERT INTO notas (id, aluno_id, avaliacao_id, nota) VALUES
(201068921674212343, 2010689216742, 12393742, 8.9),
(200868921532112362, 2008689215321, 12393742, 8.5),
(201068921541314156, 2010689215413, 14174829, 6.7),
(200768921622314198, 2007689216223, 14174829, 7.4);


INSERT INTO descritores_port (id, habilidade, serie, numero) VALUES
(1, 'Identificar letras entre desenhos números e outros simbolos graficos', 1, 1),
(2, 'Reconhecer as letras do alfabeto', 1, 2)