from flask import Flask,render_template
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''

##WSGI application
app = Flask(__name__)


#Home page
@app.route('/')  
def welcome():
    return '''<html>
    <body>
    <h1>Welcome to the Flask App. Starting now and then</h1>
    </body>
    </html>'''



@app.route('/index')  
def index():
    return render_template('index.html')



@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)
















