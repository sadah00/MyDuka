from flask import Flask , render_template ,request ,redirect ,url_for
from database import get_products ,get_sales,insert_products

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
    stock = [200,100,50]
    return render_template("stock.html",stock = stock)

@app.route('/products')
def products():
    products = get_products()
    return render_template("products.html",products = products )

@app.route('/add_products',methods=['GET','POST'])
def add_products():
    product_name = request.form["product_name"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]

    new_products = (product_name,buying_price,selling_price)
    insert_products(new_products)
    return redirect(url_for('products'))

@app.route('/sales')
def sales():
    sales = get_sales()
    return render_template("sales.html", sales = sales)



app.run(debug=True)