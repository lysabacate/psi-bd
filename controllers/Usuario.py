from flask import render_template, request, redirect, flash
from models.Usuario import Usuario
from utils import db
from flask import Blueprint


bp_usuarios = Blueprint("usuarios", __name__, template_folder='templates')

@bp_usuarios.route('/teste')
def teste():
    return 'Teste'


@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
	if request.method=='GET':
		return render_template('usuarios_create.html')

	if request.method=='POST':
		nome = request.form.get('nome')
		email = request.form.get('email')
		senha = request.form.get('senha')
		csenha = request.form.get('csenha')
		usuario = Usuario(nome, email, senha)
		db.session.add(usuario)
		db.session.commit()
		return 'Dados cadastrados com sucesso!'
	
		#return redirect(url_for('.recovery'))