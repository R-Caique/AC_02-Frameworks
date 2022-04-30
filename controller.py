import os
import sql
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('cadastro.html')

@app.route("/lista", methods=["GET", "POST"])
def lista():
    response = sql.getRegisters()
    print(response)
    return response

@app.route("/cadastros", methods=['POST'])
def cadastros():
    user = request.form['username']
    email = request.form['email']
    address = request.form['address']

    sql.register(user, email, address);
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)