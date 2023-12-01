import torch, os
import base64, uuid, os
from flask import Flask, render_template, url_for, request
from flask_cors import CORS, cross_origin

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    # Set whatever other headers you like...
    return response


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def get_out_text(text):
# Load model directly
	# Use a pipeline as a high-level helper
	from transformers import pipeline

	pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta")
		final_out = str(pipeline(sent)))

		return final_out


@app.route('/', methods=['POST','GET'])
def get_text():
    srcData = str(request.get_data())
    fm_out = get_out_text(srcData)

    return fm_out



if __name__ == '__main__':
    # run app in debug mode on port 3330
    app.run(debug=False, port=3330)
