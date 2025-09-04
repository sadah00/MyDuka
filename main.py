from flask import Flask , render_template

# creating a flask instance
app = Flask(__name__)

@app.route('/')  # unique routes
def home():  # must have a unique name
    return "My index route"
 
@app.route('/contact') # decorator function  
def contact(): # View function - giving back data
    return "Contact Us"

@app.route('/login')
def login():
    return "Sign in"

@app.route('/Register')
def register():
    return "Sign up"

@app.route('/info')
def info():
    return "Display more information"

@app.route('/products')
def products():
    products = ["Bread","Milk","Eggs"]
    return products

@app.route('/sales')
def sales():
    sales = {"id 1":100, "id 2":200, "id 3":300}
    return sales



app.run()