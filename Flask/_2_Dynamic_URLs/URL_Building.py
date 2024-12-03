from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')

def home():
    return '<center><h1>Hello sir here you can check your score</h1></center>'

@app.route('/passed/<float:number>')

    # Pass Functon

def passed(number):
    if 100>= number >=90:
         return f'<center><h1> You passed your score is {number} Grade = O</h1></center>'
    elif 90> number >=80:
         return f'<center><h1> You passed your score is {number} Grade = A+</h1></center>'    
    elif 80> number >=70:
         return f'<center><h1> You passed your score is {number} Grade = A</h1></center>'
    elif 70> number >=60:
         return f'<center><h1> You passed your score is {number} Grade = B+</h1></center>'
    elif 60> number >=50:
         return f'<center><h1> You passed your score is {number} Grade = B</h1></center>'
    elif 50> number >=40:
         return f'<center><h1> You passed your score is {number} Grade = C+</h1></center>'
    elif 40> number >=30:
         return f'<center><h1> You passed your score is {number} Grade = C</h1></center>'
    elif number>100:
         return '<center><h1>Number should be range of 0 to 100</h1></center>'
    

    # Fail Function
    
@app.route('/failed/<float:number>')

def failed(number):
     return f'<center><h1>Sorry ! You Failed your score is {number}</h1></center>'
     

@app.route('/score/<float:num>')

def score(num):

    if num >= 30:
         return redirect(url_for('passed',number=num))
    else:
         return redirect(url_for('failed',number=num))
    
if __name__ == '__main__':
    app.run(debug=True)
