from flask import Flask, render_template, request
from calculadora import calcular

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return calcular()

    return render_template('calculadora.html', etapas='', resultados='')

@app.route('/pagina-inicial')

def pagina_inicial():
    return render_template('pagina_inicial.html')

if __name__ == '__main__':
    app.run(debug=True)