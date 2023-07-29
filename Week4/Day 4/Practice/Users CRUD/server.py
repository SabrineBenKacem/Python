from flask import Flask, render_template, redirect, request 
from user_model import User
app = Flask(__name__)

@app.route('/')
def read_all():
    all_users=User.get_all()
    
    return render_template('read_all.html', users = all_users)


@app.route('/users/new')
def new_user():
    return render_template("create.html")


@app.route('/users/create',  methods=['POST'])
def create_user():
    data_dict = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
    }
   
    User.create_user(data_dict)
    return redirect('/')


@app.route('/users')
def home():
    return redirect('/')

@app.route('/users/<int:user_id>')
def show (user_id):
    data_dict = {'id':user_id}
    user= User.get_one_by_id(data_dict)
    return render_template("read_one.html", user= user)


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    data_dict = {'id':user_id}
    user= User.get_one_by_id(data_dict)
    return render_template("edit.html", user= user)

@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user (user_id):
    data_dict = {**request.form}
    data_dict['id'] = user_id
    user= User.update_one_by_id(data_dict)
    return redirect(f'/users/{user_id}')

@app.route('/users/<int:user_id>/destroy', methods=['POST'])
def destroy(user_id):
    data_dict = {'id': user_id}
    User.destroy(data_dict)
    # redirect always to a route
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=5001)