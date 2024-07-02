from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from ecommercebot.retrieval_and_generation import generation
from ecommercebot.ingestion import ingestdata


app = Flask(__name__)

load_dotenv()

vstore = ingestdata("done")
chain = generation(vstore)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get', methods=['GET', 'POST'])
def chat():
    userText = request.form['msg']
    result = chain.invoke(userText)
    print("Response : ", result)
    return str(result)


if __name__ == '__main__':
    app.run(debug=True)