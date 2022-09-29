from flask_app import app
from flask import request, render_template, redirect
from flask_app.models.models_ninja import Ninja
from flask_app.models.models_dojo import Dojo

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all_dojos()
    return render_template('/ninjas.html', dojos=dojos)

# Add ninja
@app.route('/add_ninja', methods=['POST'])
def add_ninja():
    Ninja.add_ninja(request.form)
    dojo = request.form['dojo_id']
    return redirect(f'/dojos/{dojo}')

# Update ninja
@app.route('/ninjas/edit/<int:id>')
def update_form(id):
    data = {
        "id": id
    }
    ninja = Ninja.get_one_ninja(data)
    dojo = Dojo.get_dojo_id_and_name(data)
    return render_template('/edit_ninja.html', id=id, ninja=ninja[0], dojo=dojo[0])

@app.route('/ninjas/edit/<int:id>/update', methods=['POST'])
def update_ninja(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_dojo_id_and_name(data)
    dojo_id = dojo[0]['id']
    Ninja.update_ninja(request.form)
    return redirect(f'/dojos/{dojo_id}')

# Delete ninja
@app.route('/delete/<int:id>')
def delete_ninja(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_dojo_id_and_name(data)
    dojo_id = dojo[0]['id']
    Ninja.delete_ninja(data)
    return redirect(f'/dojos/{dojo_id}')
