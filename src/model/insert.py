from model import session, Relevancia, TipoEvento

def insert_relevancia():
    niveis_relevancia = [
        Relevancia(nivel="Baixa"),
        Relevancia(nivel="Média"),
        Relevancia(nivel="Alta"),
    ]

    session.add_all(niveis_relevancia)
    session.commit()

def insert_tipo_evento():
    tipos_evento = [
        TipoEvento(nome="Prova"),
        TipoEvento(nome="Trabalho"),
        TipoEvento(nome="Projeto"),
        TipoEvento(nome="Seminário")
    ]

    session.add_all(tipos_evento)
    session.commit()