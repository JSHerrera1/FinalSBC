from flask import Flask, render_template, request
from fetchTerm import fetchTerm

app = Flask(__name__)


@app.get('/')
def index():

    context = {
        'title': 'Buscador de términos',
        'content': 'Sistemas Basdos en el Conocimiento - 2022'
    }

    return render_template('index.html', **context)


@app.post('/search')
def search():
    term = request.form['term']
    responses = fetchTerm(term)

    context = {
        'title': 'Buscador de términos',
        'content': f'Resultados de la búsqueda: {term}',
        'responses': responses
    }

    return render_template('search.html', **context)

@app.post('/detail/<idterm>')
def more(idterm):
    responses = fetchTerm(idterm)
    context = {
        'title': 'Buscador de términos',
        'content': f'Resultados de la búsqueda: {idterm}',
        'responses': responses
    }
    return render_template('more.html', **context)


app.run(host='', port=8080, debug=True)
