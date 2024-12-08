from banco import connect_db
import sqlite3
from random import randint

class Gestores:
    
    def __init__(self, gestor_id=0, nome='',email='',nascimento='',senha='') -> None:
        self.gestor_id = gestor_id
        self.nome = nome
        self.email = email
        self.nascimento=nascimento
        self.senha=senha

    def __str__(self) -> str:
        return str(self.gestor_id) + ' ' + str(self.nome) 
    
def create(gestor: Gestores):
   
    connection, cursor = connect_db()

    try:
        gestor_id = generate_manager_id(cursor,gestor)

        cursor.execute('INSERT INTO gestores (id, nome, email, nascimento, senha) VALUES (?, ?, ?, ?, ?)',
                        (gestor_id, gestor.nome, gestor.email, gestor.nascimento,gestor.senha))

    except sqlite3.IntegrityError:
        print('ID duplicado')
    
    connection.commit()
    connection.close()

def list():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM gestores')
    gestores_1 = cursor.fetchall() # Lista com os dados da tabela
    gestores_2: list[Gestores] = [] # Lista de Objetos(Professor) com os dados da tabela

    for gestor  in gestores_1:
        gestores_2.append(Gestores(gestor[0], gestor[1], gestor[2],gestor[3],gestor[4]))

    connection.close()

    return gestores_2

def delete(gestor_id):
   
    connection, cursor = connect_db()

    cursor.execute('DELETE FROM gestores WHERE id = ?', (str(gestor_id),))

    connection.commit()
    connection.close()

def generate_manager_id(cursor: sqlite3.Cursor, gestor: Gestores):
  
    escola = '88901'
    nascimento = gestor.nascimento[6:]
    cod = nascimento + escola
    
    for n in range(3):
        cod += str(randint(0, 9))
    
    return cod

