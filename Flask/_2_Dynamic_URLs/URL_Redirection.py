from flask import Flask, redirect, url_for

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# Route for redirecting to another page
@app.route('/redirect_to_home')
def redirect_to_home():
    # Redirects to the home route
    return redirect(url_for('home'))

# Route for another example page
@app.route('/about')
def about():
    return "This is the About Page!"

# Route for redirecting to the about page
@app.route('/go_to_about')
def go_to_about():
    return redirect(url_for('about'))

if __name__ == '__main__':
    app.run(debug=True)
