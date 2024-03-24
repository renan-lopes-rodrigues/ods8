from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def main():
    with open('database/custos/custos.json') as custos:
        custos = json.load(custos)
    return render_template('main.html', custos=custos)