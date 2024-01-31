from flask import Flask, render_template, request, jsonify
import psycopg2
from config import db_name, user, password, host

app = Flask(__name__)

def fetch_data(query):
    with psycopg2.connect(database=db_name, user=user, host=host, password=password) as conn:
        with conn.cursor() as curs:
            curs.execute(query)
            result = curs.fetchall()
            column_names = [desc[0] for desc in curs.description]
            return {'column_names': column_names, 'data': result}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign.html')
def sign():
    return render_template('sign.html')


@app.route('/query', methods=['GET'])
def handle_query():
    query = request.args.get('query', '')
    data = fetch_data(query)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
