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
	pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta",
		#temperature=0.7,  # 'randomness' of outputs, 0.0 is the min and 1.0 the max
		#top_p=0.15,  # select from top tokens whose probability add up to 15%
		#top_k=0,  # select from top 0 tokens (because zero, relies on top_p)
		max_new_tokens=1024,  # mex number of tokens to generate in the output
		repetition_penalty=1.1)
	final_out = str(pipe(text))
	print(final_out)

	return final_out


@app.route('/', methods=['POST'])
def get_text():
    srcData = str(request.get_data())
    fm_out = get_out_text(srcData)

    return fm_out



if __name__ == '__main__':
    # run app in debug mode on port 3330
    app.run(debug=False, port=3330)
