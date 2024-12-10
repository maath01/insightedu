from database.banco import connect_db


def turmas_alunos(turma_id, aluno_id):
    """Associa uma turma e um aluno"""
    connection, cursor = connect_db()

    cursor.execute('INSERT INTO turmas_alunos (turmas_id, alunos_id) VALUES (?, ?)', (turma_id, aluno_id))

    connection.commit()
    connection.close()


def professores_turmas_materias(professor_id, turma_id, materia_id):
    """Associa uma turma a professores e os professores a materias"""
    connection, cursor = connect_db()

    cursor.execute('INSERT INTO professores_turmas_materias (professores_id, turmas_id, materias_id) VALUES (?, ?, ?)',
                    (professor_id,turma_id, materia_id))

    connection.commit()
    connection.close()


def escolas_gestores(escola_id, gestor_id):
    """Associa uma escola e um gestor"""
    connection, cursor = connect_db()

    cursor.execute('INSERT INTO escolas_gestores (escolas_id, gestores_id) VALUES (?, ?)', (escola_id, gestor_id))

    connection.commit()
    connection.close()


def escolas_turmas(escola_id, turma_id):
    """Associa uma escola e uma turma"""
    connection, cursor = connect_db()

    cursor.execute('INSERT INTO escolas_turmas (escolas_id, turmas_id) VALUES (?, ?)', (escola_id, turma_id))

    connection.commit()
    connection.close()


def escolas_coordenadores(escola_id, coordenador_id):
    """Associa uma escola e um coordenador"""
    connection, cursor = connect_db()

    cursor.execute('INSERT INTO escolas_coordenadores (escolas_id, coordenadores_id) VALUES (?, ?)', (escola_id, coordenador_id))

    connection.commit()
    connection.close()


def escolas_professores(escola_id, professor_id):
    """Associa uma escola e um professor"""
    connection, cursor = connect_db()

    cursor.execute('INSERT INTO escolas_professores (escolas_id, professores_id) VALUES (?, ?)', (escola_id, professor_id))

    connection.commit()
    connection.close()


def escolas_alunos(escola_id, aluno_id):
    """Associa uma escola e um aluno"""
    connection, cursor = connect_db()

    cursor.execute('INSERT INTO escolas_alunos (escolas_id, alunos_id) VALUES (?, ?)', (escola_id, aluno_id))

    connection.commit()
    connection.close()


def coordenadores_turmas(coordenador_id, turma_id):
    """Associa um coordenador a uma turma"""
    connection, cursor = connect_db()

    cursor.execute('INSERT INTO coordenadores_turmas (coordenadores_id, turmas_id) VALUES (?, ?)', (coordenador_id, turma_id))

    connection.commit()
    connection.close()

