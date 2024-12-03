from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return 'This is route'

# Path Parameters

@app.route('/welcome/<name>')

def name(name):
    return f'<h1>Hi {name} you are welcome</h1>'

# Path Parameters as Integer

@app.route('/add/<int:num>')

def add(num):
    return f'The number is {num} and the addition is {num + num}'

# Multiple Integer Parameter

@app.route('/add_two/<int:num1>/<int:num2>')

def add_two(num1,num2):
    return f'{num1} + {num2} = {num1+num2}'

if __name__ == '__main__':
    app.run(debug=True)