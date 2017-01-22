import sqlite3 as sql
from flask import request
from flask import Flask, render_template
app= Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start')
def start():
    return render_template('symptoms_form.html')

@app.route('/submit_form', methods=['POST'])
def submit():
    concussion_number = request.form['concussion_number']
    headache_level = request.form['headache_level']
    nauseous_level = request.form['nauseous_level']
    drowsy_level = request.form['drowsy_level']
    light_sensitivity_level = request.form['light_sensitivity_level']
    noise_sensitivity_level = request.form['noise_sensitivity_level']
    foggy_level = request.form['foggy_level']
    focus_level = request.form['focus_level']

    #Saving our questionarie to the database

    save_questionaire(concussion_number,headache_level, nauseous_level, drowsy_level, light_sensitivity_level, noise_sensitivity_level, foggy_level, focus_level)

    return render_template('test.html')

def save_questionaire(concussion_number,headache_level, nauseous_level, drowsy_level, light_sensitivity_level, noise_sensitivity_level, foggy_level, focus_level):
    connection = sql.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO questionaires (concussion_number,headache_level, nauseous_level, drowsy_level, light_sensitivity_level, noise_sensitivity_level, foggy_level, focus_level) VALUES (?,?,?,?,?,?,?,?)", (concussion_number,headache_level, nauseous_level, drowsy_level, light_sensitivity_level, noise_sensitivity_level, foggy_level, focus_level))
    connection.commit()
    connection.close()
