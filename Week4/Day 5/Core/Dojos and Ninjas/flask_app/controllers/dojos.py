from flask import  render_template, redirect, request 
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja




@app.route('/')
def dojo():
    return render_template("dojo.html")




@app.route('/dojos/create', methods=["post"])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')   


@app.route('/dojos')
def get_all():
    all_dojos = Dojo.get_all()
    
    return render_template("dojo.html" ,dojos = all_dojos)

@app.route('/dojos/<int:dojo_id>')
def get_one_by_id_with_ninjas(dojo_id):
    this_dojo = Dojo.get_one_by_id_with_ninjas({'id': dojo_id})
    return render_template('dojo_show.html', dojo = this_dojo)