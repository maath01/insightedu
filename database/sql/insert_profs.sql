
INSERT INTO professores (id, nome, email, senha, uf, data_nascimento, cpf, idade) VALUES
(199568921436, 'Ana Silva Souza', 'ana.silva@gmail.com', 'anass123', 'CE', '01-01-1995', '058.942.809-21', 39),
(199868921543, 'Roberto Gonçalves', 'roberto.goncalves@gmail.com', '12345678', 'CE', '20-04-1998', '921.748.910-21', 36),
(199268921821, 'Diego Morais', 'diego.morais@gmail.com', '12345678', 'CE', '07-08-1992', '735.891.318-97', 42);

INSERT INTO escolas_professores (escolas_id, professores_id) VALUES 
(68921, 199568921436),
(68921, 199868921543),
(68921, 199268921821);


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