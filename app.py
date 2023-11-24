from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/theory')
def theory():
    return render_template('theory.html')

@app.route('/encryption')
def encryption():
    return render_template('encryption.html')

if __name__ == '__main__':
    app.run(debug=True)

