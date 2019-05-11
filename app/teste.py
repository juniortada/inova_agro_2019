from app import get_uri
from app.db import sessao, Dao
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import json


def criar_db():
    """ 
    Cria o banco de dados caso ele não exista.
    O nome do banco será o definido no config DB_URI. 
    """
    dados = get_uri()
    con = psycopg2.connect("dbname='postgres' user='"+dados['user']+"' host='localhost' password='"+dados['password']+"'")
    cur = con.cursor()
    cur.execute("select datname from pg_catalog.pg_database where datname='"+dados['db']+"'")
    if not bool(cur.rowcount):
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur.execute('CREATE DATABASE ' + dados['db'])
    cur.close()
    con.close()


def alterar_config():
    "Muda config CRIAR_DB para False"
    filel = __file__.replace('teste.py','')+'config.json'
    cfg = None
    with open(filel, 'r') as arq:
        cfg = json.loads(arq.read())
    if cfg is not None:
        cfg['CRIAR_DB'] = False
        with open(filel, 'w') as arq:
            arq.write(json.dumps(cfg, indent=2))