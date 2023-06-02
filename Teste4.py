from flask import Flask, render_template

meu_site = Flask(__name__)

#Criar a primeira pagina do site
@meu_site.route('/')

def homepage():
    return render_template('homepage.html')


@meu_site.route('/grau')
def contatos():
    return render_template('graudemoto.html')

@meu_site.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html',nome_usuario=nome_usuario)

#Colocar o site no ar

if __name__ == '__main__':
    meu_site.run(debug=True)
