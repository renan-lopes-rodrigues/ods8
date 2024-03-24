from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def main():
    with open('database/custos/fixos.json') as custos_fixos:
        custos_fixos = json.load(custos_fixos)
    return render_template('main.html', custos_fixos=custos_fixos)