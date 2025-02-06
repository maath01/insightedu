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
(13364342, 1, 3, 199568921436, 689211426, '20-06-2024'),
(14348723, 1, 4, 199568921436, 689211426, '20-06-2024'),
(14174829, 1, 4, 199868921543, 689211832, '20-06-2024');
INSERT INTO materias_avaliacoes (materias_id, avaliacoes_id) VALUES
(3, 12393742),
(3, 13364342),
(3, 14348723),
(1, 14174829);

INSERT INTO notas (id, aluno_id, avaliacao_id, nota) VALUES
(201068921674212343, 2010689216742, 12393742, 8.9),
(201068921674213354, 2010689216742, 13364342, 9.1),
(201068921674214321, 2010689216742, 14348723, 10.0),
(200868921532113365, 2008689215321, 13364342, 7.4),
(200868921532114378, 2008689215321, 14348723, 8.9),
(200868921532112362, 2008689215321, 12393742, 8.5),
(201068921541314156, 2010689215413, 14174829, 6.7),
(200768921622314198, 2007689216223, 14174829, 7.4);

INSERT INTO descritores_port (id, habilidade, serie, numero) VALUES
(1, 'Reconhecer que textos são lidos e escritos da esquerda para a direita e de cima para baixo da página', 1, 1),
(2, 'Escrever, espontaneamente ou por ditado, palavras e frases de forma alfabética – usando letras/grafemas que representem fonemas', 1, 2),
(3, 'Observar escritas convencionais, comparando-as às suas produções escritas, percebendo semelhanças e diferenças', 1, 3),
(4, 'Distinguir as letras do alfabeto de outros sinais gráficos', 1, 4),
(5, 'Reconhecer o sistema de escrita alfabética como representação dos sons da fala', 1, 5),
(6, 'Utilizar, ao produzir o texto, grafia correta de palavras conhecidas ou com estruturas silábicas já dominadas', 2, 6),
(7, 'Segmentar palavras em sílabas e remover e substituir sílabas iniciais, mediais ou finais para criar novas palavras', 2, 7),
(8, 'Ler e escrever palavras com correspondências regulares diretas entre letras e fonemas', 2, 8),
(9, 'Ler e escrever corretamente palavras com sílabas CV, V, CVC, CCV, identificando que existem vogais em todas as sílabas', 2, 9),
(10, 'Ler e escrever corretamente palavras com marcas de nasalidade', 2, 10),
(11, 'Ler e escrever palavras com correspondências regulares contextuais entre grafemas e fonemas', 3, 11),
(12, 'Ler e escrever corretamente palavras com sílabas CV, V, CVC, CCV, VC, VV, CVV', 3, 12),
(13, 'Ler e escrever corretamente palavras com os dígrafos lh, nh, ch', 3, 13),
(14, 'Usar acento gráfico em monossílabos tônicos e palavras oxítonas', 3, 14),
(15, 'Identificar o número de sílabas de palavras, classificando-as em monossílabas, dissílabas, trissílabas e polissílabas', 3, 15),
(16, 'Grafar palavras utilizando regras de correspondência fonema-grafema regulares diretas e contextuais', 4, 16),
(17, 'Leitura e escrita de palavras com sílabas VV e CVV em casos nos quais a combinação VV é reduzida na língua oral', 4, 17),
(18, 'Localizar palavras no dicionário para esclarecer significados', 4, 18),
(19, 'Usar acento gráfico em paroxítonas terminadas em -i(s), -l, -r, -ão(s)', 4, 19),
(20, 'Identificar a função na leitura e usar adequadamente sinais de pontuação', 4, 20),
(21, 'Grafar palavras utilizando regras de correspondência fonema-grafema e palavras de uso frequente com correspondências irregulares', 5, 21),
(22, 'Identificar o caráter polissêmico das palavras, comparando diferentes significados conforme o contexto', 5, 22),
(23, 'Acentuar corretamente palavras oxítonas, paroxítonas e proparoxítonas', 5, 23),
(24, 'Diferenciar, na leitura de textos, vírgula, ponto e vírgula, dois-pontos e reticências', 5, 24),
(25, 'Identificar a expressão de presente, passado e futuro em tempos verbais do modo indicativo', 5, 25),
(26, 'Reconhecer a impossibilidade de uma neutralidade absoluta no relato de fatos e identificar graus de parcialidade', 6, 26),
(27, 'Estabelecer relação entre os diferentes gêneros jornalísticos, compreendendo a centralidade da notícia', 6, 27),
(28, 'Analisar diferenças de sentido entre palavras de uma série sinonímica', 6, 28),
(29, 'Analisar a função e as flexões de substantivos, adjetivos e verbos nos modos indicativo, subjuntivo e imperativo', 6, 29),
(30, 'Identificar os efeitos de sentido dos modos verbais conforme gênero textual e intenção comunicativa', 6, 30),
(31, 'Distinguir diferentes propostas editoriais e identificar recursos que impactam o leitor', 7, 31),
(32, 'Comparar notícias e reportagens sobre um mesmo fato divulgadas em diferentes mídias', 7, 32),
(33, 'Formar palavras derivadas com os prefixos e sufixos mais produtivos no português', 7, 33),
(34, 'Reconhecer, em textos, o verbo como o núcleo das orações', 7, 34),
(35, 'Identificar verbos de predicação completa e incompleta em orações de textos lidos ou produzidos', 7, 35),
(36, 'Identificar e comparar as várias editorias de jornais impressos e digitais', 8, 36),
(37, 'Justificar diferenças ou semelhanças no tratamento de uma informação em diferentes textos', 8, 37),
(38, 'Produzir artigos de opinião com defesa de um ponto de vista e argumentos adequados', 8, 38),
(39, 'Utilizar conhecimentos linguísticos e gramaticais na produção textual', 8, 39),
(40, 'Analisar processos de formação de palavras por composição e regras de uso do hífen', 8, 40),
(41, 'Analisar a disseminação de notícias falsas nas redes sociais e estratégias para reconhecê-las', 9, 41),
(42, 'Analisar e comentar a cobertura da imprensa sobre fatos de relevância social', 9, 42),
(43, 'Produzir artigos de opinião assumindo posição diante de tema polêmico e utilizando argumentos diversos', 9, 43),
(44, 'Escrever textos corretamente, de acordo com a norma-padrão e com estruturas sintáticas complexas', 9, 44),
(45, 'Identificar, em textos lidos e em produções próprias, orações com a estrutura sujeito-verbo de ligação-predicativo', 9, 45);

INSERT INTO descritores_mat (id, habilidade, serie, numero) VALUES
(1, 'Utilizar números naturais como indicador de quantidade ou de ordem em diferentes situações cotidianas', 1, 1),
(2, 'Contar de maneira exata ou aproximada, utilizando diferentes estratégias como o pareamento e outros agrupamentos', 1, 2),
(3, 'Estimar e comparar quantidades de objetos de dois conjuntos para indicar "tem mais", "tem menos" ou "tem a mesma quantidade"', 1, 3),
(4, 'Contar a quantidade de objetos de coleções até 100 unidades e apresentar o resultado por registros verbais e simbólicos', 1, 4),
(5, 'Comparar números naturais de até duas ordens em situações cotidianas', 1, 5),
(6, 'Comparar e ordenar números naturais até a ordem de centenas', 2, 6),
(7, 'Fazer estimativas por meio de estratégias diversas e registrar o resultado da contagem de objetos', 2, 7),
(8, 'Comparar quantidades de objetos de dois conjuntos por estimativa e indicar diferenças', 2, 8),
(9, 'Compor e decompor números naturais de até três ordens', 2, 9),
(10, 'Construir fatos básicos da adição e subtração e utilizá-los no cálculo mental ou escrito', 2, 10),
(11, 'Ler, escrever e comparar números naturais até a unidade de milhar', 3, 11),
(12, 'Identificar características do sistema de numeração decimal', 3, 12),
(13, 'Estabelecer a relação entre números naturais e pontos da reta numérica', 3, 13),
(14, 'Utilizar diferentes procedimentos de cálculo mental e escrito para resolver problemas de adição e subtração', 3, 14),
(15, 'Resolver e elaborar problemas de adição e subtração utilizando diferentes estratégias de cálculo', 3, 15),
(16, 'Ler, escrever e ordenar números naturais até a ordem de dezenas de milhar', 4, 16),
(17, 'Mostrar que todo número natural pode ser escrito por adições e multiplicações por potências de dez', 4, 17),
(18, 'Resolver e elaborar problemas com números naturais envolvendo adição e subtração', 4, 18),
(19, 'Utilizar as relações entre adição e subtração, bem como entre multiplicação e divisão, para ampliar estratégias de cálculo', 4, 19),
(20, 'Utilizar as propriedades das operações para desenvolver estratégias de cálculo', 4, 20),
(21, 'Ler, escrever e ordenar números naturais até a ordem das centenas de milhar', 5, 21),
(22, 'Ler, escrever e ordenar números racionais na forma decimal', 5, 22),
(23, 'Identificar e representar frações menores e maiores que a unidade', 5, 23),
(24, 'Identificar frações equivalentes', 5, 24),
(25, 'Comparar e ordenar números racionais positivos na reta numérica', 5, 25),
(26, 'Comparar, ordenar, ler e escrever números naturais e racionais positivos na reta numérica', 6, 26),
(27, 'Reconhecer o sistema de numeração decimal e suas diferenças com outros sistemas', 6, 27),
(28, 'Resolver e elaborar problemas que envolvam cálculos com números naturais', 6, 28),
(29, 'Construir algoritmo e representá-lo por fluxograma para resolver um problema simples', 6, 29),
(30, 'Classificar números naturais em primos e compostos e estabelecer relações entre múltiplos e divisores', 6, 30),
(31, 'Resolver e elaborar problemas com números naturais envolvendo divisores e múltiplos', 7, 31),
(32, 'Resolver e elaborar problemas que envolvam porcentagens', 7, 32),
(33, 'Comparar e ordenar números inteiros e utilizá-los em operações', 7, 33),
(34, 'Resolver e elaborar problemas que envolvam operações com números inteiros', 7, 34),
(35, 'Resolver um mesmo problema utilizando diferentes algoritmos', 7, 35),
(36, 'Efetuar cálculos com potências de expoentes inteiros e usar notação científica', 8, 36),
(37, 'Resolver problemas usando a relação entre potenciação e radiciação', 8, 37),
(38, 'Resolver e elaborar problemas de contagem com o princípio multiplicativo', 8, 38),
(39, 'Resolver e elaborar problemas envolvendo cálculo de porcentagens', 8, 39),
(40, 'Reconhecer e utilizar procedimentos para obter uma fração geratriz de uma dízima periódica', 8, 40),
(41, 'Reconhecer que alguns segmentos de reta não têm medidas expressas por números racionais', 9, 41),
(42, 'Reconhecer um número irracional e estimar sua posição na reta numérica', 9, 42),
(43, 'Efetuar cálculos com números reais', 9, 43),
(44, 'Resolver e elaborar problemas com números reais em notação científica', 9, 44),
(45, 'Resolver e elaborar problemas envolvendo porcentagens sucessivas e taxas percentuais', 9, 45);

INSERT INTO dominio_descritores_port (id, aluno_id, descritor_1, descritor_2, descritor_3,  descritor_4, descritor_5, descritor_6, descritor_7, descritor_8, descritor_9, descritor_10, descritor_11, descritor_12, descritor_13, descritor_14, descritor_15, descritor_16, descritor_17, descritor_18, descritor_19, descritor_20, descritor_21, descritor_22, descritor_23, descritor_24, descritor_25, descritor_26, descritor_27, descritor_28, descritor_29, descritor_30, descritor_31, descritor_32, descritor_33, descritor_34, descritor_35, descritor_36, descritor_37, descritor_38, descritor_39, descritor_40, descritor_41, descritor_42, descritor_43, descritor_44, descritor_45) VALUES
(0, 2010689216742, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0),
(1, 2008689215321, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0);

INSERT INTO dominio_descritores_mat (id, aluno_id, descritor_1, descritor_2, descritor_3,  descritor_4, descritor_5, descritor_6, descritor_7, descritor_8, descritor_9, descritor_10, descritor_11, descritor_12, descritor_13, descritor_14, descritor_15, descritor_16, descritor_17, descritor_18, descritor_19, descritor_20, descritor_21, descritor_22, descritor_23, descritor_24, descritor_25, descritor_26, descritor_27, descritor_28, descritor_29, descritor_30, descritor_31, descritor_32, descritor_33, descritor_34, descritor_35, descritor_36, descritor_37, descritor_38, descritor_39, descritor_40, descritor_41, descritor_42, descritor_43, descritor_44, descritor_45) VALUES
(0, 2010689216742, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0),
(1, 2008689215321, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0);

INSERT INTO questoes (id, enunciado, serie, materia, assunto, resposta) VALUES
(51557832, 'Na frase "O gato preto dorme na cadeira.", qual é o substantivo e qual é o adjetivo?', 5, 'Português', 'Classes de palavras', 'Gato e preto'),
(51589712, 'Leia a frase abaixo e responda à pergunta. "Ana correu para a escola porque estava atrasada.", Por que Ana correu para a escola?', 5, 'Português', 'Interpretação de texto', 'Porque estava atrasada')
