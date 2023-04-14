from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.users_model import User

@app.route('/users', methods=['GET'])
def get_users():
    list_of_users = User.get_all()
    print("list_of_users")
    return render_template("index.html", list_of_users=list_of_users)

@app.route( "/user/form", methods=["GET"] )
def display_todo_form():
    return render_template( "create.html")

@app.route('/user/create', methods=['POST'])
def create_user(): 
        print(request.form)
        new_user = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
        }
        user_id = User.create_one(new_user)
        return redirect('/users')

@app.route( "/user/delete/<int:id>", methods=['POST'] )
def delete_user( id ):
    data = {
        "users_id": id
    }
    User.delete_one(data)
    return redirect('/users' )

@app.route( "/user/edit/<int:id>", methods=['GET'] )
def display_user_edit_form( id ):
    data = {
        "users_id" : id
    }
    current_user = User.get_one( data )
    return render_template( "edit_user.html", current_user = current_user )

@app.route( "/user/update/<int:id>", methods=['POST'] )
def update_user( id ):
    update_user = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "users_id" : id
    }
    User.update_one( update_user )
    return redirect( '/users')

@app.route( "/show/<int:id>", methods = ['GET'])
def show_user(id):
    data = {
        "users_id" : id
    }
    list_of_user = User.get_users(data)
    print("list_of_user")
    return render_template("show.html", list_of_user=list_of_user)