from flask import Flask , render_template 

# creating a flask instance
app = Flask(__name__)

@app.route('/')  # unique routes
def home():  # must have a unique name
    return render_template("index.html")

@app.route('/dashboard') # decorator function
def dashboard(): # View function - giving back data
    return render_template("dashboard.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/stock')
def stock():
    return render_template("stock.html")

@app.route('/products')
def products():
    products = ["Bread","Milk","Eggs"]
    return render_template("products.html")

@app.route('/sales')
def sales():
    sales = {"id 1":100, "id 2":200, "id 3":300}
    return render_template("sales.html")



app.run()