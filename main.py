from flask import Flask , render_template ,request ,redirect ,url_for,flash
from database import get_products ,get_sales,get_stock,insert_products,insert_sales,insert_stock,available_stock,insert_user

# creating a flask instance
app = Flask(__name__)

app.secret_key = 'delicate88'

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
    full_name = request.form['full_name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    password = request.form['password']

    user_details = (full_name, phone_number, email, password)
    insert_user(user_details)
    flash("Registration successful", "success")
    return redirect(url_for('login'))

@app.route('/stock')
def stock():
    stock = get_stock()
    products = get_products()
    return render_template("stock.html",stock = stock, products = products)

@app.route('/manage_stock',methods=['GET','POST'])
def manage_stock():
    pid = request.form["pid"]
    stock_quantity= request.form["stockquantity"]

    new_stock=(pid,stock_quantity)
    insert_stock(new_stock)
    flash("Stock updated successfully","success")
    return redirect(url_for('stock'))

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
    flash("Product added successfully","success")
    return redirect(url_for('products'))

@app.route('/sales')
def sales():
    sales = get_sales()
    products = get_products()
    return render_template("sales.html", sales = sales, products = products)

@app.route('/make_sale', methods=['GET','POST'])
def make_sale():
    pid= request.form["pid"]
    quantity= request.form["quantity"]

    new_sale=(pid,quantity)
    check_stock = available_stock(pid)
    if check_stock < float(quantity):
        print("Insufficient stock")
        return redirect(url_for('sales'))
    insert_sales(new_sale)
    flash("Sale made successfully","success")
    return redirect(url_for('sales'))


app.run(debug=True)