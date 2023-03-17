from flask import Flask, request, jsonify
from wordament_solver import find_words
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.debug = True

@app.route('/api/find-words', methods=['POST'])
def api_find_words():
    matrix = request.json.get('matrix')
    n = request.json.get('n')
    words = find_words(matrix, n)
    return jsonify(words=words)


if __name__ == '__main__':
    app.run()
