from flask import Flask

dados = {
            "name":"John",
            "age":30,
            "cars":["Ford", "BMW", "Fiat"]
        }

webApp = Flask(__name__)

@webApp.route('/info')
def index():
    return dados

webApp.run(debug=True)