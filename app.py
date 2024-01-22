from flask import Flask, jsonify
from service.service import generate_epl_mp3

app = Flask(__name__)

@app.route('/endpoint1', methods=['GET'])
def endpoint1():
    # to be implemented
    return jsonify({"message": "Response from endpoint1"})

@app.route('/generate/epl', methods=['POST'])
def generate_epl_news():
    generate_epl_mp3()
    return jsonify({"message": "sucess"})

if __name__ == '__main__':
    app.run(debug=True)