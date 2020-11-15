from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    message = "hello"
    return render_template('flash.html', message=message)


app.run(debug=True)