from flask import Flask 

app = Flask(__name__)

# Dyanamic URL using Path parameter 

@app.route('/')
@app.route('/home')

def home():
    return '<h1>Wecome to Flask App</h1>'

@app.route('/welcome/<name>')

def welcome(name):
    return f'<h1>Welcome {name.title()}</h1>'

if __name__ == '__main__':
    app.run(debug=True)