from banco import connect_db
import sqlite3
from random import randint

class Coordenador:
    
    def __init__(self, coordenador_id=0, nome='',email='',nascimento='',senha='') -> None:
        self.coordenador_id = coordenador_id
        self.nome = nome
        self.email = email
        self.nascimento=nascimento
        self.senha=senha

    def __str__(self) -> str:
        return str(self.coordenador_id) + ' ' + str(self.nome) 
 
def create(coordenador: Coordenador):
   
    connection, cursor = connect_db()

    try:
        coordenador_id = generate_coordinator_id(cursor,coordenador)

        cursor.execute('INSERT INTO coordenadores (id,nome,email,nascimento,senha) VALUES (?, ?, ?, ?,?)',
                        (coordenador_id, coordenador.nome, coordenador.email, coordenador.nascimento,coordenador.senha))

    except sqlite3.IntegrityError:
        print('ID duplicado')
    
    connection.commit()
    connection.close()


def delete(coordenador_id):
  
    connection, cursor = connect_db()

    cursor.execute('DELETE FROM coodenadores WHERE id = ?', (str(coordenador_id),))

    connection.commit()
    connection.close()


def list():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM coordenadores')
    coordenadores_1 = cursor.fetchall() # Lista com os dados da tabela
    coordenadores_2: list[Coordenador] = [] # Lista de Objetos(Professor) com os dados da tabela

    for coordenador  in coordenadores_1:
       coordenadores_2.append(Coordenador(coordenador[0],coordenador[1], coordenador[2],coordenador[3],coordenador[4]))

    connection.close()

    return coordenadores_2

def generate_coordinator_id(cursor: sqlite3.Cursor, coordenador: Coordenador):
    
    escola = '88901'
    nascimento = coordenador.nascimento[6:]
    cod = nascimento + escola
    
    for n in range(3):
        cod += str(randint(0, 9))
    
    return cod
