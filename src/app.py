from flask import Flask
from file2 import outro_arquivo

app = Flask(__name__)

@app.route('/')
def file2():
    return outro_arquivo()
# def hello_world():
#     return 'Hello, World! funciona atualização tbm debug true'

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000,debug=true)
    app.run(host='0.0.0.0', port=5000, debug=True)

