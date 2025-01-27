from database.banco import connect_db

class DescritorPort:

    def __init__(self, desc_id=0, habilidade='', serie=0, numero=0, materia=''):
        self.desc_id = desc_id
        self.habilidade = habilidade
        self.serie = serie
        self.numero = numero
        self.materia = materia
    
    def __str__(self):
        return f'Descritor {self.numero} {self.materia} - {self.habilidade}'
    


def list_descs():
    """Lista os descritores de português do banco de dados"""

    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM descritores_port')
    list_1 = cursor.fetchall()
    list_2: list[DescritorPort] = []

    for item in list_1:
        list_2.append(DescritorPort(item[0], item[1], item[2], item[3], item[4]))

    connection.close()

    return list_2


def get(desc_id):
    """Devolve um descritor especifico do banco de dados"""

    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM descritores_port WHERE id = ?', str(desc_id),)
    row = cursor.fetchall()[0]
    desc = DescritorPort(row[0], row[1], row[2], row[3], row[4])

    connection.close()

    return desc