# get modules, define app in global namespace, session key
from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

# global counter
counter = 0

# routing rules
@app.route('/')
def iterator(): 
      global counter
      counter += 1
      session['views'] = counter
      return render_template('index.html')

@app.route('/twice', methods=['POST'])
def double_iterator():
      global counter
      counter += 1
      session['views'] = counter
      return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
      global counter
      counter = 0
      session['views'] = counter
      return redirect('/')

# start server
app.run(debug=True)