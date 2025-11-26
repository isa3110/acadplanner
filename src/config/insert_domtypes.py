from model import *

def insert_relevancia():
    with ENGINE.connect() as conn:
        niveis_relevancia = [
            Relevancia(nivel="Baixa"),
            Relevancia(nivel="Média"),
            Relevancia(nivel="Alta"),
        ]

        conn.add_all(niveis_relevancia)
        conn.commit()

def insert_tipo_evento():
    with ENGINE.begin() as session:
        tipos_evento = [
            TipoEvento(nome="Prova"),
            TipoEvento(nome="Trabalho"),
            TipoEvento(nome="Projeto"),
        TipoEvento(nome="Seminário")
    ]

    session.add_all(tipos_evento)
    session.commit()