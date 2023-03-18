from flask import Flask, request, jsonify
from wordament_solver import find_words
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/api/find-words', methods=['POST'])
@cross_origin()
def api_find_words():
    matrix = request.json.get('matrix')
    n = request.json.get('n')
    words = find_words(matrix, n)
    return jsonify(words=words)

