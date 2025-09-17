from flask import Flask , render_template ,request ,redirect ,url_for,flash
from database import get_products ,get_sales,get_stock,insert_products,insert_sales,insert_stock,available_stock,insert_user,check_user
from flask_bcrypt import Bcrypt

# creating a flask instance
app = Flask(__name__)

bcrypt = Bcrypt(app)

app.secret_key = 'delicate88'

@app.route('/')  # unique routes
def home():  # must have a unique name
    return render_template("index.html")

@app.route('/dashboard') # decorator function
def dashboard(): # View function - giving back data
    return render_template("dashboard.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        registered_user = check_user(email)
        print(registered_user)
        if not registered_user:
            flash("User doesn't exist,Please Register","danger")
            return redirect(url_for('register'))
        else:
            if bcrypt.check_password_hash(registered_user[-1],password):
                flash("Logged in Successfully","Success")
                return redirect(url_for("dashboard"))
            else:
                flash("Password incorrect,try again","danger")
        
    return render_template("login.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        password = request.form['password']
        existing_user = check_user(email)

        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (full_name,phone_number,email,hashed_password)
            insert_user(new_user)
            flash("User registered successfully","success")
            return redirect(url_for('register'))
        
        else:
            flash("User already exists,please login","danger")
    return render_template("register.html")    

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