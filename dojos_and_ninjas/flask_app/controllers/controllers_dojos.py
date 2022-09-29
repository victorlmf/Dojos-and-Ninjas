from flask_app import app
from flask import request, render_template, redirect
from flask_app.models.models_dojo import Dojo

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all_dojos()
    return render_template('/dojos.html', dojos=dojos)

# Add Dojo
@app.route('/add_dojo', methods=['POST'])
def add_dojo():
    Dojo.add_dojo(request.form)
    return redirect('/dojos')

# Show Dojo
@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('/dojo.html', dojo=dojo)

