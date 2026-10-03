from flask import Flask, redirect,render_template,request,redirect,url_for



'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''


### Jinja2 Template Engine
'''
{{ }} expressions to print output in HTML
{%...%} conditions, for loops
{#...#} this is for comments
'''


##WSGI application
app = Flask(__name__)


#Routing between pages---------------------------------------------

#Home page
@app.route('/')  
def welcome():
    return '''<html>
    <body>
    <h1>Welcome to the Flask App. Starting now and then</h1>
    </body>
    </html>'''



@app.route('/index',methods=['GET'])  
def index():
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')



# @app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method == 'POST':
#         name=request.form['name']
#         return f"Hello {name}! How are you?"
#     else:
#         return render_template('form.html')




#To show results-------------------------------------------------

#Parameterized route
@app.route('/success/<int:score>')
def success(score): 
    res = ""
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"
    return render_template('result.html',result = res)


#printing using expression and using comments and loop in html file
@app.route('/successres/<int:score>')
def successres(score): 
    res = ""
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"

    exp={"score":score,"res":res}
    
    return render_template('result1.html',result = exp)
    

#using if in HTML--------------------------------------------------
@app.route('/successif/<int:score>')
def successif(score): 
    return render_template('result2.html',result = score)



@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',result=res)




@app.route('/submit', methods=['GET', 'POST'])
def submit():

    if request.method == 'POST':

        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science) / 4

        return redirect(url_for('successres', score=total_score))

    else:
        return render_template('getresult.html')








if __name__ == '__main__':
    app.run(debug=True)
















