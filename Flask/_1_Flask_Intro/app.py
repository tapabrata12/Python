from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>This is home page</h1>'

# Creating another end Point

@app.route('/about')

def about():
    return '<h1>This is about page</h1>'

if __name__ == "__main__":
    app.run(debug=True)
