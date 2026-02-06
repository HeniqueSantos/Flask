from estudo import app
from flask import render_template, url_for

@app.route('/')

def homepage():

    context = {
        'usuario1': {
             'nome': 'Henrique',
             'sobrenome': 'Dos Santos',
             'Gmail': 'seugmail@gmail.com',
             'Senha': '123456'
        },
        'usuario2': {}
    }
    return render_template('index.html', context=context)

@app.route('/bem-vindos')
def bem_vindos():
    return render_template('bem-vindos.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')