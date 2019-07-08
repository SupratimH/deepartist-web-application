from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from src.serve import get_model_api
import os
from time import sleep
from multiprocessing import Process


app = Flask(__name__)
CORS(app) # needed for cross-domain requests, allow everything by default
model_api = get_model_api()

# default route
@app.route('/')
def index():
    #return "<center><b>Welcome to DeepArtist, the art-lover bot!<b></center>"
	return render_template('find-artist.html')


# keep_alive method - always run a concurrent process
#@app.route('/keep_alive')
def keep_alive():
	while True:
		print("DeepArtist is alive!!")
		sleep(15)


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


# app page route
#@app.route('/deepartist')
#def deepartist():
#    return render_template('find-artist.html')


# API route
@app.route('/find_artist', methods=['POST'])
def api():
	input_url = request.json
	#input_url = request.args['url']
	output_data = model_api(input_url)
	response = jsonify(output_data)
	return response


if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True)
	p = Process(target=keep_alive)
	p.start()
	app.run(debug=False, use_reloader=False)
	p.join()
