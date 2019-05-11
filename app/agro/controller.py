# Author: Junior Tada
from flask import Blueprint, request, render_template, jsonify, flash, url_for, redirect
from app.db import sessao, Dao
from app.agro.model import Produtor
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
                nome = request.form['nome'].strip()
                produtor.nome = nome
                Dao(session).salvar(produtor)
                return render_template('agro/produtores.html')
        return render_template('agro/produtor.html')
    except Exception as e:
        msg = 'Erro ao cadastrar produtor!'
        log.exception(msg + str(e))
        flash(msg, 'alert-danger')
        return render_template('index.html')
