from flask_app import app
from flask import render_template,redirect,request
from flask_app.models import dojo,ninja

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html",dojos = dojo.Dojo.get_all())


@app.route('/show/<int:ninjas_id>')
def show(ninjas_id):
    data = {
        'id': ninjas_id
    }
    return render_template("ninjas.html",ninjas = ninja.Ninja.get_one(data))

@app.route('/ninjas/edit/<int:ninjas_id>')
def edit_page(ninjas_id):
    data = {
        'id': ninjas_id
    }
    return render_template("ninjas_edit.html", ninjas = ninja.Ninja.get_one(data))

@app.route('/ninjas/update', methods=['POST'])
def update_ninja():
    ninja.Ninja.update(request.form)
    return redirect('/')

@app.route('/ninjas/delete/<int:ninjas_id>')
def delete(ninjas_id):
    data = {
        'id': ninjas_id
    }
    ninja.Ninja.delete(data)
    return redirect('/dojos')