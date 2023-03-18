from flask import Flask, request, jsonify
from wordament_solver import find_words

app = Flask(__name__)


@app.route('/api/find-words', methods=['POST'])
def api_find_words():
    matrix = request.json.get('matrix')
    n = request.json.get('n')
    words = find_words(matrix, n)
    return jsonify(words=words)

