from database.scripts.banco import connect_db
from database.scripts.connection_tables import escolas_gestores
import sqlite3
from random import randint

class Gestor:
    """Modelo de dados da tabela gestores"""
    
    def __init__(self, gestor_id=0, nome='', email='', nascimento='', senha='', cpf='', idade=0) -> None:
        self.gestor_id = gestor_id
        self.nome = nome
        self.email = email
        self.nascimento = nascimento
        self.senha = senha
        self.cpf = cpf
        self.idade = idade

    def __str__(self) -> str:
        return str(self.gestor_id) + ' ' + str(self.nome) 
    
def create(gestor: Gestor, escola):
    """Insere um novo gestor no banco de dados"""
    connection, cursor = connect_db()

    try:
        gestor_id = generate_manager_id(gestor, escola)

        cursor.execute('INSERT INTO gestores (id, nome, email, nascimento, senha, cpf, idade) VALUES (?, ?, ?, ?, ?, ?, ?)',
                        (gestor_id, gestor.nome, gestor.email, gestor.nascimento, gestor.senha, gestor.cpf, gestor.idade))
        connection.commit()

    except sqlite3.IntegrityError:
        print('ID duplicado')
    else:
        escolas_gestores(escola.escola_id, gestor_id, cursor, connection)
        gestor.gestor_id = gestor_id
    
    connection.close()

def list_managers():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM gestores')
    gestores_1 = cursor.fetchall() # Lista com os dados da tabela
    gestores_2: list[Gestor] = [] # Lista de Objetos(Gestor) com os dados da tabela

    for gestor  in gestores_1:
        gestores_2.append(Gestor(gestor[0], gestor[1], gestor[2],gestor[3],gestor[4], gestor[5], gestor[6]))

    connection.close()

    return gestores_2

def delete(gestor_id):
    """Deleta um gestor do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('DELETE FROM gestores WHERE id = ?', (str(gestor_id),))
    connection.commit()
    cursor.execute('DELETE FROM escolas_gestores WHERE gestores_id = ?', (str(gestor_id),))
    connection.commit()

    connection.close()


def get(gestor_id):
    """Pega um gestor especifico do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM gestores WHERE id = ?', (str(gestor_id),))
    row = cursor.fetchall()[0]
    gestor = Gestor(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    connection.close()

    return gestor

def update_managers(gestor_id,gestor: Gestor):
    """Atualiza um elemento no banco de dados"""
    connection, cursor = connect_db()

    cursor.execute("UPDATE gestores SET  nome= ?, email = ?, nascimento = ?, senha = ? WHERE id = ?", 
                   (gestor.nome, gestor.email,gestor.nascimento,gestor.senha, gestor_id))
    
    connection.commit()
    connection.close()  

def generate_manager_id(gestor: Gestor, escola):
    """Gera um id para o gestor"""
    nascimento = gestor.nascimento[:4]
    cod = nascimento + str(escola.escola_id)
    
    for n in range(3):
        cod += str(randint(0, 9))
    
    return cod

