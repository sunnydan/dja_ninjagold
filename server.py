from flask import Flask, render_template, redirect, request, session
import random
from time import gmtime, strftime
app = Flask(__name__)
app.secret_key = "420blazeit"

@app.route('/')
def index():
    try:
        return render_template('index.html', gold=session['gold'], activities=list(reversed(session['activities'])), gained=session["gained"])
    except:
        session['gold'] = 0
        session['activities'] = []
    return render_template('index.html', gold=session['gold'], activities=list(reversed(session['activities'])))

@app.route('/process_money', methods=['POST'])
def process():
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    if request.form['building'] == "reset":
        session['gold'] = 0
        session['activities'] = []
        session['gained'] = True
    if request.form['building'] == "farm":
        i = random.randint(10, 20)
        session['activities'].append("<p style='color: green;'>Earned "+str(i)+" gold(s) from the farm! ("+time+")</p>")
        session['gold'] += i
        session['gained'] = True
    if request.form['building'] == "cave":
        i = random.randint(5, 10)
        session['activities'].append("<p style='color: green;'>Earned "+str(i)+" gold(s) from the cave! ("+time+")</p>")
        session['gold'] += i
        session['gained'] = True
    if request.form['building'] == "house":
        i = random.randint(2, 5)
        session['activities'].append("<p style='color: green;'>Earned "+str(i)+" gold(s) from the house! ("+time+")</p>")
        session['gold'] += i
        session['gained'] = True
    if request.form['building'] == "casino":
        i = random.randint(-50, 50)
        if i >= 0:
            session['activities'].append("<p style='color: green;'>Earned "+str(i)+" gold(s) from the casino! ("+time+")</p>")
            session['gained'] = True
        else:
            session['activities'].append("<p style='color: red;'>Lost "+str(abs(i))+" gold(s) from the casino! ("+time+")</p>")
            session['gained'] = False
        session['gold'] += i
    return redirect('/')

app.run(debug=True)