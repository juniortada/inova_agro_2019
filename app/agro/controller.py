# Author: Junior Tada
from flask import Blueprint, request, render_template, jsonify, flash, url_for, redirect
from app.db import sessao, Dao
from app.agro.model import Produtor, Producao
from app import log
import json


# Define o blueprint
agro = Blueprint('agro', __name__)

@agro.route('/produtor', methods=['GET'])
def produtor():
    """
        Método para exibição da página com todos os produtores cadastrados.
        :return: view com a página produtor.html 
    """
    try:
        with sessao() as session:
            produtores = Dao(session).todos(Produtor)
            return render_template('agro/produtores.html', produtores=produtores)
    except Exception as e:
        msg = 'Erro ao exibir produtores!'
        log.exception(msg + str(e))
        flash(msg, 'alert-danger')
        return render_template('index.html')


@agro.route('/produtor/novo', methods=['GET', 'POST'])
def produtor_novo():
    """
        Método cadastrar novo produtor.
        :return: view com a página de cadastro de produtor.html 
    """
    try:
        if request.method == 'POST':
            produtor = Produtor()
            with sessao() as session:
                produtor.nome = request.form['nome'].strip()
                produtor.nome_propriedade = request.form['nome_propriedade'].strip()
                produtor.tamanho = request.form['tamanho'].strip()
                Dao(session).salvar(produtor)
                return redirect(url_for('agro.produtor'))
        return render_template('agro/produtor.html')
    except Exception as e:
        msg = 'Erro ao cadastrar produtor!'
        log.exception(msg + str(e))
        flash(msg, 'alert-danger')
        return render_template('index.html')


@agro.route('/produtor/editar/<int:id>', methods=['GET', 'POST'])
def produtor_editar(id):
    """
        Método para editar dados do produtor
        :return: view com a página de edição de cadastro produtor.html 
    """
    try:
        with sessao() as session:
            produtor = Dao(session).buscarID(Produtor, int(id))
            if produtor:
                if request.method == 'POST':
                    produtor.nome = request.form['nome'].strip()
                    produtor.nome_propriedade = request.form['nome_propriedade'].strip()
                    produtor.tamanho = request.form['tamanho'].strip()
                    Dao(session).salvar(produtor)
                    return redirect(url_for('agro.produtor'))
                return render_template('agro/produtor.html', produtor=produtor)
    except Exception as e:
        msg = 'Erro ao editar produtor!'
        log.exception(msg + str(e))
        flash(msg, 'alert-danger')
        return render_template('index.html')


@agro.route('/_produtores/', methods=['GET', 'POST'])
def _produtores():
    """
        Método para consulta com todos os produtores cadastrados.
        :return: json com todos os produtores cadastrados. 
    """   
    try:
        with sessao() as session:
            produtores = Dao(session).todos(Produtor)
            produtores = [{"id":str(i.id),"nome":i.nome} for i in produtores]
            return jsonify(produtores=produtores)
    except Exception as e:
        log.exception('Erro ajax produtores!' + str(e))

@agro.route('/producao', methods=['GET'])
def producao():
    """
        Método para exibição da página com todas as produções.
        :return: view com a página producoes.html 
    """
    try:
        with sessao() as session:
            producoes = Dao(session).todos(Producao)
            return render_template('agro/producoes.html', producoes=producoes)
    except Exception as e:
        msg = 'Erro ao exibir produções!'
        log.exception(msg + str(e))
        flash(msg, 'alert-danger')
        return render_template('index.html')


@agro.route('/producao/novo', methods=['GET', 'POST'])
def producao_novo():
    try:
        if request.method == 'POST':
            producao = Producao()
            with sessao() as session:
                dao = Dao(session)
                if _salvar_producao(producao, dao):
                    flash('Produção Salvo com Sucesso!', 'alert-success')
                    return redirect(url_for('agro.producao'))
        return render_template('agro/producao.html')
    except Exception as e:
        msg = 'Erro ao cadastrar produção!'
        log.exception(msg + str(e))
        flash(msg, 'alert-danger')
        return render_template('index.html')


@agro.route('/producao/editar/<int:id>', methods=['GET', 'POST'])
def producao_editar(id):
    try:
        with sessao() as session:
            producao = Dao(session).buscarID(Producao, int(id))
            if producao:
                if request.method == 'POST':
                    dao = Dao(session)
                    if _salvar_producao(producao, dao):
                        flash('Produção Alterado com Sucesso!', 'alert-success')
                        return redirect(url_for('agro.producao'))
                return render_template('agro/producao.html', producao=producao)
    except Exception as e:
        msg = 'Erro ao editar produção!'
        log.exception(msg + str(e))
        flash(msg, 'alert-danger')
        return render_template('index.html')


@agro.route('/consulta', methods=['GET'])
def consulta():
    """
        Método para exibição da página com consulta por período.
        :return: view com a página consultas.html 
    """
    try:
        
        return render_template('agro/consultas.html')
    except Exception as e:
        msg = 'Erro ao exibir consultas!'
        log.exception(msg + str(e))
        flash(msg, 'alert-danger')
        return render_template('index.html')


def _salvar_producao(producao, dao):
    # produtor

    producao.produtor_id = request.form['produtor_id']
    if not producao.produtor_id:
        return False
    producao.data = request.form['data']
    producao.quantidade = request.form['quantidade']
    producao.ccs = request.form['ccs']
    producao.cmt = request.form['cmt']
    producao.cbt = request.form['cbt']
    producao.gordura = request.form['gordura']
    producao.proteina = request.form['proteina']
    producao.lactose = request.form['lactose']
    producao.solidos = request.form['solidos']
    dao.salvar(producao)
    return True