from database.banco import connect_db

class Aluno:
    """Modelo de dados da tabela alunos"""

    def __init__(self, al_id, nome, senha, data_nascimento) -> None:
        self.al_id = al_id
        self.nome = nome
        self.senha = senha
        self.data_nascimento = data_nascimento

    def __str__(self) -> str:
        return str(self.al_id) + ' ' + self.nome
    

def list_students():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM alunos')
    alunos_1 = cursor.fetchall() # Lista com os dados da tabela
    alunos_2: list[Aluno] = [] # Lista de Objetos(Aluno) com os dados da tabela

    for aluno in alunos_1:
        alunos_2.append(Aluno(aluno[0], aluno[1], aluno[2], aluno[3]))

    connection.close()

    return alunos_2
