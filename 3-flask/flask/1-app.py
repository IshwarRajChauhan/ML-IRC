from flask import Flask
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''

##WSGI application
app = Flask(__name__)


#Home page
@app.route('/')  
def welcome():
    return "Welcome to the Flask App. Starting now and then"

@app.route('/index')  
def index():
    return "Welcome to the index page. Starting now and then"





if __name__ == '__main__':
    app.run(debug=True)


