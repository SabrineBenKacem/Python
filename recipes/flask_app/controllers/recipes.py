from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/recipes/new')
def new_recipe():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("new_recipe.html")

@app.route('/recipes/create', methods=['POST'])
def add_recipe():
    # print(request.form,"****************")
    if Recipe.validate(request.form):
        data_dict= {
            **request.form,
            'user_id':session['user_id']
        }
        Recipe.create(data_dict)
        return redirect('/dashboard')
    return redirect('/recipes/new')

@app.route('/recipes/<int:recipe_id>/edit')
def edit_recipe(recipe_id):
    if'user_id' not in session:
        return redirect('/')
    
    my_recipe = Recipe.get_by_id({'id':recipe_id})
    # print(my_recipe,"****************")
    return render_template("edit.html", recipe = my_recipe)



@app.route('/recipes/<int:recipe_id>/update', methods=['POST'])
def update_recipe(recipe_id):
    # print(request.form,"****************")
    if Recipe.validate(request.form):
      data_dict = {
        **request.form,
        'id':recipe_id
    }
      Recipe.update(data_dict)
    
      return redirect('/dashboard')
    return redirect(f"/recipes/{recipe_id}/edit")


@app.route('/recipes/<int:recipe_id>')
def view_recipe(recipe_id):
    data_dict = {'id':recipe_id}
    recipe= Recipe.get_by_id(data_dict)
    return render_template("view.html", recipe= recipe)

@app.route('/recipes/<int:recipe_id>/destroy',methods=['POST'])
def destroy(recipe_id):
    Recipe.delete({'id':recipe_id})
    return redirect('/dashboard')


