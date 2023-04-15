from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/fetch-respell')
def fetch():
    query = request.args.get('input')

    #summary
    response = requests.post(
        "https://api.respell.ai/v1/run",
        headers={
            # This is your API key
            'Authorization': 'Bearer 65c2ebe8-2422-437c-8716-e8985e3413f5',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        data=json.dumps({
            "spellId": "rtiMOZbvZ0yXY3f5pb1fw",
            # This field can be omitted to run the latest published version
            "spellVersionId": 'Ynq52BAZgzRi9Hr4IRGiA',
            # Fill in dynamic values for each of your 2 input blocks
            "inputs": {
            "input": 'What is tehe S-R latch?',
            "summary_prompt": 'You are an AI teacher whose sole purpose is to explain the topic or question in a way that a college student can understand. Go step by step in your explanation and use plenty of examples and analogies and tie that back to the main point. Explain as if you were a kind, understanding teacher and talk in that manner too.',
            }
        }),
    )
    dictionary = json.loads(response.text)
    summary_output =  dictionary["outputs"]['output_summary']

    # Get a list of all the attributes and methods available for the response object
    return summary_output





if __name__ == '__main__':
    app.run(debug=True)