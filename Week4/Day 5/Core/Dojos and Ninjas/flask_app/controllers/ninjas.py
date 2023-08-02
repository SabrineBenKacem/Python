from flask import  render_template, redirect, request 
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja




@app.route('/ninjas')
def ninja():
    all_dojos = Dojo.get_all()
    return render_template("ninja.html", dojos = all_dojos)




@app.route('/ninjas/create', methods=["post"])
def create_ninja():
    print(request.form,"****************")
    Ninja.create_ninja(request.form)
    return redirect('/dojos') 

@app.route('/dojos')
def home():
    return redirect('/')



