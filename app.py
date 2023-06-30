from flask import Flask, render_template, request, jsonify

import dataHandle

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/baike/data', methods=['POST'])
def queryData():
    word = request.json.get('word')
    page = request.json.get('page')
    pageSize = request.json.get('pageSize')
    return dataHandle.queryBaike(word, page, pageSize)


@app.route('/data')
def data():
    return render_template("data.html")


if __name__ == '__main__':
    app.run()
