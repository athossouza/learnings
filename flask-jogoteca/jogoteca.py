from flask import Flask, render_template, request, redirect

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

    # def __str__(self):
    #     return  f'{self.nome}, {self.categoria}, {self.console}'

jogo1 = Jogo('Tetris','Puzzly','Atari')
jogo2 = Jogo('Batlefield','Tiro','Playstation')
jogo3 = Jogo('God of War', 'Rock n Slash', 'PS4')

listajogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Lista.html', titulo='Jogos', jogos=listajogos)

@app.route('/novo')
def novo():
    return render_template('Novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    listajogos.append(jogo)
    return redirect('/')



app.run(debug=True)