from flask import Flask, request, jsonify, json
from flask_cors import CORS
from src.serve import get_model_api

app = Flask(__name__)
CORS(app) # needed for cross-domain requests, allow everything by default
model_api = get_model_api()

# default route
@app.route('/')
def index():
    return "Index API"

# HTTP Errors handlers
@app.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404

@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

# API route
@app.route('/api', methods=['POST'])
def api():
	input_url = request.json
	#input_url = request.args['url']
	output_data = model_api(input_url)
	response = jsonify(output_data)
	return response

if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True)
	app.run(debug=False)
