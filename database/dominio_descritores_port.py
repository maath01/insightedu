from banco import connect_db
import sqlite3

class DominioDescritoresPort:
    def __init__(self, id=None, aluno_id=0, descritor_1=0, descritor_2=0, descritor_3=0, 
                 descritor_4=0, descritor_5=0, descritor_6=0, descritor_7=0, descritor_8=0, 
                 descritor_9=0, descritor_10=0, descritor_11=0, descritor_12=0, descritor_13=0, 
                 descritor_14=0, descritor_15=0, descritor_16=0, descritor_17=0, descritor_18=0, 
                 descritor_19=0, descritor_20=0, descritor_21=0, descritor_22=0, descritor_23=0, 
                 descritor_24=0, descritor_25=0, descritor_26=0, descritor_27=0, descritor_28=0, 
                 descritor_29=0):
        self.id =id
        self.aluno_id = aluno_id
        self.descritor_1 = descritor_1
        self.descritor_2 = descritor_2
        self.descritor_3 = descritor_3
        self.descritor_4 = descritor_4
        self.descritor_5 = descritor_5
        self.descritor_6 = descritor_6
        self.descritor_7 = descritor_7
        self.descritor_8 = descritor_8
        self.descritor_9 = descritor_9
        self.descritor_10 = descritor_10
        self.descritor_11 = descritor_11
        self.descritor_12 = descritor_12
        self.descritor_13 = descritor_13
        self.descritor_14 = descritor_14
        self.descritor_15 = descritor_15
        self.descritor_16 = descritor_16
        self.descritor_17 = descritor_17
        self.descritor_18 = descritor_18
        self.descritor_19 = descritor_19
        self.descritor_20 = descritor_20
        self.descritor_21 = descritor_21
        self.descritor_22 = descritor_22
        self.descritor_23 = descritor_23
        self.descritor_24 = descritor_24
        self.descritor_25 = descritor_25
        self.descritor_26 = descritor_26
        self.descritor_27 = descritor_27
        self.descritor_28 = descritor_28
        self.descritor_29 = descritor_29
    

    def __str__(self) -> str:
      return str(self.id) + ' ' + str(self.descritor_1) + ' ' + str(self.descritor_2) + ' ' + str(self.descritor_3) + ' ' + str(self.descritor_4) + ' ' + str(self.descritor_5) + ' ' + str(self.descritor_6) + ' ' + str(self.descritor_7) + ' ' + str(self.descritor_8) + ' ' + str(self.descritor_9) + ' ' + str(self.descritor_10) + ' ' + str(self.descritor_11) + ' ' + str(self.descritor_12) + ' ' + str(self.descritor_13) + ' ' + str(self.descritor_14) + ' ' + str(self.descritor_15) + ' ' + str(self.descritor_16) + ' ' + str(self.descritor_17) + ' ' + str(self.descritor_18) + ' ' + str(self.descritor_19) + ' ' + str(self.descritor_20) + ' ' + str(self.descritor_21) + ' ' + str(self.descritor_22) + ' ' + str(self.descritor_23) + ' ' + str(self.descritor_24) + ' ' + str(self.descritor_25) + ' ' + str(self.descritor_26) + ' ' + str(self.descritor_27) + ' ' + str(self.descritor_28) + ' ' + str(self.descritor_29)


#-----------------------------------------------------------------------------------------------------------------------------------------------
def create(dominiodescritoresport: DominioDescritoresPort):
    """Insere um novo registro de descritores de portugues no banco de dados"""
    connection, cursor = connect_db()

    try:
        cursor.execute('SELECT 1 FROM dominio_descritores_port WHERE aluno_id = ?', (dominiodescritoresport.aluno_id,))
        existe = cursor.fetchone() 

        if existe:
            print (f"Erro: O aluno com ID {dominiodescritoresport.aluno_id} já está cadastrado no banco de dados.")
            return

        aluno_id = dominiodescritoresport.aluno_id
        cursor.execute('''
            INSERT INTO dominio_descritores_port (
                aluno_id, descritor_1, descritor_2, descritor_3, descritor_4, 
                descritor_5, descritor_6, descritor_7, descritor_8, descritor_9, 
                descritor_10, descritor_11, descritor_12, descritor_13, descritor_14, 
                descritor_15, descritor_16, descritor_17, descritor_18, descritor_19, 
                descritor_20, descritor_21, descritor_22, descritor_23, descritor_24, 
                descritor_25, descritor_26, descritor_27, descritor_28, descritor_29) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            aluno_id, dominiodescritoresport.descritor_1, dominiodescritoresport.descritor_2, 
            dominiodescritoresport.descritor_3, dominiodescritoresport.descritor_4, 
            dominiodescritoresport.descritor_5, dominiodescritoresport.descritor_6, 
            dominiodescritoresport.descritor_7, dominiodescritoresport.descritor_8, 
            dominiodescritoresport.descritor_9, dominiodescritoresport.descritor_10, 
            dominiodescritoresport.descritor_11, dominiodescritoresport.descritor_12, 
            dominiodescritoresport.descritor_13, dominiodescritoresport.descritor_14, 
            dominiodescritoresport.descritor_15, dominiodescritoresport.descritor_16, 
            dominiodescritoresport.descritor_17, dominiodescritoresport.descritor_18, 
            dominiodescritoresport.descritor_19, dominiodescritoresport.descritor_20, 
            dominiodescritoresport.descritor_21, dominiodescritoresport.descritor_22, 
            dominiodescritoresport.descritor_23, dominiodescritoresport.descritor_24, 
            dominiodescritoresport.descritor_25, dominiodescritoresport.descritor_26, 
            dominiodescritoresport.descritor_27, dominiodescritoresport.descritor_28, 
            dominiodescritoresport.descritor_29
        ))

        connection.commit()

    except sqlite3.Error as e:
        print(f"Erro ao inserir no banco de dados: {e}")

    connection.close()


def delete(id):
    """Deleta um registro de descritores de portugues no banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('DELETE FROM dominio_descritores_port WHERE id = ?', (str(id),))
    connection.commit()

    connection.close()


def list():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM dominio_descritores_port')
    dominio_port_1 = cursor.fetchall() # Lista com os dados da tabela
    dominio_port_2: list[DominioDescritoresPort] = [] # Lista de Objetos com os dados da tabela

    for dominio_port  in dominio_port_1:
        dominio_port_2.append(DominioDescritoresPort(dominio_port[0], dominio_port[1], dominio_port[2], dominio_port[3], dominio_port[4]))

    connection.close()

    return '\n'.join(str(obj) for obj in dominio_port_2)



def get(id):
    """Pega um registro de descritores de portugues especifico no banco de dados """
    connection, cursor = connect_db()
    cursor.execute('SELECT 1 FROM dominio_descritores_port WHERE id = ?', (id,))
    existe = cursor.fetchone() 
    if existe:
         cursor.execute('SELECT * FROM dominio_descritores_port WHERE id = ?', (str(id),))
         row = cursor.fetchall()[0]
         dominio_port = DominioDescritoresPort(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

         connection.close()

         return dominio_port
    else:
        print("O ID informado não existe no banco de dados")






