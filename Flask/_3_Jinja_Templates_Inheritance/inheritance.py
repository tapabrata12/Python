from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')

def home():
    return render_template("i_home.html",title ="Home")

@app.route('/about')

def about():
    return render_template("i_about.html",title = "About")

if __name__ == "__main__":
    app.run(debug=True)