import random
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

number = random.randrange(0, 101)

@app.route('/')
def main():
      return render_template('index.html', debug = number)

@app.route('/verify', methods=['POST'])
def hint():
      session['guess'] = request.form['guess']
      guess = session['guess']
      
      if int(guess) > number: 
            return render_template('wrong.html', hint = ">")
      elif int(guess) < number: 
            return render_template('wrong.html', hint = "<")
      elif int(guess) == number:
            global number
            number = random.randrange(0, 101)
            return render_template('right.html')

      
app.run(debug=False)