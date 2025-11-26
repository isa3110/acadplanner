from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import User, TipoEvento, Relevancia, DataEvento
from models import engine

events_bp = Blueprint('events', __name__, template_folder='templates', static_folder='static')

# TEM QUE AJEITAR TUDO DESSA ROTA

@events_bp.route('/events')
@login_required
def events():
    # Página de visualização dos eventos. Será disposto no HTML como cards de datas, onde a ordem será do mais próximo ao mais distante.
    with engine.begin() as conn:
        datas_eventos = conn.query(DataEvento).all()
    # Os dados de datas_eventos é retornado como uma lista de dicionários.
    return render_template('events.html', datas_eventos=datas_eventos)


@events_bp.route('/events/add', methods=['GET', 'POST'])
@login_required
def events_add():
    if request.method == 'POST':
        titulo_evento = request.form.get('titulo_evento')
        data = request.form.get('data')
        relevancia_id = int(request.form.get('relevancia'))
        tipo_evento_id = int(request.form.get('tipo_evento'))

        with session.begin():
            novo_evento = DataEvento(
                titulo_evento=titulo_evento,
                data=data,
                user_id=current_user.id,
                relevancia_id=relevancia_id,
                tipo_evento_id=tipo_evento_id
            )
            session.add(novo_evento)
            flash('Evento adicionado com sucesso!', 'success')
            return redirect(url_for('events.events'))

    if request.method == 'GET':
        # Pega os dados de relevância e tipo de evento para fazer o SELECT no formulário.
        relevancias: Relevancia = session.query(Relevancia).all()
        tipos_eventos: TipoEvento = session.query(TipoEvento).all()
        return render_template('events_add.html', 
                            relevancias=relevancias, 
                            tipos_eventos=tipos_eventos)


@events_bp.route('/events/delete/<int:event_id>', methods=['POST'])
@login_required
def events_delete(event_id):
    evento = session.get(DataEvento, event_id)
    if evento:
        try:
            with session.begin():
                session.delete(evento)
                flash('Evento deletado com sucesso!', 'success')
        except Exception as e:
            flash(f'Erro ao deletar o evento: {str(e)}', 'error')
    else:
        flash('Evento não encontrado.', 'error')
    return redirect(url_for('events.events'))


@events_bp.route('/events/edit/<int:event_id>', methods=['GET', 'POST'])
@login_required
def events_edit(event_id):
    if request.method == 'POST':
        evento = session.get(DataEvento, event_id)
        if evento:
            titulo_evento = request.form.get('titulo_evento')
            data = request.form.get('data')
            relevancia_id = int(request.form.get('relevancia'))
            tipo_evento_id = int(request.form.get('tipo_evento'))

            with session.begin():
                evento_atualizado = session.get(DataEvento, event_id)
                evento_atualizado.titulo_evento = titulo_evento
                evento_atualizado.data = data
                evento_atualizado.relevancia_id = relevancia_id
                evento_atualizado.tipo_evento_id = tipo_evento_id
                session.add(evento)
                flash('Evento atualizado com sucesso!', 'success')
                return redirect(url_for('events.events'))
        else:
            flash('Evento não encontrado.', 'error')
            return redirect(url_for('events.events'))
    
    if request.method == 'GET':
        evento = session.get(DataEvento, event_id)
        if evento:
            relevancias = session.query(Relevancia).all()
            tipos_eventos = session.query(TipoEvento).all()
            return render_template('events_edit.html', 
                                evento=evento, 
                                relevancias=relevancias, 
                                tipos_eventos=tipos_eventos)
        else:
            flash('Evento não encontrado.', 'error')
            return redirect(url_for('events.events'))
    