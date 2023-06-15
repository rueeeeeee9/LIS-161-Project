from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/devices/<brand>')
def devices(brand):
    smartphones_list = read_smartphones_by_brand(brand)
    return render_template('devices.html',brand=brand, smartphones=smartphones_list)

@app.route('/devices/<int:smartphone_id>')
def smartphone(smartphone_id):
    smartphone = read_smartphone_by_id(smartphone_id)
    return render_template('smartphone.html',smartphone=smartphone)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/processed', methods=['POST'])
def processing():
    smartphone_data = {
        "brand": request.form['brand'],
        "model": request.form['brand_model'],
        "chipset": request.form['brand_chipset'],
        "main_camera": request.form['brand_main_camera'],
        "selfie_camera": request.form['brand_selfie_camera'],
        "internal_memory": request.form['brand_internal_memory'],
        "battery": request.form['brand_battery'],
        "color": request.form['brand_color'],
        "price": request.form['brand_price'],
        "condition": request.form['brand_condition'],
        "reason_for_selling": request.form['brand_reason_for_selling'],
        "url": request.form['brand_url']
    }
    insert_smartphone(smartphone_data)
    return redirect(url_for('devices', brand=request.form['brand']))

@app.route('/modify', methods=['post'])
def modify():
 if request.form["modify"] == "edit":
    smartphone_id = request.form["smartphone_id"]
    smartphone = read_smartphone_by_id(smartphone_id)
    return render_template('update.html', smartphone=smartphone)
 elif request.form["modify"] == "delete":
    smartphone_id =request.form["smartphone_id"]
    smartphone = read_smartphone_by_id(smartphone_id)
    delete_smartphone(smartphone_id)
    return redirect(url_for("devices", smartphone['brand']))

@app.route('/update', methods=['post'])
def update():
    smartphone_data = {
        "id": request.form["smartphone_id"],
        "brand": request.form['smartphone_brand'],
        "model": request.form['smartphone_model'],
        "chipset": request.form['smartphone_chipset'],
        "main_camera": request.form['smartphone_main_camera'],
        "selfie_camera": request.form['smartphone_selfie_camera'],
        "internal_memory": request.form['smartphone_internal_memory'],
        "battery": request.form['smartphone_battery'],
        "color": request.form['smartphone_color'],
        "price": request.form['smartphone_price'],
        "condition": request.form['smartphone_condition'],
        "reason_for_selling": request.form['smartphone_reason_for_selling'],
        "url": request.form['smartphone_url']
    }
    update_smartphone(smartphone_data)
    return redirect(url_for('smartphone', smartphone_id = request.form['smartphone_id']))

@app.route('/search', methods=['get'])
def search():
    query = request.args.get('query', '')
    results = search_smartphones(query)
    return render_template('search_results.html', query=query, results=results)
   
if __name__ == "__main__":
    app.run(debug=True)