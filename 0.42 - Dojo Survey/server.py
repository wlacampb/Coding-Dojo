from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def prompt():
      return render_template("index.html")

@app.route('/result', methods=['POST'])
def display():
      name_choice = request.form['name']
      location_choice = request.form['location']
      language_choice = request.form['language']
      comment_choice = request.form['comment']
      return render_template("result.html", name = name_choice, location = location_choice, language = language_choice, comment = comment_choice)

app.run(debug=True)