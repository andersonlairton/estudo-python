from flask import Flask
from file2 import outro_arquivo
from tipo_de_dados import tipoDados
from variaveis import variaveis
import sys

app = Flask(__name__)

@app.route('/')
def file2():
    return outro_arquivo()
# def hello_world():
#     return 'Hello, World! funciona atualização tbm debug true'

@app.route('/tipos-dados')
def tipodados():
    tipoDados()
    sys.stdout.flush()  # Força a saída do buffer
    return "#### fim excucao"  

@app.route('/fuction-dir')
def functionDir():

    #função dir lista todos os diretorios no escopo local
    print(dir(100))
    return "\n ### fim da execução"


@app.route("/variaveis")
def var():
    return variaveis()
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000,debug=true)
    app.run(host='0.0.0.0', port=5000, debug=True)

