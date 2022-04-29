from multiprocessing import context
from flask import Flask, make_response, redirect, render_template,request

app = Flask(__name__)

items = ["tenis","zapatillas","sandalias"]

@app.route('/index')
def index():  
    ipUsuario = request.remote_addr
    response = make_response(redirect('/informacion'))
    response.set_cookie('ipUsuario',ipUsuario)
    return render_template("base.html")

@app.route('/informacion')
def informacion():
    ipUsuario = request.cookies.get('ipUsuario')
    context = {
        "ipUsuario": ipUsuario,
        "items": items
    }
    return render_template("informacion.html", **context)

app.run(debug=True)